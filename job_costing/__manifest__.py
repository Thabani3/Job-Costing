{
    'name': 'Job Costing',
    'version': '1.0',
    'summary': 'Module for managing job costs including materials, labor, overheads, and subcontractors.',
    'description': """Manage job-related expenses and calculate total job costs""",
    'author': 'Thabaniirvin Miya',
    'depends': ['base', 'hr', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/job_costing_actions.xml',
        'views/job_costing_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
