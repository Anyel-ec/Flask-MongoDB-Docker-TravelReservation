from flask import render_template, redirect, url_for, jsonify, request
from app.models.Client import Client
from app.services.ClientService import ClientService

class ClientController:
    def __init__(self, environment):
        self.ClientService = ClientService(environment)


    def crear_cliente(self):
        if request.method == 'POST':
            nombres = request.form['nombres']
            cedula = request.form['cedula']
            correo = request.form['correo']
            direccion = request.form['direccion']
            provincia_id = request.form['provincia_id']
            genero_id = request.form['genero_id']
            eliminado = request.form['eliminado']
            if nombres and cedula and correo and direccion and provincia_id and genero_id and eliminado:
                self.ClientService.agregar_usuario(nombres, cedula, correo, direccion, provincia_id, genero_id, eliminado)
                return redirect(url_for('listar_clientes'))
            else:
                return jsonify({"error": "Se requieren todos los campos"}), 400
        return render_template('Client/crear_cliente.html')
    
    def ver_cliente(self, cedula):
        cliente = self.ClientService.obtener_cliente_por_cedula(cedula)
        if cliente:
            return render_template('Client/ver_cliente.html', cliente=cliente)
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
        
    def editar_cliente(self, cedula):
        if request.method == 'POST':
            nuevo_nombres = request.form['nombres']
            nuevo_correo = request.form['correo']
            nueva_direccion = request.form['direccion']
            nueva_provincia_id = request.form['provincia_id']
            nuevo_genero_id = request.form['genero_id']
            nuevo_eliminado = request.form['eliminado']
            if nuevo_nombres or nuevo_correo or nueva_direccion or nueva_provincia_id or nuevo_genero_id or nuevo_eliminado:
                if self.ClientService.actualizar_cliente(cedula, nuevo_nombres, nuevo_correo, nueva_direccion, nueva_provincia_id, nuevo_genero_id, nuevo_eliminado):
                    return redirect(url_for('listar_clientes'))
                else:
                    return jsonify({"error": "Cliente no encontrado"}), 404
            else:
                return jsonify({"error": "Se requiere al menos un campo para actualizar"}), 400
        cliente = self.ClientService.obtener_cliente_por_cedula(cedula)
        if cliente:
            return render_template('Client/actualizar_cliente.html', cliente=cliente)
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
        
    def eliminar_cliente(self, cedula):
        if self.ClientService.eliminar_cliente(cedula):
            return redirect(url_for('listar_clientes'))
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
        
    def listar_clientes(self):
        clientes = self.ClientService.obtener_todos_los_clientes()
        return render_template('Client/index.html', clientes=clientes)
    
    
    