# -*- coding: utf-8 -*-

from odoo import models, fields
class InheritProductTemplate(models.Model):
    _inherit = 'product.template' 

    color_category = fields.Char(string='Categoría de color')
    art = fields.Char(string='Arte')
    image = fields.Binary(string='Imagen')
    properties = fields.Text(string='Propiedades del papel tapiz')
    carrier_material = fields.Char(string='Medida Rollo')
    upper_material = fields.Char(string='Material Superior')
    pattern_offset = fields.Char(string='Material Portador')
    roll_measure = fields.Char(string='Desplazamiento de patrón')
    feature_ids = fields.Many2many(comodel_name='product.feature', string='Caracteristicas de producto')
    



