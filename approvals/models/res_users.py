from openerp import fields,models,api

class ResUsers(models.Model):
    _inherit = 'res.users'

    substitute_ids = fields.One2many('res.users','substitute_id', string="Substitutes")
    substitute_id = fields.Many2one('res.users', string="Substitute")
