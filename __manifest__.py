{
    'name': 'College_Management_app',
    'author': 'Alka',
    'version': '1.0',
    'summary': 'College Management System',
    'sequence': -100,
    'description': """College Management System""",
    'category': 'Education',
    'website': 'https://www.example.com',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'security/college_security.xml',
        'views/student_views.xml',
        'views/faculty_views.xml',
        'views/department_views.xml',
        'views/course_views.xml',
        'views/menus.xml',
        'data/college_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'

}