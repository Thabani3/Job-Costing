from odoo import models, fields

class SubcontractorCost(models.Model):
    _name = 'job_costing.subcontractor_cost'
    _description = 'Subcontractor Cost'

    job_id = fields.Many2one('job_costing.job', string='Job')
    subcontractor_name = fields.Char(string='Subcontractor Name')
    service_cost = fields.Float(string='Service Cost')
