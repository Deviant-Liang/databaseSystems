from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .model import Register
from shop import db, login_manager




class CustomerRegisterForm(FlaskForm):
    name = StringField('Name: ')
    email = StringField('Email: ', [validators.DataRequired()])
    phone = StringField('Phone: ', [validators.DataRequired()])
    type = StringField('Type: ', [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired(), validators.EqualTo('confirm', message=' Both password must match! ')])
    confirm = PasswordField('Repeat Password: ', [validators.DataRequired()])
    submit = SubmitField('Register')
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")

    


class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])



class CustomerUpdateFrom(FlaskForm):
    name = StringField('Name: ', [validators.DataRequired()])
    phone = StringField('Phone: ', [validators.DataRequired()])  
    def update(self, id, name, phone):  
        if (name!=None) and (phone!=None):
            num_rows_updated = Register.query.filter_by(id=id).update(dict(name=name))
            db.session.commit()
            num_rows_updated = Register.query.filter_by(id=id).update(dict(phone=phone))
            db.session.commit()

   




   

 

    

     

   


    

