#-*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
from odoo.exceptions import ValidationError

class modulo_clase(models.Model):
    _name = 'modulo.clase'
    _description = 'clase'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Tipo de aula")
    fecha = fields.Date(string="Fecha")
    hora_inicio = fields.Datetime(string="Hora de inicio")
    hora_fin = fields.Datetime(string="Hora de fin")
    profesor_id = fields.Many2one(
        comodel_name='modulo.profesor', 
        string="Profesor", 
        ondelete='restrict')
    alumno_ids = fields.Many2many(
        comodel_name='res.partner', 
        string="Alumnos", 
        ondelete='restrict')
    
    #la hora de inicio debe ser menor que la hora de fin
    @api.constrains('hora_inicio', 'hora_fin')
    def _check_hora(self):
        for record in self:
            if record.hora_inicio > record.hora_fin:
                raise models.ValidationError("La hora de inicio debe ser menor que la hora de fin")

class modulo_profesor(models.Model):
    _name = 'modulo.profesor'
    _description = 'Profesor'

    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    email = fields.Char(string="Email")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    clases_ids = fields.One2many(
        comodel_name='modulo.clase', 
        inverse_name='profesor_id', 
        string="Clases", 
        ondelete='restrict')
    
    #el email debe ser unico:
    _sql_constraints = [
        ('email_unique',
        'UNIQUE(email)',
        "El email debe ser único"),
    ]


class modulo_alumno(models.Model):
    _name = 'modulo.alumno'
    _description = 'alumno'
    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    email = fields.Char(string="Email")
    photo = fields.Image(max_width=100, max_height=100)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    nivel_estudios  = fields.Selection(
        [(1, 'Primaria'), (2, 'ESO'), (3, 'Bachillerato')], string="Curso")
    clases_ids = fields.Many2many(
        comodel_name='modulo.clase', 
        string="Clases", 
        ondelete='restrict')
    
    _sql_constraints = [
        ('email_unique',
        'UNIQUE(email)',
        "El email debe ser único"),
    ]