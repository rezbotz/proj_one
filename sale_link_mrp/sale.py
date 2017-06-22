from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class SaleOrder_linked(models.Model):
    _inherit = 'sale.order'

    # mrp_id = fields.Many2one('mrp.production', string='Source', copy=False)
    mrp_id = fields.One2many('mrp.production', 'sale_id', 'Related MO')
    mrp_text = fields.Char('Related MO')

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
            for mo in partner.mrp_id:
                # text+=mo.name
                mrp_array.append(mo.name)
            partner.mrp_text = ", ".join(mrp_array)
