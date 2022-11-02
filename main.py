from fastapi import FastAPI, Response, status, HTTPException
import Product
import DB

app = FastAPI()
cursor = DB.conn.cursor()


@app.get("/products")
def get_all():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return {"data": products}


@app.get("/products/{id}")
def get_by_id(id: str):
    cursor.execute("SELECT * FROM products WHERE id = %s", (str(id)))
    product = cursor.fetchone()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"product details": product}


@app.post("/products")
def create(product: Product):
    cursor.execute("""INSERT INTO products (name,description,for_sale,in_stock,price) 
        VALUES (%s,%s,%s) RETURNING *""", (product.title,product.content,product.published))
    product = cursor.fetchone()
    DB.conn.commit()
    return {"data": product}


@app.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str):
    cursor.execute("DELETE FROM products WHERE id = %s RETURNING *", (str(id)))
    deleted_product = cursor.fetchone()
    DB.conn.commit()
    if not deleted_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"product id[{id}] does not exist.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/products/{id}")
def update(id: int, product: Product):
    cursor.execute("UPDATE products name = %s, description = %s, for_sale = %s, in_stock = %s, price = %s WHERE id = %s RETURNING *", 
    (product.name, product.description, product.for_sale, product.in_stock, product.price, (str(id))))
    updated_product = cursor.fetchone()
    DB.conn.commit()
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"product id[{str(id)}] does not exist.")
    return {"data: ", updated_product}
