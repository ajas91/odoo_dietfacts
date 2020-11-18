# -*- coding: utf-8 -*-
{
    'name': "dietfacts",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Add Product Diet Fact Field to the Product Template
    """,

    'author': "Ali Sultan, aJaS-Tech",
    'website': "http://www.ajas-tech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Food',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
	'views/dietfact_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
