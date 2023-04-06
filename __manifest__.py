# -*- coding: utf-8 -*-


{
    'name': 'POS User',
    'version': '14.0.1.0.0',
    'category': 'Point of Sale',
    'author': 'Abhishek Creation',
    'website': '',
    'license': 'LGPL-3',
    'summary': 'Restrict POS Users to allowed Points of Sale.',
    
    'description': """
The module allows restricting access to Points of Sale for POS users.
    """,
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/pos_user_restrict_security.xml',
        'views/res_users_views.xml',
        'views/pos_menu.xml',
    ],
    'external_dependencies': {
    },
    
    'application': False,
    'installable': True,
    'auto_install': False,
}