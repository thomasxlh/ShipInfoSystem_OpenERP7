{
    "name" : "Ship",#模块名
    "version" : "1.1",       #模块版本
    "description" : 'Ship', #模块说明
    "author" : "Thomas Huang",   #作者
    "website" : "http://www.openerp.cn",#网址
    "depends" : [],                   #依赖的模块
    'qweb' : [
        'static/src/xml/hide_export.xml',		#取消export
    ],
		"data": [
				'security/ir.model.access.csv',
				'security/ir_ship_rule.xml',
        'views/ship_view.xml',
        'views/ship_partner_view.xml',
        'views/ship_kind_view.xml',
        'views/ship_kind_require_view.xml',
        'views/ship_kind_manage_view.xml',
        'views/ship_kind_view2.xml',
    ],
    "init_xml" : [
        'views/ship_id_sequence.xml',
    ],
    "update_xml" : [
    ],  #模块更新的时候会读入的文件
    "installable" : True,                #可否安装                 
    "category":'Generic Modules/Others' #模块类型
}