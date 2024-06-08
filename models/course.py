# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'college.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    department_id = fields.Many2one('college.department', string='Department')
    student_ids = fields.Many2many('college.student', string='Students')
    faculty_ids = fields.Many2many('college.faculty', string='Faculty')