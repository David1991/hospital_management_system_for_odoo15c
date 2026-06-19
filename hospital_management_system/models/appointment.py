from odoo import models,fields

class Appointment(models.Model):
    _name = "appointment"
    _description = "Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    patient_id = fields.Many2one(string='Patient', comodel_name='patient')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    
    