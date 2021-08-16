from flask_restful import Resource,reqparse

from models.keahlian import KeahlianModel

class Keahlian(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument(
        "nama",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )

    def get(self):
        return {"keahlian":[x.json() for x in KeahlianModel.query.all()]}

    def post(self):
        data = Keahlian.parser.parse_args()
        if KeahlianModel.find_by_id(data['id']):
            return {"message":"An satuan with id '{}' already exists".format(data['id'])}
        item = KeahlianModel(**data)
        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return item.json(), 201


class KeahlianId(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nama",
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )

    def get(self, id):
        keahlian = KeahlianModel.find_by_id(id)
        if keahlian:
            return keahlian.json()
        return {"message":"Keahlian not found"}

    def put(self, id):
        keahlian = KeahlianModel.find_by_id(id)
        if keahlian is None:
            return {"message": "Item not found"}
        data = KeahlianId.parser.parse_args()
        keahlian.nama = data['nama']
        keahlian.save_to_db()
        return keahlian.json()

    def delete(self, id):
        keahlian = KeahlianModel.find_by_id(id)

        if keahlian:
            keahlian.delete_from_db()
        return {'message':'keahlian deleted'}