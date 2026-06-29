from odoo import models,fields,api
from datetime import date
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = "patient"
    _description = "Patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    ref = fields.Char(string='Reference', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default='female')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one(string='Appointment', comodel_name='appointment')
    image = fields.Image(string = "Image")
    tag_id = fields.Many2many("patient.tag", string = "Tag")
    appointment_count = fields.Integer(string = "Appointment Count", compute = '_compute_appointment_count', store = True)
    appointment_ids = fields.One2many("appointment", 'patient_id', string = "Appointment")
    parent = fields.Char(string = "Parent")
    material_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string = "Material Status", tracking = True)
    partner_name = fields.Char(string = "Partner Name")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['appointment'].search_count([('patient_id', '=', rec.id)])

    # Checking the condition of Date of Birth
    @api.constrains(date_of_birth)
    def check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError("The entered date of birth is not acceptable!")

    # Reference Value is change sequence number directly save in database
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('patient')
        return super(Patient, self).create(vals)
    
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('patient')
        return super(Patient, self).create(vals)

    # Computing for Age
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    