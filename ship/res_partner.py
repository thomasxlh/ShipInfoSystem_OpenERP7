# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields

class res_partner(osv.osv):
    """Override users due to change defalt partner id in partner"""
    _inherit = "res.partner"
    
#add for one2namy to ship.info
    def _get_id(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for rec in self.browse(cr, uid, ids, context=context):
            res[rec.id] = rec.id
        return res
        
    _columns = {
        #copy from partner.id
        'ship_contact': fields.function(_get_id, string="Partner id", type='char', method=True),
        'ship_company': fields.function(_get_id, string="Partner id", type='char', method=True),
        'cus_ships': fields.one2many('ship.info', 'ship_contact', 'Customer sell ships', domain=[('sale_kind','=','sell')]),
        'cus_ships_buy': fields.one2many('ship.info', 'ship_contact', 'Customer buy ships', domain=[('sale_kind','=','buy')]),
        'com_ships': fields.one2many('ship.info', 'ship_company', 'Company sell ships', domain=[('sale_kind','=','sell')]),
        'com_ships_buy': fields.one2many('ship.info', 'ship_company', 'Company buy ships', domain=[('sale_kind','=','buy')]),
        'remark': fields.text( 'remark',select=1),
    }

    _defaults = {
        'user_id': lambda obj, cr, uid, context: uid,
        #'date': fields.date.context_today, 
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
