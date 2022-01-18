from odoo import fields, models, api, _


class TasksInherit(models.Model):
    _inherit = 'project.task'

    seq = fields.Char(required=True,
                      copy=False,
                      readonly=True,
                      index=True,
                      default=lambda self: _('New'))
    ont_sn = fields.Char(string="ONT-SN")
    hag_sn = fields.Char(string="HAG-SN")
    phone = fields.Char(string="Phone")
    location = fields.Char(string="Location")

    @api.model
    def create(self, values):
        if values.get('seq', _('New') == _('New')):
            values['seq'] = self.env['ir.sequence'].next_by_code('task.sequence') or _('New')
        result = super(TasksInherit, self).create(values)
        return result

