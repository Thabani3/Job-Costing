from odoo import models, fields, api

class OverheadCost(models.Model):
    _name = 'job_costing.overhead_cost'
    _description = 'Overhead Cost'

    job_id = fields.Many2one('job_costing.job', string='Job')
    overhead_amount = fields.Float(string='Overhead Amount')
    activity_driver = fields.Float(string='Activity Driver', help="e.g., total labor hours")
    predetermined_rate = fields.Boolean(string="Use Predetermined Rate")
    overhead_rate = fields.Float(compute='_compute_overhead_rate', string="Overhead Rate")
    total_overhead_cost = fields.Float(compute='_compute_total_overhead_cost', string="Total Overhead Cost")

    @api.depends('overhead_amount', 'activity_driver', 'predetermined_rate')
    def _compute_overhead_rate(self):
        for record in self:
            record.overhead_rate = record.overhead_amount if record.predetermined_rate else record.overhead_amount / record.activity_driver if record.activity_driver else 0.0

    @api.depends('overhead_rate', 'activity_driver')
    def _compute_total_overhead_cost(self):
        for record in self:
            record.total_overhead_cost = record.overhead_rate * record.activity_driver
