from odoo import models,fields,api

class Appointment(models.Model):
    _name = "appointment"
    _description = "Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    patient_id = fields.Many2one(string='Patient', comodel_name='patient')
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help='Reference of the patient from the patient record.')
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='State', required=True, default='draft')
    doctor_id = fields.Many2one('res.users', string="Doctor")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button Click !!!!!!!")
        return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Click Successful!',
                    'type': 'rainbow_man',
                }
            }
    
    