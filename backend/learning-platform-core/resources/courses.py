from extensions import api,db
from flask_restx import Resource , fields
from flask import Flask , request
from models import Course

# model seralizer
course_model = api.model(
    "Course",{
        "id":fields.Integer(),
        "title":fields.String(),
        "description": fields.String(),
        "price":fields.Float(),
        "total_hours":fields.Integer(),
        "rating":fields.Integer()
        
    }
)


@api.route("/courses")
class CoursesResource(Resource):
    @api.marshal_list_with(course_model)
    def get(self):
        """get all courses"""
        return Course.query.all()

    @api.marshal_with(course_model)
    def post(self):
        """create course"""
        data = request.get_json()
        new_course = Course(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            total_hours=data.get('total_hours'),
            rating=data.get('rating')
        )
        db.session.add(new_course)
        db.session.commit()
        return new_course, 201



@api.route("/course/<int:id>")
class CourseResource(Resource):
    @api.marshal_with(course_model)
    def get(self , id):
        """get course by id"""
        return Course.query.get_or_404(id)

    @api.marshal_with(course_model)
    def put(self , id):
        """update cousre by id"""
        course_to_update = Course.query.get_or_404(id)
        data = request.get_json()
        course_to_update.title = data.get('title' ,  course_to_update.title )
        course_to_update.description = data.get('description' ,  course_to_update.description)
        course_to_update.price = data.get('price' , course_to_update.price)
        course_to_update.total_hours = data.get('total_hours' , course_to_update.total_hours)
        course_to_update.rating = data.get('rating', course_to_update.rating)
        db.session.commit()
        return course_to_update, 200


    @api.marshal_with(course_model)
    def delete(self , id):
        """delete by id"""
        course_to_delete = Course.query.get_or_404(id)
        db.session.delete(course_to_delete)
        db.session.commit()
        return "", 204
