# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Department(models.Model):
    _name = 'college.department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    faculty_ids = fields.One2many('college.faculty', 'department_id', string='Faculty')
    course_ids = fields.One2many('college.course', 'department_id', string='Courses')