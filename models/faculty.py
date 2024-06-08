# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Faculty(models.Model):
    _name = 'college.faculty'
    _description = 'Faculty'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    department_id = fields.Many2one('college.department', string='Department')
    course_ids = fields.Many2many('college.course', string='Courses')