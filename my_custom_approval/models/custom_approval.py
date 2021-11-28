from odoo import _, api, fields, models


class Approvals(models.Model):
    _inherit = 'approval.request'

    request_status = fields.Selection(selection_add=[('expenses', 'Expenses'),('can','Cancel')])

    # def action_expenses(self):
    #     for rec in self:
    #         rec.request_status = 'expenses'
    #         rec.create_expenses()


    def create_expenses(self):
        exp_obj = self.env['hr.expense'].search([])
        vals = {
            'name': self.name,
            'product_id': 1,
            'partner_id': self.partner_id.id,
            'unit_amount': self.amount,
            'state': 'draft'
        }
        expenses_id = exp_obj.create(vals)
        return expenses_id



    
class HrExpense(models.Model):
    _inherit = 'hr.expense'

    partner_id = fields.Many2one('res.partner', string="Partner")





