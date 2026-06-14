from flask import request 
from models import User
from flask_restx import Resource, fields , Namespace
from extensions import api , db


user_ns = Namespace("users" , description="User's operations")

## seralization ##

user_model = user_ns.model(
    "User",{
        "id": fields.Integer(),
        "first_name": fields.String(),
        "last_name": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "role": fields.String(),
    }
)

## validation ##

user_input_model = user_ns.model(
    "UserInput",{
        "id": fields.Integer(required=True),
        "first_name": fields.String(required=True),
        "last_name": fields.String(required=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
        "role": fields.String(required=True),
    }
)


## CRUD ##

@user_ns.route("/")
class UsersResources(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """ get all users"""
        return User.query.all()

    @user_ns.marshal_with(user_model)
    @user_ns.expect(user_input_model)
    def post(self):
        """create a user"""
        data = user_ns.payload
        new_user = User(
            id= data.get('id'),
            first_name= data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            role=data.get('role')
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user , 201

@user_ns.route("/<int:id>") 
class UserResource(Resource):
    @user_ns.marshal_with(user_model)
    def get(self , id):
        """ get user by id"""
        return User.query.get_or_404(id)

    @user_ns.marshal_with(user_model)
    @user_ns.expect(user_input_model)
    def put(self , id):
        """ update user by id"""
        user_to_update = User.query.get_or_404(id)
        data = user_ns.payload
        user_to_update.first_name = data.get('first_name' , user_to_update.first_name),
        user_to_update.last_name = data.get('last_name' , user_to_update.last_name),
        user_to_update.email = data.get('email' , user_to_update.email),
        user_to_update.password = data.get('password' , user_to_update.password),
        user_to_update.role = data.get('role' , user_to_update.role)

        db.session.commit()
        return user_to_update,200

    def delete(self , id):
        """ delete user by id """
        user_to_delete = User.query.get_or_404(id)
        db.session.delete(user_to_delete)
        return "" , 204


