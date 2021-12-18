# Python ORM

- **Why Python programming is awesome**

    As a general-purpose language, Python is the single language that you may ever need for developing just about anything.

    It can be used for the programming of the front end (client side) with which users interact and back end (server side) database of your website. It can be used for numerical and data analysis for scientific study and research. It can be used to develop artificial intelligence. It can be used to develop both online and offline applications from productivity tools, games and other type of app you can think off.
- **How to connect to a MySQL database from a Python script**

```python
import MySQLdb
db = MySQLdb.connect(host=MY_HOST, 
                                                user=MY_USER, 
                                                passwd=MY_PASS, 
                                                db=MY_DB)
```

- **How to `SELECT` rows in a MySQL table from a Python script**

```python
import MySQLdb
db = MySQLdb.connect(host="host", user="user", 
                                                    passwd="passwd", db="database")
cursor = db.cursor()
cursor.execute("""SELECT * FROM table_name WHERE id = x""")
rows = cursor.fetchall()
    for r in rows:
        print(r)

cursor.close()
db.close()

```

- **How to `INSERT` rows in a MySQL table from a Python script**

```python
import MySQLdb
db = MySQLdb.connect(host="host", user="user", 
                                                    passwd="passwd", db="database")
cursor = db.cursor()
cursor.execute("""INSERT INTO table_name (value1, value2) 
                                    VALUES ("string1", "String2")""")
rows = cursor.fetchall()
    for r in rows:
        print(r)

cursor.close()
db.close()
```

- **What ORM means**

    Object relational mapping.

- **How to map a Python Class to a MySQL table**

```python
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = sqlalchemy.create_engine('mysql://host:1234@localhost:3306/database_name')
Base = declarative_base()

class User(Base):
    __tablename__= 'User'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

Base.medata.create_all(engine)

```

## What is a object relational mapping

ORM is a code library that automates the transfer of data stored in relational database tables into objects.

![https://www.fullstackpython.com/img/visuals/orms-bridge.png](https://www.fullstackpython.com/img/visuals/orms-bridge.png)

### Why are ORMs useful?

provide a high-level abstraction upon a [relational database](https://www.fullstackpython.com/databases.html) that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.

### What are the downsides of using an ORM?

There are numerous downsides of ORMs, including

1. Impedance mismatch

    Impedance mismatch is a catch-all term for the difficulties that occur when moving data between relational tables and application objects. The gist is that the way a developer uses objects is different from how data is stored and joined in relational tables.

    [](http://www.agiledata.org/essays/impedanceMismatch.html)

2. Potential for reduced performance

    With ORMs, the performance hit comes from the translation of application code into a corresponding SQL statement which may not be tuned properly.

3. Shifting complexity from the database into the application code.

    The addition of data handling logic in the codebase generally isn't an issue with a sound application design, but it does increase the total amount of Python code instead of splitting code between the application and the database stored procedures.

![Take a look at the table which shows how ORMs can work with different web frameworks and connectors and relational databases.](https://www.fullstackpython.com/img/visuals/orm-examples.png)

Take a look at the table which shows how ORMs can work with different web frameworks and connectors and relational databases.

### Resources

[Object-relational Mappers (ORMs)](https://www.fullstackpython.com/object-relational-mappers-orms.html)

[https://mysqlclient.readthedocs.io/user_guide.html](https://mysqlclient.readthedocs.io/user_guide.html)

[Python MySQL Documentation](https://www.mikusa.com/python-mysql-docs/index.html)

[SQLAlchemy 1.4 Documentation](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

[SQLAlchemy 1.4 Documentation](https://docs.sqlalchemy.org/en/13/)

[Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)

[Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)

[10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)

[SQLAlchemy - pysheeet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)

[SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

[SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
