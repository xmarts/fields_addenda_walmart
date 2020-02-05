# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddFieldsAdendaWalmart(models.Model):
	_inherit = 'account.invoice'
	
	child_contact_name1 = fields.Char(string="Child Contact Name", compute='get_customer_contact_person')

	def get_customer_contact_person(self):
		if self.partner_id and self.partner_id.child_ids:
			self.customer_contact = ' '.join(str(person.name) for person in self.partner_id.child_ids)


	