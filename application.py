from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
  pass
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'

db = SQLAlchemy(app, model_class=Base)



class Drink(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(120))
    
    def __repr__(self):
      return f'{self.name} - {self.description}'
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def get_drinks():
    return {"drinks": "get drinks"}
  
if __name__ == '__main__':
    app.run(debug=True)
