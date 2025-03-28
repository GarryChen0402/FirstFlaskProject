# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class TbDepart(db.Model):
    __tablename__ = 'tb_depart'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)



class TbUser(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer)
    depart_id = db.Column(db.ForeignKey('tb_depart.id'))

    depart = db.relationship('TbDepart', primaryjoin='TbUser.depart_id == TbDepart.id', backref='tb_users')
