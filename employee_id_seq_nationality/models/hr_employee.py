# Copyright 2021, Iheb Ltaief <ihebltaief@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from odoo import api, fields, models, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    """Implement company wide unique identification number."""

    _inherit = 'hr.employee'

    identification_id = fields.Char(
        string='Identification No',
        copy=False
    )

    _sql_constraints = [
        ('identification_id_uniq', 'unique(identification_id)',
         'The Employee Number must be unique across the company(s).'),
    ]

    @api.model
    def create(self, vals):
        if not vals.get('identification_id'):
            if not vals.get('country_id', False):
                raise Warning(_('You must select Nationality for this employee'))
            else:
                country_id = self.env['res.country'].browse(vals['country_id'])
                if not country_id.code:
                    raise Warning(_('You must set code for this country'))
                else:
                    vals['identification_id'] = '%s%s' % (self.env['res.country'].browse(vals['country_id']).code,
                                         self.env['ir.sequence'].next_by_code('hr.employee.id'))
        return super(HrEmployee, self).create(vals)
