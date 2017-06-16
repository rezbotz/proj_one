from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class SaleOrder_linked(models.Model):
    _inherit = 'sale.order'

    mrp_id = fields.Many2one('mrp.production', string='Source', copy=False)

    @api.multi
    def renotes(self, mrp_id):
        # import ipdb; ipdb.set_trace()
        if mrp_id:
            self.write({'mrp_id': mrp_id})
        return
