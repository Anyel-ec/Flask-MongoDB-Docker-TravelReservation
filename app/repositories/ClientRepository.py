import pymongo

from app.models.Client import Client

class ClientRepository:
    def __init__(self, environment):
        self.environment = environment # .env 
        self.cliente = pymongo.MongoClient(self.environment.get_database_url()) ## String Conexion
        self.db = self.cliente[self.environment.get_database_name()] ## Nombre de la BD
        self.coleccion = self.db["cliente"] ## Nombre de la coleccion


    #    insertar del cliente
    def insertar_cliente(self, cliente):
        self.coleccion.insert_one(cliente.to_dict())

    def actualizar_cliente(self, cliente, nuevo_nombres=None, nuevo_correo=None, nueva_direccion=None, nueva_provincia_id=None, nuevo_genero_id=None, nuevo_eliminado=None):
        update_data = {}
        if nuevo_nombres:
            update_data['nombres'] = nuevo_nombres
        if nuevo_correo:
            update_data['correo'] = nuevo_correo
        if nueva_direccion:
            update_data['direccion'] = nueva_direccion
        if nueva_provincia_id:
            update_data['provincia_id'] = nueva_provincia_id
        if nuevo_genero_id:
            update_data['genero_id'] = nuevo_genero_id
        if nuevo_eliminado:
            update_data['eliminado'] = nuevo_eliminado

        if update_data:
            self.coleccion.update_one({'cedula': cliente.cedula}, {"$set": update_data})
            return True
        else:
            return False
        
    #    eliminar cliente
    def eliminar_cliente(self, cliente):
        resultado = self.coleccion.delete_one({'cedula': cliente.cedula})
        return resultado.deleted_count > 0
    
    #    obtener todos los clientes
    def obtener_todos_los_clientes(self):
        clientes = []
        for cliente_data in self.coleccion.find():
            clientes.append(Client(cliente_data['nombres'], cliente_data['cedula'], cliente_data['correo'], cliente_data['direccion'], cliente_data['provincia_id'], cliente_data['genero_id'], cliente_data['eliminado']))
        return clientes
    
    #    obtener cliente por cedula
    def obtener_cliente_por_cedula(self, cedula):
        cliente_data = self.coleccion.find_one({'cedula': cedula})
        if cliente_data:
            return Client(cliente_data['nombres'], cliente_data['cedula'], cliente_data['correo'], cliente_data['direccion'], cliente_data['provincia_id'], cliente_data['genero_id'], cliente_data['eliminado'])
        return None


    