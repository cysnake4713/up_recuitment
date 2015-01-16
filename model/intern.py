__author__ = 'cysnake4713'
# coding=utf-8

import logging
from openerp import exceptions
from openerp.tools.translate import _
from openerp.osv import osv, fields

_logger = logging.getLogger(__name__)


class HrMember(osv.Model):
    _name = 'hr.member'
    _columns = {
        'name': fields.char('Name', 64, required=True),
        'type': fields.selection([('intern', 'Intern'), ('recuit', 'Recuit')], 'Member Type'),
        'gender': fields.selection([(u'男', u'男'), (u'女', u'女')], 'Gender'),
        'birthday': fields.date('Birthday'),
        'native_place': fields.char('Native Place', 32),
        'folk': fields.char('Folk', 32),
        'academy': fields.char("Academy", 128),
        'major': fields.char("Major", 128),
        'start_date': fields.date('Start Date'),
        'end_date': fields.date('End Date'),
        'moblie': fields.char('Moblie', 24),
        'qq': fields.char('QQ or Weichat', size=32),
        'image': fields.binary('Image'),
        'resume': fields.binary('Resume'),
        'resume_name': fields.char('Resume Name', 128),
        'works': fields.binary('Works'),
        'works_name': fields.char('Works Name', 128),
        'create_date': fields.datetime('Created on', select=True),
        'id_number': fields.char('ID Number', size=32),
        'id_image': fields.binary('ID Scan Image'),
        'id_image_name': fields.char('ID Scan Image Name', size=64),
        'student_id_image': fields.binary('Student ID Image'),
        'student_id_image_name': fields.char('Student ID Image Name', size=64),

        'emergency_name': fields.char('Emergency Name', 64),
        'emergency_relation': fields.char('Emergency Relation', 64),
        'emergency_phone': fields.char('Emergency Phone', 64),

        'is_contected': fields.char('Is Contected to company', 64),
    }

    _sql_constraints = {
        ('id_number_unique', 'unique (id_number)', 'The id_number of the member must be unique!')
    }

    def create_by_id_number(self, cr, uid, values, context=None):
        try:
            if 'id_number' in values:
                member_id = self.search(cr, uid, [('id_number', '=', values['id_number'])], context=context)
                if member_id:
                    self.write(cr, uid, member_id, values, context)
                else:
                    self.create(cr, uid, values, context)
                return 1
            else:
                _logger.warning('id_number is not nullable!')
                return 0
        except Exception, e:
            _logger.error(str(e))
            return 0