#-*- coding: utf-8 -*-

from odoo import models, fields, api

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

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
 