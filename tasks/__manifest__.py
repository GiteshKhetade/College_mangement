# -*- coding: utf-8 -*-
{
    'name': "tasks",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'sequence': "-100",
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/tasks_employee_views.xml',
        'views/tasks_task_views.xml',
        'views/tasks_category_views.xml',
        'views/tasks_project_views.xml',
        'views/tasks_comment_views.xml',
        'views/car_rental_views.xml',
        'views/carrental_templete.xml',
        'views/car_rental_views.xml',
        'views/tasks_menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto-install' : False

    # 'assets':{
    #     'web.assets_frontend': [
    #         'tasks/static/src/css/car_templete.css',
    #     ],
    # },
   
}


