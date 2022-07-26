from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta


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
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(copy=False, default=date.today() + relativedelta(months=+3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean(readonly=False)
    garden = fields.Boolean(readonly=False)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to separate garden orientation"
    )
    active = fields.Boolean('Active', default=True, readonly=False)
    state = fields.Selection(
        required=True,
        copy=False,
        string='State',
        selection=[('new', 'New'), ('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('sold', 'Sold'),
                   ('canceled', 'Canceled')],
        default="new"
    )
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Estate Property Type")
    salesperson_id = fields.Many2one(comodel_name="res.partner", default=lambda self: self.env.user, string="Salesman")
    buyer_id = fields.Many2one(comodel_name="res.users", copy=False, string="Buyer")
    tag_id = fields.Many2many("estate.property.tag", string="Tags")
    offer_id = fields.One2many("estate.property.offer", "property_id", copy=False, string="Offer")




