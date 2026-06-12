# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    sinid = fields.Char(
        "SIN No",
        help="Social Insurance Number",
        groups="hr.group_hr_user",
        tracking=True,
    )
