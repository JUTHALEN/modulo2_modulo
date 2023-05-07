#-*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
from odoo.exceptions import ValidationError

class modulo2_provincia(models.Model):
    _name = 'modulo2.provincia'
    _description = 'Modelo de provincias'

    name = fields.Char(string="Nombre de provincia")
    description = fields.Text(string="Descripción")


class modulo2_direccion(models.Model):
    _name = 'modulo2.direccion'
    _description = 'Modelo de dirección'

    name = fields.Char(string="Dirección")
    provincia_id = fields.Many2one(
        comodel_name='modulo2.provincia', 
        string="Provincia", 
        ondelete='restrict')

class modulo2_modelo(models.Model):
    _name = 'modulo1.modulo'
    _inherit = 'modulo1.modulo'
    _description = 'Modelo extendido'
    name = fields.Char(string="Dirección")
    description = fields.Text(string="Descripción", default="Descripción por defecto")
    description2 = fields.Html(string="Descripción HTML")

    #Esto lo que hace es que cuando el nombre se cambie genere una contraseña nueva
    #Hay que definir la funcion que quiero llamar antes de llamarla
    # @api.depends('name') 
    # def _compute_password(self):
    #     for record in self:
    #         record.password = secrets.token_urlsafe(8)

    #Entonces es mejor crearla así para que tengo sentido:
    # def _compute_password():
    #     return secrets.token_urlsafe(8)

    password = fields.Char(string="Contraseña", default=lambda s: secrets.token_urlsafe(8))
    last_login = fields.Datetime(string="Último login", default=fields.Datetime.now, required = True)
    enrollment_date = fields.Date(string="Fecha de alta", default=fields.Date.today)
    is_boolean = fields.Boolean(string="Es Booleano")
    photo = fields.Image(max_width=100, max_height=100)
    choice = fields.Selection(
        string="Opciones",
        selection=[('1', 'Opción 1'), ('2', 'Opción 2'), ('3', 'Opción 3')])

    dni = fields.Char(string="DNI", size=9)
    @api.constrains('value')
    def _check_edad(self):
        for record in self:
            if record.value < 18:
                raise models.ValidationError("Debe ser mayor de edad")
    
    _sql_constraints = [
        ('dni_unique',
        'UNIQUE(dni)',
        "El DNI debe ser único"),
    ]
    
    
    


#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
 