import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('servicio-cc4c8-4a892d9c264b.json')
app = firebase_admin.initialize_app(cred)

class NOSQL:
    def __init__(self):
        self.db = firestore.client()

    def insert(self, coleccion, documento, datos):
        self.db.collection(coleccion).document(documento).set(datos)
        return 'OK'

    def consultar(self, coleccion):
        resultado = self.db.collection(coleccion).stream()
        registros = []
        registros = [item.to_dict() for item in resultado]
        return registros

    def update(self, coleccion,documento,datos,valor):
        self.datos = datos
        datoActualizado = self.db.collection(coleccion).document(documento)
        datoActualizado.update({self.datos:valor})
