from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.user import UserDetailModel, UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "status",
        type=int,
        required=True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "role_id",
        type=int,
        required=True,
        help = "This field cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return {"message":"A user with that email already exists"}, 400
        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return {"message":"User success created"}, 201


class UserDetail(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id_user",
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        "nama_depan",
        type=str,
        required= True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        "nama_belakang",
        type = str,
        required = True,
        help="This field cannot be left balnk"
    )
    parser.add_argument(
        "alamat",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "no_hp",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "email",
        type = str,
        required = True,
        help = "This filed cannot be left blank"
    )
    parser.add_argument(
        "kecamatan",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "foto",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "token",
        type = int,
        required = True,
        help = "This field cannot be left blank"
    )

    @jwt_required()
    def post(self):
        data = UserDetail.parser.parse_args()
        if UserDetailModel.find_by_id(data['id']):
            return {"message":"A user with that email already exists"}, 400
        user = UserDetailModel(**data)
        try:
            user.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return {"message":"User success created"}, 201