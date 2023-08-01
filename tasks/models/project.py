from odoo import models, fields, api


class Project(models.Model):
    _name = 'tasks.project'
    _description = 'tasks.project'

    name = fields.Char(string="Project Name",required=True)
    description = fields.Text(string="Project Desc",required=True)
    emplooyees_ids = fields.Many2many('tasks.employee',string="Employes")
    task_count = fields.Integer(string="Count Task",compute='_compoute_task_count')

    def _compoute_task_count(self):
        for rec in self:
            task_count = self.env['tasks.task'].search_count([('assignto_id', '=', rec.id)])
            rec.task_count = task_count