from app import db

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