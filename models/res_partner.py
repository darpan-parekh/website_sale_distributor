# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_destributor = fields.Boolean(string='Destributor')
    is_default_destributor = fields.Boolean(string="Default Destributor")

    @api.onchange('is_default_destributor')
    def onchange_is_default_destributor(self):
        self.is_destributor = False
        if self.is_default_destributor:
            self.is_destributor = self.is_default_destributor

    @api.constrains('is_destributor','is_default_destributor')
    def _check_default_destributor(self):
        default_dist_counts = len(self.env['res.partner'].search([('is_default_destributor', '=', True)]).ids)
        if default_dist_counts > 1:
            raise ValidationError(_('Only one destributor will be default destributor. !!!'))
