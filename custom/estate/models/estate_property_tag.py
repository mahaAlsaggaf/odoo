from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Many2many Test Model"
    name = fields.Char(required=True)