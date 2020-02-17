# Copyright 2013-2020 Open2Bizz <info@open2bizz.nl>
# License LGPL-3

from odoo import api, fields, models, _

fields_to_log = [
'additional_note',
'address_home_id',
'address_id',
'bank_account_id',
'birthday',
'category_ids',
'certificate',
'child_ids',
'children',
'coach_id',
'color',
'contract_ids',
'country_id',
'country_of_birth',
'department_id',
'emergency_contact',
'emergency_phone',
'gender',
'identification_id',
'image',
'job_id',
'job_title',
'km_home_work',
'marital',
'medic_exam',
'mobile_phone',
'name',
'notes',
'parent_id',
'passport_id',
'permit_no',
'place_of_birth',
'sinid',
'spouse_birthdate',
'spouse_complete_name',
'ssnid',
'study_field',
'study_school',
'timesheet_cost',
'timesheet_manager_id',
'timesheet_validated',
'tz',
'user_id',
'vehicle',
'visa_expire',
'visa_no',
'website_message_ids',
'work_email',
'work_location',
'work_phone',
'trainer_id',
'subtrainer_ids',
'percentage_pt_revenue',
'percentage_coaching_revenue',
'percentage_pt_revenue_subtrainer',
'percentage_coaching_revenue_subtrainer'
]

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    trainer_id = fields.Many2one('hr.employee', string="Trainer")
    subtrainer_ids = fields.One2many('hr.employee', 'trainer_id', string="Subtrainers")
    percentage_pt_revenue = fields.Float('Percentage PT omzet (%)')
    percentage_coaching_revenue = fields.Float('Percentage Coaching omzet (%)')
    percentage_pt_revenue_subtrainer = fields.Float('Percentage PT omzet subtrainer (%)')
    percentage_coaching_revenue_subtrainer = fields.Float('Percentage Coaching omzet subtrainer (%)')

    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        all_changes = ""
        for field in fields_to_log:
            if field in vals:
                text_to_add = """<li><span style="font-weight:bold;">%s</span> --> %s</li>""" % (self._get_field_label(field), vals.get(field))
                all_changes += text_to_add
                no_changes = False
        changelog = _("""
        <p>The following fields have been changed:
        <ul>%s</ul>
        </p>

        """) % (all_changes)
        if no_changes == False:
            self.message_post(body=_("%s") %(changelog))
        return res

    def _get_field_label(self, field):
        field_record = self.env['ir.model.fields'].search([('model_id','=','hr.employee'),('name','=',field)])
        return field_record.field_description
