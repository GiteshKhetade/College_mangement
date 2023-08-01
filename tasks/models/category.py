from odoo import models, fields, api


class Category(models.Model):
    _name = 'tasks.category'
    _description = 'tasks.category'

    name = fields.Char(string="Enter Category",required=True)
    project_id = fields.Many2one('tasks.project',string="Project Details")