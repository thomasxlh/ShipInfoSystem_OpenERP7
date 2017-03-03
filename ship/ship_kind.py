# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
class ship_kind(osv.osv):
		_name = 'ship.kind'
		#_rec_name = 'complete_name' #显示的是name的值,没建的话重写   ------- 不能加，会不可用而显示出全部记录The field 'Name' (complete_name) can not be searched: non-stored function field without fnct_search
		def name_get_full(self, cr, uid, ids, context=None):
				if isinstance(ids, (list, tuple)) and not len(ids):
						return []
				if isinstance(ids, (long, int)):
						ids = [ids]
				reads = self.read(cr, uid, ids, ['name','parent_id'], context=context)
				res = []
				for record in reads:
						name = record['name']
						if record['parent_id']:
								name = record['parent_id'][1]+' / '+name
						res.append((record['id'], name))
				return res

		def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
				res = self.name_get_full(cr, uid, ids, context=context)
				return dict(res)

		_description = "Ship Category"
		
		
		_columns = {
				'name': fields.char('Name', size=64, required=True, translate=True, select=True),
				'complete_name': fields.function(_name_get_fnc, type="char", string='Name'),
				'parent_id': fields.many2one('ship.kind','Parent Category', select=True, ondelete='cascade'),
				'child_id': fields.one2many('ship.kind', 'parent_id', string='Child Categories'),
				'sequence': fields.integer('Sequence', select=True, help="Gives the sequence order when displaying a list of product categories."),
				'parent_left': fields.integer('Left Parent', select=1),
				'parent_right': fields.integer('Right Parent', select=1),
				
		}


		_defaults = {
		}

		_parent_name = "parent_id"
		_parent_store = True
		_parent_order = 'sequence, name'
		_order = 'parent_left'

		def _check_recursion(self, cr, uid, ids, context=None):
				level = 100
				while len(ids):
						cr.execute('select distinct parent_id from ship_kind where id IN %s',(tuple(ids),))
						ids = filter(None, map(lambda x:x[0], cr.fetchall()))
						if not level:
								return False
						level -= 1
				return True

		_constraints = [
				(_check_recursion, 'Error ! You cannot create recursive categories.', ['parent_id'])
		]
		def child_get(self, cr, uid, ids):
				return [ids]
				 
ship_kind(
)