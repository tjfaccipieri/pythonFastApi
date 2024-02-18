from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
  __tablename__ = 'tb_users'

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50), unique=True)
  fullname = Column(String(100))

  posts = relationship("Post", back_populates="owner")


class Post(Base):
  __tablename__ = 'tb_posts'

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(50))
  content = Column(String(100))
  user_id = Column(Integer, ForeignKey('tb_users.id'))

  owner = relationship("User", back_populates="posts")