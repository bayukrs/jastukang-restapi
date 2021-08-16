from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.jasa import JasaKategoriModel, JasaModel, JasaSubKategoriModel, SatuanJasaModel

class JasaKategori(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nama',
        type=str,
        required= True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'id',
        type=str,
        required = True,
        help = "This field canno be left blank"
    )
    def get(self):
        return {'kategori':[x.json() for x in JasaKategoriModel.query.all()]}

    def post(self):
        data = JasaKategori.parser.parse_args()
        if JasaKategoriModel.find_by_id(data['id']):
            return {'message':"Kategori dengan id '{}' sudah ada".format(data['id'])}, 400
        
        item = JasaKategoriModel(**data)
        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return item.json(), 201

class JasaKategoriId(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nama',
        type=str,
        required= True,
        help="This field cannot be left blank"
    )
    def get(self, id):
        kategori = JasaKategoriModel.find_by_id(id)
        if kategori:
            return kategori.json()
        return {'message':'Item not found'}, 404

    def put(self, id):
        data = JasaKategoriId.parser.parse_args()
        kategori = JasaKategoriModel.find_by_id(id)
        if kategori is None:
            return {"message": "Item not found"}
        kategori.nama = data['nama']
        kategori.save_to_db()
        return kategori.json()
    
    def delete(self, id):
        kategori = JasaKategoriModel.find_by_id(id)

        if kategori:
            kategori.delete_from_db()
        return {'message':'Kategori deleted'}


class JasaSubKategori(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nama',
        type=str,
        required= True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'id_kategori',
        type=str,
        required= True,
        help="This field cannot be left blank"
    )
    def get(self):
        return {'sub_kategori':[x.json() for x in JasaSubKategoriModel.query.all()]}

    def post(self):
        data = JasaSubKategori.parser.parse_args()
        if JasaSubKategoriModel.find_by_name(data['nama']):
            return {'message':"Sub Kategori dengan nama '{}' sudah ada".format(data['nama'])}, 400
        id_kategori = JasaSubKategoriModel.new_id(data['id_kategori'])
        item = JasaSubKategoriModel(id_kategori, **data)
        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return item.json(), 201

    
class JasaSubKategoriId(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nama',
        type=str,
        required= True,
        help="This field cannot be left blank"
    )
    
    def get(self, id):
        sub_kategori = JasaSubKategoriModel.find_by_id(id)
        if sub_kategori:
            return sub_kategori.json()
        return {'message':'Item not found'}, 404

    def put(self, id):
        data = JasaSubKategoriId.parser.parse_args()
        kategori = JasaSubKategoriModel.find_by_id(id)
        if kategori is None:
            return {"message": "Item not found"}
        kategori.nama = data['nama']
        kategori.save_to_db()
        return kategori.json()

    def delete(self, id):
        sub_kategori = JasaSubKategoriModel.find_by_id(id)
        if sub_kategori:
            sub_kategori.delete_from_db()
        return {'message':'Sub Kategori deleted'}


class JasaSatuan(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nama',
        type=str,
        required= True,
        help="This field cannot be left blank"
    )

    def get(self):
        return {'sub_kategori':[x.json() for x in SatuanJasaModel.query.all()]}

    def post(self):
        data = JasaSatuan.parser.parse_args()
        if SatuanJasaModel.find_by_name(data['nama']):
            return {'message':"Satuan dengan nama '{}' sudah ada".format(data['nama'])}, 400
        item = SatuanJasaModel(**data)
        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return item.json(), 201


class parser_jasa():
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nama_jasa',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'harga_harian',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'harga_borongan',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'kategori',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'sub_kategori',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'kemampuan',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'keahlian',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'gambar',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'deskripsi',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'satuan',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )


class Jasa(Resource):
    def get(self):
        return {"jasa":[x.json() for x in JasaModel.query.all()]}

    def post(self):
        data = parser_jasa.parser.parse_args()
        if JasaModel.find_by_id(data['nama_jasa']):
            return {'message':"Satuan dengan nama_jasa '{}' sudah ada".format(data['nama'])}, 400
        id_jasa = JasaModel.add_id(data['sub_kategori'])
        item = JasaModel(id_jasa, **data)
        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item"}, 500
        return item.json(), 201


class JasaId(Resource):
    def get(self, id):
        jasa = JasaModel.find_by_id(id)
        if jasa:
            return jasa.json()
        return {'message':'Item not found'}, 404

    def put(self, id):
        jasa = JasaModel.find_by_id(id)
        if jasa is None:
            return {'message':'Item not found'}, 404
        data = parser_jasa.parser.parse_args()
        for key,value in data.items():
            if getattr(jasa, key):
                setattr(jasa, key, value)
        jasa.save_to_db()
        return jasa.json()

    def delete(self, id):
        jasa = JasaModel.find_by_id(id)
        if jasa:
            jasa.delete_from_db()
        return {"message":"Jasa deleted"}



class JasaBySub(Resource):
    def get(self, kategori, sub_kategori):
        return {"jasa":[x.json() for x in JasaModel.find_by_sub_kategori(kategori, sub_kategori)]}


class JasaByKat(Resource):
    def get(self, kategori):
        return {"jasa":[x.json() for x in JasaModel.find_by_kategori(kategori)]}