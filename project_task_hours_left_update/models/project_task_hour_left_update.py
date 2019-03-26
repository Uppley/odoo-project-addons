# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectTaskHourLeftUpdate(models.Model):

    # project.task.type is already used to designate a workflow stage for a task.
    _name = 'project.task.hour.left.update'
    _description = 'Project Task Hour Left Update'

    left_to_do = fields.Float(required=True)
    task_id = fields.Many2one('project.task', 'Task', required=True)
    note = fields.Text()
