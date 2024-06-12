class Client:

    #Constructor
    def __init__(self, nombres, cedula, correo, direccion, provincia_id, genero_id, eliminado):
        self.nombres = nombres
        self.cedula = cedula
        self.correo = correo
        self.direccion = direccion
        self.provincia_id = provincia_id
        self.genero_id = genero_id
        self.eliminado = eliminado


    def to_dict(self):
        return {
            'nombres': self.nombres,
            'cedula': self.cedula,
            'correo': self.correo, 
            'direccion': self.direccion,
            'provincia_id': self.provincia_id,
            'genero_id': self.genero_id,
            'eliminado': self.eliminado
        }