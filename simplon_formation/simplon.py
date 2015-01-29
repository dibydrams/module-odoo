__author__ = 'Diby'

from openerp.osv import fields, osv, orm

class simplon_formation(osv.osv):
	_name = "simplon.formation"
	_description = "Formation"
	_columns = {
		'name':fields.char('Nom',size=64, required=True),
		'partner_id':fields.many2one('res.partner', 'Customer'),
	}

def create(self, cr, uid, vals, context=None):
	vals['name'] = 'Simplon' + vals['name']
	res = super(simplon_formation, self).create(cr, uid, vals, context=context)
	return res

def write

def unlink

def invoice_open(cr, uid,ids, context=None):

simplon_formation()