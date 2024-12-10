from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import PacienteForm, MedicoForm, CitaForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citas_medicas.db'
app.config['SECRET_KEY'] = 'mi_clave_secreta'
db = SQLAlchemy(app)

# Modelos
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10), nullable=False)  # Almacenar como cadena
    hora = db.Column(db.String(5), nullable=False)    # Almacenar como cadena
    estado = db.Column(db.String(20), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pacientes', methods=['GET', 'POST'])
def pacientes():
    form = PacienteForm()
    if form.validate_on_submit():
        nuevo_paciente = Paciente(nombre=form.nombre.data, apellido=form.apellido.data,
                                   telefono=form.telefono.data, email=form.email.data,
                                   contraseña=form.contraseña.data)
        db.session.add(nuevo_paciente)
        db.session.commit()
        return redirect(url_for('pacientes'))
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', form=form, pacientes=pacientes)

@app.route('/medicos', methods=['GET', 'POST'])
def medicos():
    form = MedicoForm()
    if form.validate_on_submit():
        nuevo_medico = Medico(nombre=form.nombre.data, especialidad=form.especialidad.data,
                              horario=form.horario.data, email=form.email.data)
        db.session.add(nuevo_medico)
        db.session.commit()
        return redirect(url_for('medicos'))
    medicos = Medico.query.all()
    return render_template('medicos.html', form=form, medicos=medicos)

@app.route('/citas', methods=['GET', 'POST'])
def citas():
    form = CitaForm()
    form.paciente_id.choices = [(p.id, p.nombre) for p in Paciente.query.all()]
    form.medico_id.choices = [(m.id, m.nombre) for m in Medico.query.all()]
    
    if form.validate_on_submit():
        nueva_cita = Cita(fecha=form.fecha.data.strftime('%Y-%m-%d'),  # Convertir fecha a cadena
                          hora=form.hora.data,  # Ya es una cadena
                          estado=form.estado.data, 
                          paciente_id=form.paciente_id.data,
                          medico_id=form.medico_id.data)
        db.session.add(nueva_cita)
        db.session.commit()
        return redirect(url_for('citas'))
    citas = Cita.query.all()
    return render_template('citas.html', form=form, citas=citas)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas dentro del contexto de la aplicación
    app.run(debug=True)