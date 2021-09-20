#from flask import Flask, request, jsonify
from flask import Flask,request,jsonify
from flask_cors import CORS
from nosql import *

#crea una instancia de la clase Flask
servidor = Flask(__name__)
CORS(servidor)

#---[Prueba]--------------------------
@servidor.route("/prueba")
def prueba():
    return "Ok, exito en el servidor"

#---[GET] : consultar ----------------
@servidor.route("/mas_recientes", methods=['GET'])
def consultaProductos():
    #datos = {'respuesta': 'Por implementar'}
    nosql = NOSQL()
    datos = nosql.consultar('productos')

    return jsonify({'message': 'Proceso con exito',
                   'object': 'list to dictionary',
                   'data': datos}),200

#---[POST] : adicionar ---------------
@servidor.route("/mas_recientes", methods=['POST'])
def adicionarProductos():
    datos = request.json

    nosql = NOSQL()
    nosql.insert('productos', datos['codigo'], datos)

    #print(datos)
    return jsonify({'message': 'Proceso con exito',
                   'object': 'text',
                   'data': 'Ok'}),200

#---[Update] : Actualziar
@servidor.route("/mas_recientes", methods=['PUT'])
def actualizarProductos():
    nosql = NOSQL()
    datos = request.json
    nosql.update('productos',datos['codigo'],'precio', datos['precio']) 
     #print(datos)
    return jsonify({'message': 'Proceso con exito',
                   'object': 'text',
                   'data': 'Ok'}),200                  

#-------------------------------------
if __name__ == '__main__':
    servidor.run(debug=True)

