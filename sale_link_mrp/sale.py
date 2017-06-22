from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class SaleOrder_linked(models.Model):
    _inherit = 'sale.order'

    # mrp_id = fields.Many2one('mrp.production', string='Source', copy=False)
    mrp_id = fields.One2many('mrp.production', 'sale_id', 'Related MO')
    mrp_text2 = fields.Text('Related MO2')
    mrp_text = fields.Text('Related MO')

    @api.multi
    def renotes(self, mrp_id):
        if mrp_id:
            self.write({'mrp_id': [
                (   4,
                    mrp_id
                )
                ]})

        return
    mrp_text = fields.Char(compute='_related_mo', string="Related MO")
    @api.multi
    def _related_mo(self):
        for partner in self:
            mrp_array=[]
            if len(partner.mrp_id):
                for mo in partner.mrp_id:
                    # text+=mo.name
                    mrp_array.append(mo.name)
                    partner.mrp_text = ", ".join(mrp_array)
            else:
                    partner.mrp_text = "false"


    @api.multi
    def search_mrp(self):
        # return {
        #     'name': _('Cash Control'),
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'mrp.production',
        #     'view_id': self.env.ref('account.view_account_bnk_stmt_cashbox').id,
        #     'type': 'ir.actions.act_window',
        #     'res_id': self.env.context.get('cashbox_id'),
        #     'context': context,
        #     'target': 'new'
        # }
        #
        result = {
            "type": "ir.actions.act_window",
            "res_model": "mrp.production",
            "views": [[False, "tree"], [False, "form"]],
            "domain": [["id", "in", self.mrp_id.ids]],
            "context": {"create": False},
            "name": "Related MO",
        }

        return result
