from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Test Model"
    #_postcode = "estate.property"
    #_date_availability = "estate.property"
    #_expected_price = "estate.property"
    #_selling_price = "estate.property"
    #_bedrooms = "estate.property"
    #_living_area = "estate.property"
    #_facades = "estate.property"
    #_garage = "estate.property"
    #_garden = "estate.property"
    #_garden_area = "estate.property"
    #_garden_orientation = "estate.property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to separate garden orientation"
    )





