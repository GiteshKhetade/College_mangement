from odoo import models, fields, api


class Task(models.Model):
    _name = 'tasks.task'
    _description = 'tasks.task'

    name = fields.Char(string="Name of Task",required=True)
    description = fields.Text(string="Description",required=True)
    deadline = fields.Datetime(string="Date")
    assignto_id = fields.Many2one('tasks.employee',string='Assigned to',required=True)
    categories_ids = fields.Many2many('tasks.category',string="Categories")