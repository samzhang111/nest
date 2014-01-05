from sqlalchemy import Table, Column, Integer, ForeignKey, String
from database import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('posts.id'))
    body = Column(String(21844))
    parent_left = Column(Integer)
    parent_right = Column(Integer)
    lineage = Column(String(21844))
    depth = Column(Integer)
    
    def __init__(self, parent_id, body, parent_left, parent_right, depth):
        self.parent_id = parent_id
        self.body = body
        self.parent_left = parent_left
        self.parent_right = parent_right
        self.depth = depth

        self.lineage = ''


    def __repr__(self):
        return '<Post %r>' % self.lineage
