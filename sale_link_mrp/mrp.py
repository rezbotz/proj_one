from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class MrpProduction_Linked(models.Model):
    _inherit = 'mrp.production'

    partner_id = fields.Many2one('res.partner', string='Customer', copy=False)
    sale_id = fields.Many2one('sale.order', string='Related Sales', copy=False)

    # @api.onchange('origin')
    # def _get_customer(self):
    #     import re
    #     for record in self:
    #         # import ipdb; ipdb.set_trace()
    #         origin = self.origin
    #         if origin:
    #             sres = re.findall(r"((?:SO\d{3}))", origin)
    #             if len(sres) > 0:
    #                 so_ids = self.env['sale.order'].search([['name', '=', sres[0]]])
    #                 if len(so_ids) > 0 :
    #                     # record.sale_id = so_ids.id
    #                     # import ipdb; ipdb.set_trace()
    #                     record.partner_id = so_ids[0].partner_id.id
    #                     so_ids[0].renotes()
    #                     return
    #
    #     # record.sale_id = ""
    #     return
    #
    #
    # @api.multi
    # def write(self, vals):
    #     res = super(MrpProduction_Linked, self).write(vals)
    #     # self._get_customer()
    #     import ipdb; ipdb.set_trace()
    #     return res

    @api.model
    def create(self, vals):
        origin = vals['origin']
        import re
        if origin:
            sres = re.findall(r"((?:SO\d{3}))", origin)
            if len(sres) > 0:
                so_ids = self.env['sale.order'].search([['name', '=', sres[0]]])
                if len(so_ids) > 0 :
                    vals['partner_id']= so_ids[0].partner_id.id
                    vals['sale_id']= so_ids[0].id
                    res = super(MrpProduction_Linked, self).create(vals)
                    so_ids[0].renotes(res.id)

            else:
                res = super(MrpProduction_Linked, self).create(vals)

        return res
