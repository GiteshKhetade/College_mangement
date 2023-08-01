from odoo import models, fields, api


class Comment(models.Model):
    _name = 'tasks.comment'
    _description = 'tasks.comment'

    task_ids = fields.Many2one('tasks.task', string="Tasks")
    employ_ids = fields.Many2one('tasks.employee',string="Employees")
    comment = fields.Text(string="Comment")
    comment_date = fields.Datetime(string="Comment Date")

