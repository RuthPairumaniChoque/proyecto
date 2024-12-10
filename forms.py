from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, PasswordField
from wtforms.validators import DataRequired

class PacienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Agregar Paciente')

class MedicoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    especialidad = StringField('Especialidad', validators=[DataRequired()])
    horario = StringField('Horario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Agregar Médico')

class CitaForm(FlaskForm):
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    hora = StringField('Hora', validators=[DataRequired()])  # Cambiar a StringField
    estado = StringField('Estado', validators=[DataRequired()])
    paciente_id = SelectField('Paciente', coerce=int, validators=[DataRequired()])
    medico_id = SelectField('Médico', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Agregar Cita')