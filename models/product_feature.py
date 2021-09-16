# -*- coding: utf-8 -*-
from odoo import api, models, fields
from odoo.tools.translate import _
from odoo.exceptions import UserError

import logging

class ProductFeatures(models.Model):
    _name = 'product.feature'
    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    image = fields.Binary(string='Imagen')
    
