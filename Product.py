from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    for_sale: bool = True
    in_stock: int
    price: float
    