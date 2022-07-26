from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "One2many Test Model"

    price = fields.Float()
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False)
    partner_id = fields.Many2one(comodel_name="res.partner", string="Salesperson", required=True)
    property_id = fields.Many2one(comodel_name="estate.property", string="Property", required=True)
