from __future__ import unicode_literals
import frappe
from frappe import _

def get_data():
	return {
		'fieldname': 'delivery_note',
		'non_standard_fieldnames': {
			'Stock Entry': 'delivery_note_no',
			'Quality Inspection': 'reference_name',
			'Auto Repeat': 'reference_document',
			'Delivery Note': 'return_against',
			'Installation Note': 'prevdoc_docname',
		},
		'internal_links': {
			'Sales Order': ['items', 'sales_order'],
			'Quotation': ['items', 'quotation'],
			'Vehicle': ['items', 'vehicle']
		},
		'transactions': [
			{
				'label': _('Fulfilment'),
				'items': ['Sales Invoice', 'Packing Slip', 'Delivery Trip']
			},
			{
				'label': _('Reference'),
				'items': ['Sales Order', 'Quotation', 'Installation Note']
			},
			{
				'label': _('Reference'),
				'items': ['Quality Inspection', 'Auto Repeat']
			},
			{
				'label': _('Returns'),
				'items': ['Delivery Note']
			},
		]
	}
