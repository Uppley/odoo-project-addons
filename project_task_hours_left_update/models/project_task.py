# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class ProjectTaskWithHourLeft(models.Model):
    """Add the relation to hour left"""

    _inherit = 'project.task'

    @api.depends('planned_hours', 'hour_left_update_ids')
    def compute_latest_hour_left(self):
        for task in self:
            latest_update = self.env['project.task.hour.left.update'].search(
                [('task_id', '=', task.id)],
                order='create_date',
                limit=1)

            task.hour_left = latest_update and latest_update.left_to_do or task.planned_hours

    hour_left = fields.Float(compute='compute_latest_hour_left')
    hour_left_update_ids = fields.One2many('project.task.hour.left.update', 'id', 'Hour Left Updates')
    hour_left_update_count = fields.Integer('Hour Left Update Count', compute='_compute_hour_left_update_count')

    def _compute_hour_left_update_count(self):
        for task in self:
            task.hour_left_update_count = len(
               self.env['project.task.hour.left.update'].search([('task_id', '=', task.id)])
            )
