from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from random import randint


class PlanningRoleTraining(models.Model):
    _name = "planning.role.training"
    _description = "Planning Role Training"
    _order = "id desc"

    def _get_default_color(self):
        return randint(1, 11)

    sequence = fields.Integer()
    company_id = fields.Many2one(
        comodel_name="res.company",
        # string='Company',
        required=True,
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="company_id.currency_id",
        store=True,
        required=True,
    )

    name = fields.Char(
        required=True,
        index=True,
    )

    point_rate = fields.Integer(
        default=0,
        required=True,
    )
    amount = fields.Monetary(
        default=0.00,
        required=True,
        currency_field="currency_id",
    )
    color = fields.Integer(
        default=_get_default_color,
        required=True,
    )

    active = fields.Boolean(
        default=True,
        required=True,
    )

    resource_ids = fields.Many2many(
        comodel_name="resource.resource",
        relation="planning_resource_ids",
        column1="planning_role_id",
        column2="resource_id",
        required=True,
        # string='Resource',
        domain="[('id', 'in', available_resource_ids)]",
    )
    available_resource_ids = fields.Many2many(
        comodel_name="resource.resource",
        # string='Available Resource',
        compute="_compute_available_resource_ids",
    )

    # Validasi untuk setiap Company agar tidak ada nama yang sama
    @api.constrains("name")
    def _check_unique_name(self):
        for record in self:
            if self.search(
                [
                    ("name", "=", record.name),
                    ("company_id", "=", record.company_id.id),
                    ("id", "!=", record.id),
                ]
            ):
                raise ValidationError("The Name field must be unique for same Company!")

    # Compute yang depends terhadap Field Active
    @api.depends("active")
    def _compute_available_resource_ids(self):
        for rec in self:
            # Digunakan untuk Mendefinisikan Model / Table yang hendak digunakan
            resource_obj = self.env["resource.resource"]
            if rec.active:
                # Jika Role ID dalam posisi aktif akan dilakukan eksekusi kondisi yang ini
                # Mencari Existing Resource yang sudah terpakai pada Model ini
                used_resource_ids = list(
                    set(self.search([("active", "=", True)]).mapped("resource_ids.id"))
                )

                # Mencari Available Resource dan diassing Resultnya ke Field Available Resource IDS
                rec.available_resource_ids = resource_obj.search(
                    [("id", "not in", used_resource_ids)]
                )
            else:
                # Mencari Data Seluruh Resource yang ada tanpa terkecuali jika Role dalam kondisi tidak Aktif
                rec.available_resource_ids = resource_obj.search([])
