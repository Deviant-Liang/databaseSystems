from shop import db
from datetime import datetime, timedelta
from flask_login import login_required, current_user, logout_user, login_user


class Addproduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    start_sale_date = db.Column(db.DateTime, nullable=False,default=datetime.today)
    end_sale_date = db.Column(db.DateTime, nullable=False,default=datetime.now()+timedelta(days=14))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<Post %r>' % self.name



db.create_all()