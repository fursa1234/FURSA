# -*- coding: utf-8 -*-
{
    'name': "Custom Approvals Request",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        
    """,

    'author': "By Pure IT For Solution",
    'website': "http://www.yourcompany.com",


    'category': 'Approvals',
    'version': '1.0',

    'depends': ['approvals','hr_expense'],

    # always loaded
    'data': [
        'views/custom_approvals.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

