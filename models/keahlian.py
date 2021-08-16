from db import db

class KeahlianModel(db.Model):
    __tablename__ = "keahlian_jasa"

    id = db.Column(db.String, primary_key=True)
    nama = db.Column(db.String)

    def __init__(self, id, nama):
        self.id = id
        self.nama = nama

    def json(self):
        return {"id":self.id, "nama":self.nama}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()