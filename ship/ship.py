# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

from openerp.osv.orm import Model
from openerp.osv import fields
from openerp.tools.translate import _


class ship_info(osv.osv):
		_name = 'ship.info'
		_discription = '船舶信息'
		_order = 'ship_id desc'
		_rec_name = 'ship_id' #显示的是name的值,没建的话重写
		_columns = { 
				'ship_id':fields.char( u'编号',size=64,select=1),
        
        'ship_kind':fields.many2one( 'ship.kind',string=u'船舶类别',select=1, domain=[('sequence','<>',0)]),
        'cus_kind': fields.selection([('agency',u'中介'),('owner', u'船东'),('ship_company', u'船舶管理公司'),],string=u'客户类型', select=1),
        'ship_company':fields.many2one( 'res.partner',string=u'所属客户',select=False, domain=[('is_company','=',True)]),
        'ship_name':fields.char( u'船名',size=64,select=1),
        'imo':fields.char( u'IMO号码',size=64,select=1),
        'info_from':fields.char( u'信息来源',size=64,select=1),
        'feature':fields.char( u'特征参数',size=64,select=1),
        'factory':fields.char( u'建造厂',size=64,select=1),
        'owner_price':fields.float( u'船东报价(万元)',size=64,select=1),
        'price':fields.float( u'报价(万元)',digits=(16,2),select=1),
        'ship_contact':fields.many2one( 'res.partner',string=u'联系人',select=False, domain=[('is_company','=',False)]),
        'publish_date':fields.date( u'信息发布日期',size=64,select=1),
        'remark':fields.text(u'备注',select=1),
        'tracking':fields.text(u'跟踪备注',select=1),
        'sale_status': fields.selection([('sell',u'出售'),('buy', u'求购'),('bought', u'已购'),('sold', u'已售'),],string=u'出售情况', required=1,select=False),
        'sale_kind': fields.selection([('sell',u'出售'),('buy', u'求购'),],string=u'出售性质', required=1,select=False),
        'query_ppl':fields.char( u'配置查询用户',size=64,select=1),
        'used_name':fields.char( u'船舶曾用名',size=64,select=1),
        'call_sign':fields.char( u'呼号',size=64,select=1),
        'register_id':fields.char( u'登记号',size=64,select=1),
        'main_power':fields.float( u'主机功率(PS)',digits=(16,2),select=1),
        #'attachment':fields.many2many( 'ir.attachment',string=u'相关附件',select=False),
        'owner_raise_date':fields.date( u'报价日期/有效期(船东)',select=1),
        'raise_date':fields.date( u'报价日期/有效期',select=1),
        'expiry_date':fields.date( u'有效期',select=1),
        
        
        'build_date':fields.date( u'建造年月',select=1),
        'build_date2':fields.date( u'(至)建造年月',select=1),
        
        'ship_grade': fields.selection([('ZC',u'中国船级社/ZC'),('CCS', u'中国船级社/CCS'),
        ('ABS',u'美国船级社/ABS'),('BV', u'法国船级社/BV'),
        ('DNV',u'挪威船级社/DNV'),('GL', u'德国船级社/GL'),
        ('KR',u'韩国船级社/KR'),('LR', u'劳埃德船级社/LR'),
        ('NK',u'日本船级社/NK'),('RINA', u'意大利船级社/RINA'),
        ('PRS',u'波兰船舶登记局/PRS'),('RS', u'俄罗斯船舶登记局/RS'),
        ('IRS',u'印度船级社/IRS'),('CRS',u'克罗地亚船舶登记局/CRS'),('other',u'其他')],
        string=u'船级社', required=1,select=1),
        
        'cargo_ton':fields.float( u'载重吨',digits=(16,2),select=1),
        'deadweight_ton':fields.float( u'净吨',digits=(16,2),select=1),
        'long':fields.float( u'总长(米)',digits=(16,2),select=1),
        'wide':fields.float( u'船宽(米)',digits=(16,2),select=1),
        'absorb':fields.float( u'吃水(米)',digits=(16,2),select=1),
        'hatch_num':fields.integer( u'舱/舱口数量',select=1),
        'hatch_lid':fields.char( u'舱盖形式',size=64,select=1),
        'deck':fields.integer( u'甲板层数',select=1),
        'hatch_oil':fields.float( u'燃油舱容(立方米)',digits=(16,2),select=1),
        'yazaicang':fields.char( u'压载舱',size=64,select=1),
        'main_engine':fields.char( u'主机',size=64,select=1),
        'second_engine':fields.char( u'副机',size=64,select=1),
        'thruster':fields.char( u'推进器类型',size=64,select=1),
        'dynamo':fields.char( u'发电机',size=64,select=1),
        'oil_wear':fields.float( u'油耗(吨/天)',digits=(16,2),select=1),
        'speed':fields.float( u'航速(节)',digits=(16,2),select=1),
        'tejian':fields.date( u'特检',select=1),
        'build_country':fields.char( u'建造国',size=64,select=1),
        'flag':fields.char( u'船旗',size=64,select=1),
        'total_ton':fields.float( u'总吨',digits=(16,2),select=1),
        'light_ton':fields.float( u'轻吨',digits=(16,2),select=1),
        'droop_space':fields.float( u'垂线间长(米)',digits=(16,2),select=1),
        'deep':fields.float( u'型深(米)',digits=(16,2),select=1),
        'cabin_hold':fields.char( u'舱容',size=64,select=1),
        'hatch_size':fields.char( u'舱口尺寸',size=64,select=1),
        'deck_bear':fields.float( u'甲板承重',digits=(16,2),select=1),
        'crane':fields.char( u'吊机',size=64,select=1),
        'tension':fields.float( u'拉力(吨)',digits=(16,2),select=1),
        'hatch_fresh_water':fields.float( u'淡水舱容(立方米)',digits=(16,2),select=1),
        'oil_kind':fields.char( u'燃油种类',size=64,select=1),
        'sail_district':fields.char( u'航区',size=64,select=1),
        'wujian':fields.date( u'坞检',select=1),
        'staff':fields.many2one( 'res.users',string=u'负责人',select=False),
                
         }
         
		def _buid_day_check(self, cr, uid, ids, context=None):
				if context is None:
						context = {}
				product = self.read(cr, uid, ids, ['build_date','build_date2'], context=context)
				if product[0]['build_date'] > product[0]['build_date2'] and product[0]['build_date2'] != 0:
						return False
				return True
         
		_constraints = [
        (_buid_day_check, u'建造起始日期不能小于结束日前' , [u'建造年月']),
        ]
        
		_sql_constraints = [
        ('uniq_ship_id', 'unique(ship_id)', "The ship id must be unique"),
        ]
         
		def _get_sale_kind(self, cr, uid, context):
				if context is None:
						context = {}
				if context.get('sale_kind') == 'sell':
						return 'sell'
				if context.get('sale_kind') == 'buy':
						return 'buy'
         
		_defaults = {
        'staff': lambda obj, cr, uid, context: uid,
        'ship_id': lambda * a: '/',
        'ship_grade': 'other',
        'build_date2': 0,
        'sale_kind': _get_sale_kind,
        'publish_date': fields.date.context_today, 
    }
    
    
		def create(self, cr, uid, vals, context=None):
				if context is None:
						context = {}
				if not 'ship_id' in vals or vals['ship_id'] == '/':
						vals['ship_id'] = self.pool.get('ir.sequence').get(cr, uid, 'ship.shipid')
				if vals['sale_kind'] == 'sell':
						vals['ship_id'] = 'S' + vals['ship_id']
				if vals['sale_kind'] == 'buy':
						vals['ship_id'] = 'R' + vals['ship_id']
				return super(ship_info, self).create(cr, uid, vals, context)

		def write(self, cr, uid, ids, vals, context={}):
				if not isinstance(ids, list):
						ids = [ids]
				ship_without_id = self.search(cr, uid, [('ship_id', 'in', [False, '/']),('id', 'in', ids)], context=context)
				direct_write_ids = set(ids) - set(ship_without_id)
				super(ship_info, self).write(cr, uid, list(direct_write_ids), vals, context)
				for product_id in ship_without_id:
						vals['ship_id'] = self.pool.get('ir.sequence').get(cr, uid, 'ship.shipid')
						if vals['sale_kind'] == 'sell':
								vals['ship_id'] = 'S' + vals['ship_id']
						if vals['sale_kind'] == 'buy':
								vals['ship_id'] = 'R' + vals['ship_id']
						super(ship_info, self).write(cr, uid, product_id, vals, context)
				return 1

		def copy(self, cr, uid, id, vals, context=None):
				product = self.read(cr, uid, id, ['ship_id'], context=context)						
				if  product['ship_id']:
						vals.update({
								'ship_id': self.pool.get('ir.sequence').get(cr, uid, 'ship.shipid'),
						})
						
				return super(ship_info, self).copy(cr, uid, id, vals, context)

    
ship_info()