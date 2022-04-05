# from flask import Flask
# from flask_restful import Api, Resource ,abort, reqparse
# from flask_sqlalchemy import SQLAlchemy
#
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel.db'
# db = SQLAlchemy(app)
# api = Api(app)
#
# class DeviceRecord(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     odometer = db.Column(db.Float, nullable=False)
#     fuelQuantity = db.Column(db.Float, nullable=False)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'odometer': self.odometer,
#             'fuelQuantity': self.fuelQuantity
#         }
