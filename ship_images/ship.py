# -*- coding: utf-8 -*-
#########################################################################
# Copyright (C) 2009  Sharoon Thomas, Open Labs Business solutions      #
# Copyright (C) 2011 Akretion Sébastien BEAU sebastien.beau@akretion.com#
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################
import os
import shutil
import logging
import base64
import urllib

from openerp.osv import orm, fields


class ship_info(orm.Model):
    _inherit = "ship.info"

    def copy(self, cr, uid, id, default=None, context=None):
        if not default:
            default = {}
        original = self.read(cr, uid, id, fields=['ship_id', 'image_ids'], context=context)
        default.update({
            'image_ids': False,
        })
        local_media_repository = self.pool.get('res.company').get_local_media_repository(cr, uid, context=context)
        if local_media_repository:
            if original['image_ids']:
                old_path = os.path.join(local_media_repository, original['ship_id'])
                if os.path.isdir(old_path):
                    try:
                        shutil.copytree(old_path, old_path + '-copy')
                    except:
                        logger = logging.getLogger('ship_images_olbs')
                        logger.exception('error while trying to copy images '
                                         'from %s to %s',
                                         old_path,
                                         old_path + '.copy')

        return super(ship_info, self).copy(cr, uid, id, default, context=context)

    def get_main_image(self, cr, uid, id, context=None):
        if isinstance(id, list):
            id = id[0]
        images_ids = self.read(cr, uid, id, ['image_ids'], context=context)['image_ids']
        if images_ids:
            return images_ids[0]
        return False

    def _get_main_image(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        img_obj = self.pool.get('ship.images')
        for id in ids:
            image_id = self.get_main_image(cr, uid, id, context=context)
            if image_id:
                image = img_obj.browse(cr, uid, image_id, context=context)
                res[id] = image.file
            else:
                res[id] = False
        return res
        
    def _id_get(self, cr, uid, ids, field_name, arg, context):
         res = {}
         for rec in self.browse(cr, uid, ids, context=context):
             res[rec.id] = rec.id
         return res

    _columns = {
        'ship_table_id': fields.function(_id_get, string="ship table id", type='char', method=True),
        'image_ids': fields.one2many(
                'ship.images',
                'ship_table_id',
                string='Ship Images'),
        'ship_image': fields.function(
            _get_main_image,
            type="binary",
            string="Main Image"),
    }

    def write(self, cr, uid, ids, vals, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        # here we expect that the write on ship_id is always on 1 ship because there is an unique constraint on the default code
        if vals.get('ship_id') and ids:
            local_media_repository = self.pool.get('res.company').get_local_media_repository(cr, uid, context=context)
            if local_media_repository:
                old_ship = self.read(cr, uid, ids[0], ['ship_id', 'image_ids'], context=context)
                res = super(ship_info, self).write(cr, uid, ids, vals, context=context)
                if old_ship['image_ids']:
                    if old_ship['ship_id'] != vals['ship_id']:
                        old_path = os.path.join(local_media_repository, old_ship['ship_id'])
                        if os.path.isdir(old_path):
                            os.rename(old_path,  os.path.join(local_media_repository, vals['ship_id']))
                return res
        return super(ship_info, self).write(cr, uid, ids, vals, context=context)

    def create_image_from_url(self, cr, uid, id, url, image_name=None, context=None):
        (filename, header) = urllib.urlretrieve(url)
        with open(filename, 'rb') as f:
            data = f.read()
        img = base64.encodestring(data)
        filename, extension = os.path.splitext(os.path.basename(url))
        data = {'name': image_name or filename,
                'extension': extension,
                'file': img,
                'ship_table_id': id,
                }
        new_image_id = self.pool.get('ship.images').create(cr, uid, data, context=context)
        return True
