# Copyright 2013-2020 Open2Bizz <info@open2bizz.nl>
# License LGPL-3

from odoo import api, fields, models, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    trainer_id = fields.Many2one('hr.employee', string="Trainer", track_visibility="onchange")
    subtrainer_ids = fields.Many2many(comodel_name='hr.employee',
                            relation='subtrainers_employee',
                            column1='employee_id',
                            column2='employee_trainer_id',
                            track_visibility="onchange")

    percentage_pt_revenue = fields.Float('Percentage PT omzet (%)')
    percentage_coaching_revenue = fields.Float('Percentage Coaching omzet (%)')
    percentage_pt_revenue_subtrainer = fields.Float('Percentage PT omzet subtrainer (%)')
    percentage_coaching_revenue_subtrainer = fields.Float('Percentage Coaching omzet subtrainer (%)')


# inhertitances

    birthday = fields.Date(track_visibility="onchange")
    spouse_birthdate = fields.Date(track_visibility="onchange")
    notes = fields.Text(track_visibility="onchange")
    additional_note = fields.Text(track_visibility="onchange")
    visa_expire = fields.Text(track_visibility="onchange")
    name = fields.Char(track_visibility="onchange")
    user_id = fields.Many2one(track_visibility="onchange")
    active = fields.Boolean(track_visibility="onchange")
    address_home_id = fields.Many2one(track_visibility="onchange")
    country_id = fields.Many2one(track_visibility="onchange")
    gender = fields.Selection(track_visibility="onchange")
    marital = fields.Selection(track_visibility="onchange")
    spouse_complete_name = fields.Char(track_visibility="onchange")
    spouse_birthdate = fields.Date(track_visibility="onchange")
    children = fields.Integer(track_visibility="onchange")
    place_of_birth = fields.Char(track_visibility="onchange")
    country_of_birth = fields.Many2one(track_visibility="onchange")
    birthday = fields.Date('Date of Birth', groups="hr.group_hr_user")
    ssnid = fields.Char(track_visibility="onchange")
    sinid = fields.Char(track_visibility="onchange")
    identification_id = fields.Char(track_visibility="onchange")
    passport_id = fields.Char(track_visibility="onchange")
    bank_account_id = fields.Many2one(track_visibility="onchange")
    permit_no = fields.Char(track_visibility="onchange")
    visa_no = fields.Char(track_visibility="onchange")
    visa_expire = fields.Date(track_visibility="onchange")
    additional_note = fields.Text(track_visibility="onchange")
    certificate = fields.Selection(track_visibility="onchange")
    study_field = fields.Char(track_visibility="onchange")
    study_school = fields.Char(track_visibility="onchange")
    emergency_contact = fields.Char(track_visibility="onchange")
    emergency_phone = fields.Char(track_visibility="onchange")
    km_home_work = fields.Integer(track_visibility="onchange")
    job_title = fields.Char(track_visibility="onchange")
    address_id = fields.Many2one(track_visibility="onchange")
    work_phone = fields.Char(track_visibility="onchange")
    mobile_phone = fields.Char(track_visibility="onchange")
    work_email = fields.Char(track_visibility="onchange")
    work_location = fields.Char('Work Location')
    job_id = fields.Many2one(track_visibility="onchange")
    department_id = fields.Many2one(track_visibility="onchange")
    parent_id = fields.Many2one(track_visibility="onchange")
    child_ids = fields.One2many(track_visibility="onchange")
    coach_id = fields.Many2one(track_visibility="onchange")
    category_ids = fields.Many2many(track_visibility="onchange")
    notes = fields.Text(track_visibility="onchange")
    color = fields.Integer(track_visibility="onchange")
# end inhertitances
