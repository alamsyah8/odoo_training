# -*- coding: utf-8 -*-
{
    "name": "Sanbe Farma Module Training",
    "summary": "Training",
    "description": """
Training
========
Pelatihan technical Odoo 17 PT Sanbe Farma.
    """,
    "author": "Mukti Alamsyah, PT Sanbe Farma, PT Arkana Solusi Digital",
    "website": "https://www.sanbe-farma.com",
    "category": "Other",
    "version": "17.0.1.0.0",
    "license": "OPL-1",
    "depends": ["base", "mail", "hr"],
    "data": [
        'security/planning_slot_role.xml',
        "security/ir.model.access.csv",
        "data/hr_employee_data.xml",
        "views/planning_role_view.xml",
        'views/planning_slot_view.xml',
        'views/planning_menu_view.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    "autoinstall": False,
    "installable": True,
    "application": True,
    "external_dependencies": {"python": []},
}
