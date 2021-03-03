# Copyright 2021, Iheb Ltaief <ihebltaief@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from odoo import api, fields, models, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    """Implement company wide unique code."""

    _inherit = 'hr.employee'

    code = fields.Char(
        string='Code',
        copy=False
    )

    _sql_constraints = [
        ('code_uniq', 'unique(code)',
         'The Employee Code must be unique across the company(s).'),
    ]

    @api.model
    def create(self, vals):
        if not vals.get('country_id', False):
            raise Warning(_('You must select Nationality for this employee'))
        else:
            country_id = self.env['res.country'].browse(vals['country_id'])
            if not country_id.code:
                raise Warning(_('You must set code for this country'))
            else:
                vals['code'] = '%s%s' % (self.env['res.country'].browse(vals['country_id']).code,
                                     self.env['ir.sequence'].next_by_code('hr.employee.code'))
        return super(HrEmployee, self).create(vals)
