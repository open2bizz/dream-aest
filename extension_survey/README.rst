.. image:: hhttps://www.open2bizz.tech/web/image/res.company/1/logo?
   :target: https://www.gnu.org/graphics/heckert_gnu.transp.small.png
   :alt: License: LGPL-3

===============
extension_survey
===============

This module extends the functions when using a survey on an Applicant 

Normal
======
When setting a survey on a job, Odoo wil always use this survey
Problem
=======
When a survey is already started, and we would like to change the survey, due to a new version, Odoo will ignore the already filled survey. 
Solution
========

When starting a survey on an Applicant the survey is now saved on the applicant This way when already started, it will always use this survey
          
Notes -  IMPORTANT 
==================
When migrating you will need a migration script

Create a server action and run it on hr.applicant:

for record in records:
  if record.response_id:
    current_survey = record.job_id.survey_id.id
    record.write({'filled_survey_id': current_survey})


Credits
=======

Contributors
------------
* `Open2Bizz <https://www.open2bizz.tech>`__

Maintainers
-----------
* `Open2Bizz <https://www.open2bizz.tech>`__

