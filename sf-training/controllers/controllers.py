# -*- coding: utf-8 -*-
# from odoo import http


# class Sf-training(http.Controller):
#     @http.route('/sf-training/sf-training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sf-training/sf-training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sf-training.listing', {
#             'root': '/sf-training/sf-training',
#             'objects': http.request.env['sf-training.sf-training'].search([]),
#         })

#     @http.route('/sf-training/sf-training/objects/<model("sf-training.sf-training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sf-training.object', {
#             'object': obj
#         })

