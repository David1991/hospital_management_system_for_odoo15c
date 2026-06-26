import datetime
from odoo import api, models, fields

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    # Cancellation Date is get default
    @api.model
    def default_get(self, fields):
        result = super(CancelAppointmentWizard, self).default_get(fields)
        result['date_cancel'] = datetime.date.today()
        return result

    appointment_id = fields.Many2one("appointment", string = "Appointment")
    reason = fields.Text(string = "Reason")
    date_cancel = fields.Date(string = "Cancellation Date")
    
    def action_cancel(self):
        return