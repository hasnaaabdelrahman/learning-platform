from extensions import api,db
from flask_restx import Resource , fields , Namespace
from flask import request
from models import Comment

comment_ns = Namespace("comments" , description="Comment operations")


##  serializtion ##

comment_model = comment_ns.model(
    "Comment",{
        "id": fields.Integer(),
        "content": fields.String()
    }
)

### validation ###

comment_input_model = comment_ns.model(
    "CommentInput",{
        "content": fields.String(required=True)
    }
)

@comment_ns.route("/")
class CommentsResources(Resource):
    @comment_ns.marshal_list_with(comment_model)
    def get(self):
        """ get all comments """
        return Comment.query.all()
    
    @comment_ns.expect(comment_input_model)
    @comment_ns.marshal_with(comment_model)
    def post(self):
        """ create a comment """
        data = comment_ns.payload
        new_comment = Comment(
            content= data.get('content')
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment, 201

@comment_ns.route("/<int:id>")
class CommentResource(Resource):
    @comment_ns.marshal_with(comment_model)
    def get(self , id):
        """ get comment by id"""
        return Comment.query.get_or_404(id)

    @comment_ns.marshal_with(comment_model)
    @comment_ns.expect(comment_input_model)
    def put(self , id):
        """ update a comment with id"""
        comment_to_update = Comment.query.get_or_404(id)
        data = comment_ns.payload
        comment_to_update.content = data.get('content' , comment_to_update.content)
        db.session.commit()
        return comment_to_update,200
    
    def delete(self , id):
        """ delete comment by id """
        comment_to_delete = Comment.query.get_or_404(id)
        db.session.delete(comment_to_delete)
        db.session.commit()
        return "",204




    

