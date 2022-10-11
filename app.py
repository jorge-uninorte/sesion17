from flask import Flask, render_template, request	

app = Flask(__name__)    

@app.route('/')          		
def hola_mundo():        		
        return render_template('index.html',nombres='Escriba su nombre aquí',apellidos='Escriba sus apellidos aquí')

@app.route('/productos/<int:id>', methods=["GET", "POST"])
def mostrar_producto(id):
        if request.method == 'POST':
                return 'solicitud con POST'
        else:
                return 'solicitud con get'
        #return 'Mostrar el artículo con id:{}'.format(id)

@app.route('/hola/')
@app.route('/hola/<string:nombre>')
@app.route('/hola/<string:nombre>/<int:edad>')
def hola(nombre=None,edad=None):
        if nombre and edad:
                return 'Hola, {0} tienes {1} años.'.format(nombre,edad)
        elif nombre:
                return 'Hola, {0}'.format(nombre)
        else:
                return 'Hola mundo'

@app.route('/hello/world')
def hello_world():
        return '<h1>Hola mundo</h1>'
