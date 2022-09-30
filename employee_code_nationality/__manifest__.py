# Copyright 2021, Iheb Ltaief <ihebltaief@gmail.com>
# ------- OLYA-TECH Company ------
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Employee Code By Nationality',
    'version': '13.0.1.0.1',
    'license': 'AGPL-3',
    'category': 'Generic Modules/Human Resources',
    'summary': 'Generate automatic Code for employees with nationality code prefix when create or import employees',
    'author': 'Iheb Ltaief',
    'support': 'ihebltaief@gmail.com',
    'price': '5',
    'currency:': 'USD',
    'images': ['static/description/icon.png'],
    'depends': [
        'hr'
    ],
    'data': [
        'data/hr_employee_sequence.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
}
