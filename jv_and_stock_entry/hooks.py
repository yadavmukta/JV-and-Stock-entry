# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "jv_and_stock_entry"
app_title = "Jv And Stock Entry"
app_publisher = "info@progressiveit.in"
app_description = "Adding Stock Entry and Journal Entry Amounts in Project"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@progressiveit.in"
app_license = "MIT"


fixtures = ["Custom Field"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jv_and_stock_entry/css/jv_and_stock_entry.css"
# app_include_js = "/assets/jv_and_stock_entry/js/jv_and_stock_entry.js"

# include js, css files in header of web template
# web_include_css = "/assets/jv_and_stock_entry/css/jv_and_stock_entry.css"
# web_include_js = "/assets/jv_and_stock_entry/js/jv_and_stock_entry.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "jv_and_stock_entry.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jv_and_stock_entry.install.before_install"
# after_install = "jv_and_stock_entry.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jv_and_stock_entry.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events





doc_events = {
	
	"Project" : {
		"validate" : ["jv_and_stock_entry.jv_and_stock_entry.project_custom.update_amount","jv_and_stock_entry.jv_and_stock_entry.project_custom.update_stock_amount",
                "jv_and_stock_entry.jv_and_stock_entry.project_custom.update_journal_amount" ]
		
		
	}

	

}




# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jv_and_stock_entry.tasks.all"
# 	],
# 	"daily": [
# 		"jv_and_stock_entry.tasks.daily"
# 	],
# 	"hourly": [
# 		"jv_and_stock_entry.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jv_and_stock_entry.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jv_and_stock_entry.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jv_and_stock_entry.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jv_and_stock_entry.event.get_events"
# }

