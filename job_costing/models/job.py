from odoo import models, fields, api

class JobCostingJob(models.Model):
    _name = 'job_costing.job'
    _description = 'Job Costing'

    name = fields.Char(string='Job Name', required=True)
    material_cost_ids = fields.One2many('job_costing.material_cost', 'job_id', string='Material Costs')
    labour_cost_ids = fields.One2many('job_costing.labour_cost', 'job_id', string='Labour Costs')
    overhead_cost_ids = fields.One2many('job_costing.overhead_cost', 'job_id', string='Overhead Costs')
    subcontractor_cost_ids = fields.One2many('job_costing.subcontractor_cost', 'job_id', string='Subcontractor Costs')
    total_material_cost = fields.Float(compute='_compute_total_material_cost', string='Total Material Cost')
    total_labour_cost = fields.Float(compute='_compute_total_labour_cost', string='Total Labour Cost')
    total_overhead_cost = fields.Float(compute='_compute_total_overhead_cost', string='Total Overhead Cost')
    total_subcontractor_cost = fields.Float(compute='_compute_total_subcontractor_cost', string='Total Subcontractor Cost')
    total_job_cost = fields.Float(compute='_compute_total_job_cost', string='Total Job Cost')

    @api.depends('material_cost_ids.total_material_cost')
    def _compute_total_material_cost(self):
        for job in self:
            job.total_material_cost = sum(line.total_material_cost for line in job.material_cost_ids)

    @api.depends('labour_cost_ids.total_labour_cost')
    def _compute_total_labour_cost(self):
        for job in self:
            job.total_labour_cost = sum(line.total_labour_cost for line in job.labour_cost_ids)

    @api.depends('overhead_cost_ids.total_overhead_cost')
    def _compute_total_overhead_cost(self):
        for job in self:
            job.total_overhead_cost = sum(line.total_overhead_cost for line in job.overhead_cost_ids)

    @api.depends('subcontractor_cost_ids.service_cost')
    def _compute_total_subcontractor_cost(self):
        for job in self:
            job.total_subcontractor_cost = sum(line.service_cost for line in job.subcontractor_cost_ids)

    @api.depends('total_material_cost', 'total_labour_cost', 'total_overhead_cost', 'total_subcontractor_cost')
    def _compute_total_job_cost(self):
        for job in self:
            job.total_job_cost = job.total_material_cost + job.total_labour_cost + job.total_overhead_cost + job.total_subcontractor_cost
