# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Project Task Hours Left Update',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Allow to review the hours left from a wizard',
    'depends': ['hr_timesheet'],
    'data': [
        'views/ir_ui_menu.xml',
        'views/ir_ui_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
