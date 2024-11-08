from odoo import models, fields, api

class MaterialCost(models.Model):
    _name = 'job_costing.material_cost'
    _description = 'Material Cost'

    job_id = fields.Many2one('job_costing.job', string='Job')
    material_name = fields.Char(string='Material Name', required=True)
    material_cost = fields.Float(string='Material Cost')
    quantity = fields.Float(string='Quantity')
    total_material_cost = fields.Float(compute='_compute_total_material_cost', string='Total Material Cost')

    @api.depends('material_cost', 'quantity')
    def _compute_total_material_cost(self):
        for record in self:
            record.total_material_cost = record.material_cost * record.quantity
