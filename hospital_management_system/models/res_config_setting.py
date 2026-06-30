from odoo import fields, models

class ResConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"

    cancel_day = fields.Integer(string = "Cancel Day")