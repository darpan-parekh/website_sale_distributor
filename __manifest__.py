# -*- coding: utf-8 -*-
{
    'name': 'Website Sales Distributor',
    'author': "Darpan Parekh",
    'version': '14.0.1',
    'summary': 'Website Sales Distributor',
    'sequence': 10,
    'description': """
Website Sales Distributor
==========================
It helps customer to select choice of destributor through website. 
    """,
    'category': 'Website/Website',
    'images': [],
    'depends': ['website_sale', 'sale'],
    'data': [
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
