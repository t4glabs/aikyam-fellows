import frappe

no_cache = 1
no_sitemap = 1

def get_context(context):
    context.open_jobs = frappe.db.get_all( 'Job Opening', filters={'status': 'Open'}, fields =['job_title','route','custom_introduction']
    )

    # context.show_sidebar = 1
    return context