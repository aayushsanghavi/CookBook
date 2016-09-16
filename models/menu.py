# -*- coding: utf-8 -*-

response.logo = A(B('Cook',SPAN('Book')),
                  _class="navbar-brand",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index')),
    (T('Upload recipe'), False, URL('default','upload_recipe')),
    (T('View most voted recipes'), False, URL('default','list_recipes_by_votes')),
    (T('My recipes'), False, URL('default','my_recipes',args=auth.user_id)),
    (T('Manage'),False,URL('default','manage'))
]

if "auth" in locals(): auth.wikimenu()
