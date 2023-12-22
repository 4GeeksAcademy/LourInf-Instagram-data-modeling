import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# We use declarative_base() from SQLAlchemy to create a base class (Base)
Base = declarative_base()

# We create a class (1 class = 1 table) that will inherit from the base class. Naming convention: PascalCase, plural:
class Users(Base):
    # 1. We create the table alias __tablename__. Naming convention: snake_case
    __tablename__ = "users"
    # 2. We define the columns of the table:
    # 2.1. We define the primary key, with data type,primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. We define the model attributes, with data type
    email = Column(String, unique=True)
    username = Column(String(50),nullable=False)
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50),nullable=False)
    image_url = Column(String(150))

class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    # 2.2. We define the model attributes, with data type: no attributes here
    # 2.3. We define the foreign key, with data type,ForeignKey("alias.id")
    followers_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))
    # 3. We define the relationships: relationship(Models)
    followers = relationship(Users)  # follower_id int fk >- users.id
    following = relationship(Users)  # int fk >- users.id

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship(Users)  # author_id int fk >- users.id
    
class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    url = Column(String(150))
    type = Column(Enum("image", "video"))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)  # post_id int fk >- post.id
    
class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200))
    author_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    author = relationship(Users)  # author_id int fk >- users.id
    post = relationship(Post)  # post_id int fk >- post.id

   
    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
