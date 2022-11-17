# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSale(WebsiteSale):

    # Override
    # Add in the rendering the free_shipping_line
    def _get_shop_payment_values(self, order, **kwargs):
        values = super(WebsiteSale, self)._get_shop_payment_values(order, **kwargs)
        values['distributors'] = request.env['res.partner'].search([('is_destributor', '=', True)])
        values['default_distributors'] = request.env['res.partner'].search([('is_destributor', '=', True),('is_default_destributor', '=', True)])
        return values
