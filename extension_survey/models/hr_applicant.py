from odoo import api, fields, models


class Applicant(models.Model):
    _inherit = "hr.applicant"

    survey_id = fields.Many2one('survey.survey', related='job_id.survey_id', string="Survey", readonly=False)
    # add extra field to save a survey which has already been initiated
    filled_survey_id = fields.Many2one('survey.survey', string="Survey Started", readonly=False)
    response_id = fields.Many2one('survey.user_input', "Response", ondelete="set null", oldname="response")

# TP 18-9-2019: Add function to add 

    @api.multi
    def action_start_survey(self):
        self.ensure_one()
        # create a response and link it to this applicant
        if not self.response_id:
            response = self.env['survey.user_input'].create({'survey_id': self.survey_id.id, 'partner_id': self.partner_id.id})
            self.response_id = response.id
            # TP 18-9-2019: Add function to save the currect survey version. If opened later use this version, not the latest one
            self.filled_survey_id = survey_id
        else:
            response = self.response_id
        # grab the token of the response and start surveying
            # TP 18-9-2019: Changed to open an existing response with the saved survey_id (correct version)
        return self.filled_survey_id.with_context(survey_token=response.token).action_start_survey()
#        return self.survey_id.with_context(survey_token=response.token).action_start_survey()

    @api.multi
    def action_print_survey(self):
        """ If response is available then print this response otherwise print survey form (print template of the survey) """
        self.ensure_one()
        if not self.response_id:
            return self.survey_id.action_print_survey()
        else:
            response = self.response_id
            # TP 18-9-2019: Changed to open an existing response with the saved survey_id (correct version)
            return self.filled_survey_id.with_context(survey_token=response.token).action_print_survey()
#           return self.survey_id.with_context(survey_token=response.token).action_print_survey()
