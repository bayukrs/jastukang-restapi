from db import db

class JasaKategoriModel(db.Model):
    __tablename__ = 'jasa_kategori'

    id = db.Column(db.String, primary_key=True)
    nama = db.Column(db.String)

    sub_kategori = db.relationship('JasaSubKategoriModel', lazy = 'dynamic')
    jasa = db.relationship('JasaModel', lazy='dynamic')

    def __init__(self, id, nama):
        self.id = id
        self.nama = nama

    def json(self):
        return {
            'id':self.id, 
            'nama':self.nama, 
            'sub_kategori':[item.json() for item in self.sub_kategori.all()],
            'jasa':[x.json() for x in self.jasa.all()]
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class JasaSubKategoriModel(db.Model):
    __tablename__ = 'jasa_sub_kategori'

    id = db.Column(db.String, primary_key = True)
    nama = db.Column(db.String)

    id_kategori = db.Column(db.String, db.ForeignKey('jasa_kategori.id'))
    kategori = db.relationship('JasaKategoriModel')
    jasa = db.relationship('JasaModel', lazy='dynamic')

    def __init__(self, id, nama, id_kategori):
        self.id = id
        self.nama = nama
        self.id_kategori = id_kategori

    def json(self):
        return {
            'id':self.id, 
            'nama':self.nama, 
            'id_kategori':self.id_kategori,
            'jasa':[x.json() for x in self.jasa.all()]
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, nama):
        return cls.query.filter_by(nama=nama).first()

    @classmethod
    def new_id(cls, id_kategori):
        last_id = cls.query.filter_by(id_kategori = id_kategori).order_by(cls.id_kategori.desc()).first()
        if last_id is None:
            new_id = id_kategori + '01'
            return new_id
        huruf = last_id.id[:1]
        angka = last_id.id[2:]
        new_num = str(int(angka) + 1)
        if len(new_num) == 2:
            new_id = huruf + new_num
            return new_id
        new_id = huruf + '0' + new_num
        return new_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class SatuanJasaModel(db.Model):
    __tablename__ = 'jasa_satuan'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String)

    jasa = db.relationship('JasaModel', lazy='dynamic')

    def __init__(self, nama):
        self.nama = nama

    def json(self):
        return {'nama':self.nama, 'jasa':[x.json() for x in self.jasa.all()]}

    @classmethod
    def find_by_name(cls, nama):
        return cls.query.filter_by(nama=nama).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class JasaModel(db.Model):
    __tablename__ = 'jasa'

    id = db.Column(db.String, primary_key = True)
    nama_jasa = db.Column(db.String)
    harga_harian = db.Column(db.Integer)
    harga_borongan = db.Column(db.Integer)
    kategori = db.Column(db.String, db.ForeignKey('jasa_kategori.id'))
    sub_kategori = db.Column(db.String, db.ForeignKey('jasa_sub_kategori.id'))
    kemampuan = db.Column(db.Integer)
    keahlian = db.Column(db.String, db.ForeignKey('keahlian_jasa.id'))
    gambar = db.Column(db.String)
    deskripsi = db.Column(db.Text)
    satuan = db.Column(db.Integer, db.ForeignKey('jasa_satuan.id'))

    kategori_item = db.relationship('JasaKategoriModel')
    sub_kategori_item = db.relationship('JasaSubKategoriModel')
    keahlian_item = db.relationship('KeahlianModel')
    satuan_item = db.relationship('SatuanJasaModel')

    def __init__(self, id, nama_jasa, harga_harian, harga_borongan, kategori, sub_kategori, kemampuan, keahlian, gambar, deskripsi, satuan):
        self.id = id
        self.nama_jasa = nama_jasa
        self.harga_harian = harga_harian
        self.harga_borongan = harga_borongan
        self.kategori = kategori
        self.sub_kategori = sub_kategori
        self.kemampuan = kemampuan
        self.keahlian = keahlian
        self.gambar = gambar
        self.deskripsi = deskripsi
        self.satuan = satuan

    def json(self):
        return {
            "id":self.id,
            "nama":self.nama_jasa,
            "harga_harian":self.harga_harian,
            "harga_borongan":self.harga_borongan,
            "kategori":self.kategori,
            "sub_kategori":self.sub_kategori,
            "kemampuan":self.kemampuan,
            "keahlian":self.keahlian,
            "gambar":self.gambar,
            "deskripsi":self.deskripsi,
            "satuan":self.satuan
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_kategori(cls, kategori):
        return cls.query.filter_by(kategori=kategori)

    @classmethod
    def find_by_sub_kategori(cls,kategori, sub_kategori):
        return cls.query.filter_by(kategori = kategori, sub_kategori=sub_kategori)

    @classmethod
    def add_id(cls, sub_kategori):
        last_id = cls.query.filter_by(sub_kategori=sub_kategori).order_by(cls.sub_kategori.desc()).first()
        if last_id is None:
            new_id = sub_kategori + "_01"
            return new_id
        huruf = last_id.id[:4]
        angka = last_id.id[5:]
        new_num = str(int(angka) + 1)
        if len(new_num) == 2:
            new_id = huruf + new_num
            return new_id
        new_id = huruf + '0' + new_num
        return new_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()