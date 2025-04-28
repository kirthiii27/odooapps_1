{
    'name': "XML File Generator for Tax Office",
    'description': """
        This module allows users to generate XML files for Sales Invoices and send them as attachments directly from Odoo.

        Key Features:
        - Generate XML version of sales invoice data
        - Include customer details, invoice lines, tax information
        - Generating XML files and sending them, probably to the Tax Office (for example SAF-T, Angola, Portugal, etc.).
       
    """,
    'summary': """ Generate XML file from Invoices/Sales and send it to Tax Office.""",
    'sequence': 1,
    'author': 'Alan Technologies',
    'company': 'Alan Technologies',
    'maintainer': 'Alan Technologies',
    'website': "https://alantechnologies.in/",
    "license": "AGPL-3",
    'category': 'account',
    'version': '18.0.1.0.0',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'wizard/xml_file.xml',
        'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,

}
