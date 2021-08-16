from db import db

class UserModel(db.Model):
    __tablename__ = 'user_account'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    status = db.Column(db.Integer)
    role_id = db.Column(db.Integer)

    def __init__(self, email, password, status, role_id):
        self.email = email
        self.password = password
        self.status = status
        self.role_id = role_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email= email).first()


class UserDetailModel(db.Model):
    __tablename__ = "user_detail"

    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('user_account.id'))
    nama_depan = db.Column(db.String)
    nama_belakang = db.Column(db.String)
    alamat = db.Column(db.String)
    no_hp = db.Column(db.String)
    email = db.Column(db.String)
    kecamatan = db.Column(db.String)
    foto = db.Column(db.String)
    token = db.Column(db.Integer)

    def __init__(self, _id, nama_depan, nama_belakang, alamat, no_hp, email, kecamatan, foto, token):
        self.id_user = _id
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.alamat = alamat
        self.no_hp = no_hp
        self.email = email
        self.kecamatan = kecamatan
        self.foto = foto
        self.token = token

    def json(self):
        return {
            "id_user":self.id_user,
            "nama_depan":self.nama_depan,
            "nama_belakang":self.nama_belakang,
            "alamat":self.alamat,
            "no_hp":self.no_hp,
            "email":self.email,
            "kecamatan":self.Kecamatan,
            "foto":self.foto,
            "token":self.token
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()