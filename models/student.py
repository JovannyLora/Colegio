# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'college.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    enrollment_number = fields.Char(string='Enrollment Number')
    department_id = fields.Many2one('college.department', string='Department')
    course_ids = fields.Many2many('college.course', string='Courses')