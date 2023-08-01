from odoo import models, fields

class Carrental(models.Model):
    _name = 'tasks.carrental'
    _description = 'Tasks_Car_Rental'

    name = fields.Char(string='Car Name', required=True)
    price = fields.Float(string='Price')
    # image = fields.Binary(string='Car Image')
    description = fields.Text(string='Description')