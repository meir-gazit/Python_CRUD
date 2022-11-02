# Python_CRUD

This is a very simple example of how to create an Python CRUD operation using the FASTAPI library, the DB module opens a connection to very simple Postgres DB with only products table, there are 5 endpoints in main.py, one to get everything, another to get by ID, one to create, one to update and last one to delete products, the product schema is very simple and all the code is just to give you an idea of how CRUD should look like with Python.

In order to use the sample you should do some steps 

1.first look in the DB module and have it as reference to create your DB product table

2. create a folder and drop in it this 3 py files 

3. create from your terminal a virtual environment using the "py -3 -m venv <virtual environment name> command

4. point your interpreter to use the virtual environment by the name you defined

5. start the virtual environment by calling "environment name/Scripts/ativate.bat"

6. install FastAPI, psycopg2 and pydantic dependencies, they will be installed in the VE and not in the global environment

7. link the project to use your python that in the bin folder in the VE

8. start your server using the "uvicorn mainapp --reload" command, see the docs in the FastAPI website [https://fastapi.tiangolo.com/tutorial] for more info

9. go to the URL from your web browser or postman or any other app that can communicate with this simple sample


Hope it Will help someone.

Enjoy.
