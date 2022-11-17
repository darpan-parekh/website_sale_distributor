# -*- coding: utf-8 -*-

import json
from odoo import api, fields, models
from odoo.addons.website.models import ir_http
from odoo import http
from odoo.http import request


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    destributor_id = fields.Many2one('res.partner',string="Destributor")

    def update_sales_destributor(self, dist_id = False):
        req_order_id =  request.session.get('sale_order_id')
        order_id = self.browse(req_order_id)
        if not order_id:
            website = ir_http.get_request_website()        
            if not website:
                if self.env.context.get('website_id'):
                    website = self.env['website'].browse(self.env.context['website_id'])
                else:
                    # In the weird case we are coming from the backend (https://github.com/odoo/odoo/issues/20245)
                    website = len(self) == 1 and self or self.env['website'].search([], limit=1)        
            order_id = website.sale_get_order()
        order_id.write({
            'destributor_id': dist_id
        })

class WabsitePage(models.AbstractModel):
    _inherit = 'website'
    
    def sale_get_order(self, force_create=False, code=None, update_pricelist=False, force_pricelist=False):
        request.website = self
        so = super().sale_get_order(force_create=force_create, code=code, update_pricelist=update_pricelist, force_pricelist=force_pricelist)
        return so