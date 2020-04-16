# -*- coding: utf-8 -*-
{
    'name': "WooCommerce Connector",
    'summary': """Short (1 phrase/line) summary of the module's purpose, used as""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Saad Mujeeb - ISAA TECH",
    'website': "https://www.isaatech.com",
    'category': 'Connectors',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/views.xml',
        'views/orders.xml',
        'views/products.xml',
        'views/customers.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
