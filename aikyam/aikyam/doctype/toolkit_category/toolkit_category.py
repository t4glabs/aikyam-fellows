# Copyright (c) 2023, JinsoRaj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import get_doc

class ToolkitCategory(Document):
	def after_insert(self):
		sidebar = get_doc('Website Sidebar', 'ToolKit Sidebar')
		sidebar.append('sidebar_items', { 
			'title': self.category,
			'route': f'/toolkit/{self.name}'
		})
		sidebar.save()
	
	def after_delete(self):
		sidebar = get_doc('Website Sidebar', 'ToolKit Sidebar')
		items = sidebar.get('sidebar_items')
		for item in items:
			if item.title == self.category:
				items.remove(item)
				break
				
		sidebar.save()





