from extensions import api,db
from flask_restx import Resource , fields , Namespace
from flask import Flask , request
from models import Course


course_ns = Namespace("courses" , description="Course operations")

# model seralizer
course_model = course_ns.model(
    "Course",{
        "id":fields.Integer(),
        "title":fields.String(),
        "description": fields.String(),
        "image_url":fields.String(),
        "price":fields.Float(),
        "total_hours":fields.Integer(),
        "rating":fields.Integer()
        
    }
)

### validation ###

course_input_model = course_ns.model(
    "CourseInput",{
        "title": fields.String(required=True),
        "description": fields.String(required=True),
        "price": fields.Float(required=True),
        "total_hours": fields.Integer(required=True),
        "image_url":fields.String(required=True),
        "rating": fields.Integer(required=True)
        
    }
)


@course_ns.route("/")
class CoursesResource(Resource):
    @course_ns.marshal_list_with(course_model)
    def get(self):
        """get all courses"""
        return Course.query.all()

    @course_ns.expect(course_input_model)
    @course_ns.marshal_with(course_model)
    def post(self):
        """create course"""
        data = course_ns.payload
        new_course = Course(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            total_hours=data.get('total_hours'),
            image_url = data.get('image_url'),
            rating=data.get('rating')
        )
        db.session.add(new_course)
        db.session.commit()
        return new_course, 201



@course_ns.route("/<int:id>")
class CourseResource(Resource):
    @course_ns.marshal_with(course_model)
    def get(self , id):
        """get course by id"""
        return Course.query.get_or_404(id)

    @course_ns.expect(course_input_model)
    @course_ns.marshal_with(course_model)
    def put(self , id):
        """update cousre by id"""
        course_to_update = Course.query.get_or_404(id)
        data = course_ns.payload
        course_to_update.title = data.get('title' ,  course_to_update.title )
        course_to_update.description = data.get('description' ,  course_to_update.description)
        course_to_update.price = data.get('price' , course_to_update.price)
        course_to_update.total_hours = data.get('total_hours' , course_to_update.total_hours)
        course_to_update.rating = data.get('rating', course_to_update.rating)
        course_to_update.image_url = data.get('image_url' , course_to_update.image_url ),

        db.session.commit()
        return course_to_update, 200


    def delete(self , id):
        """delete by id"""
        course_to_delete = Course.query.get_or_404(id)
        db.session.delete(course_to_delete)
        db.session.commit()
        return "", 204
