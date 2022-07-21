from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Many2one Test Model"
    name = fields.Char(required=True)



