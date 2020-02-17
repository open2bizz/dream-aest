# Copyright 2013-2020 Open2Bizz <info@open2bizz.nl>
# License LGPL-3

{
    'name': 'Human Resource Changelog',
    'summary': 'Add logging to employee record when certain fields are changed.',
    'version': '12.0.1.0.0',
    'category': 'Catergorie',
    'website': 'https://www.open2bizz.nl/',
    'author': 'Open2Bizz',
    'license': 'LGPL-3',
    'installable': True,
    'depends': [
        'hr',
    ],
    'data': [
        'views/hr_employee.xml',
    ]
}
