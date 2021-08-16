import os
from flask import Flask
from flask.templating import render_template
from flask_restful import Api
from flask_jwt import JWT

from auth.user import identity_user, authenticated_user
from resources.jasa import JasaKategori,JasaKategoriId,JasaSubKategori, JasaSubKategoriId, JasaSatuan, Jasa, JasaId, JasaByKat, JasaBySub
from resources.keahlian import *
from resources.user import UserRegister, UserDetail

app = Flask(__name__)
uri = os.getenv('DATABASE_URL')
if uri and uri.startswith('postgres://'):
    uri =uri.replace('postgres://','postgresql://',1)
else:
    uri = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI']= uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jastukang_v1'
api = Api(app)

app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt_user = JWT(app, authenticated_user, identity_user)

@app.route('/')
def home():
    jasa = Jasa()
    items = jasa.get()
    return render_template('index.html', items=items['jasa'])

api.add_resource(JasaKategori, '/kategori_jasa')
api.add_resource(JasaKategoriId, '/kategori_jasa/<string:id>')
api.add_resource(JasaSubKategori,'/sub_kategori_jasa')
api.add_resource(JasaSubKategoriId,'/sub_kategori_jasa/<string:id>')
api.add_resource(JasaSatuan, '/satuan')
api.add_resource(Keahlian, '/keahlian')
api.add_resource(KeahlianId, '/keahlian/<string:id>')
api.add_resource(Jasa,'/jasa')
api.add_resource(JasaId,'/jasa/<string:id>')
api.add_resource(JasaByKat,'/get_jasa/<string:kategori>')
api.add_resource(JasaBySub,'/get_jasa/<string:kategori>/<string:sub_kategori>')

api.add_resource(UserRegister,'/user/register')
api.add_resource(UserDetail,'/user/add_detail')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)