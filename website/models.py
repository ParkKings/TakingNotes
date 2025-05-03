from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  # Stores the creation date/time with timezone info
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  # A foreign key is a column in a database that refrences a column of another database
  # in sql the name of the class gets refrenced in lowercase and the .id means we are wanting the id
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, data, user_id):
    self.data = data
    self.user_id = user_id

# UserMixin provides user sessions and authentications such as is_aunthenticated or get_id()
class User(db.Model , UserMixin):
  # A primary key in a database is a unique identifier for each record (row) in a table
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  # One-to-many relationship: a user can have many notes
  notes = db.relationship('Note')
  def __init__(self, email, first_name, password):
      self.email = email
      self.first_name = first_name
      self.password = password