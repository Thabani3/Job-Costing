from odoo import models, fields, api

class LabourCost(models.Model):
    _name = 'job_costing.labour_cost'
    _description = 'Labour Cost'

    job_id = fields.Many2one('job_costing.job', string='Job')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    hourly_rate = fields.Float(string='Hourly Rate')
    hours_worked = fields.Float(string='Hours Worked')
    total_labour_cost = fields.Float(compute='_compute_total_labour_cost', string='Total Labour Cost')

    @api.depends('hourly_rate', 'hours_worked')
    def _compute_total_labour_cost(self):
        for record in self:
            record.total_labour_cost = record.hourly_rate * record.hours_worked
