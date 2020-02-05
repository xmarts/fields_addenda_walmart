# -*- coding: utf-8 -*-
from odoo import http

# class FieldsAddendaWalmart(http.Controller):
#     @http.route('/fields_addenda_walmart/fields_addenda_walmart/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields_addenda_walmart/fields_addenda_walmart/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields_addenda_walmart.listing', {
#             'root': '/fields_addenda_walmart/fields_addenda_walmart',
#             'objects': http.request.env['fields_addenda_walmart.fields_addenda_walmart'].search([]),
#         })

#     @http.route('/fields_addenda_walmart/fields_addenda_walmart/objects/<model("fields_addenda_walmart.fields_addenda_walmart"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields_addenda_walmart.object', {
#             'object': obj
#         })