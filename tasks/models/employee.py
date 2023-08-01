from odoo import models, fields, api


class Employee(models.Model):
    _name = 'tasks.employee'
    _description = 'tasks.employee'

    name = fields.Char(string="Employee Name",required=True)
    department = fields.Char(string="Department",required=True)
    email = fields.Char(string="Email",required=True)
    tasks_ids = fields.One2many("tasks.task","assignto_id",string="Tasks Assigned")
    # taask_ids = fields.One2many("tasks.task",'assignto_id',string="Assigned")

#     tassk_count = fields.Integer(string='Task Count',compute = 'compute_tassk_count')
    task = fields.Integer(string="Count Task",compute='_compoute_task')



    def _compoute_task(self):
        for rec in self:
            task = self.env['tasks.employee'].search_count([('tasks_ids', '=', rec.id)])
            rec.task = task

# def compute_tassk_count (self):
#     for rec in self:
#         task_count = self.env['tasks.employee'].search_count([('tasks_id', '=',rec.id )])
#         rec.task_count = task_count
