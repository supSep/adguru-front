# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################
    # bootstrap3 theme for web2py
from gluon import current
current.auth = auth
from applications.adguru.modules.bootstrap3 import navbar, menu

response.logo = A(B('adguru'),
                  _class="navbar-brand",_href=URL('default', 'index'))
response.title = request.application.replace('_',' ').title()
response.subtitle = 'Post and sell your items on many sites with ease'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Sep Taheri <admin@sepehr.ca>'
response.meta.keywords = 'AD POST SELL CLASSIFIEDS BUY CRAIGSLIST CRIAGS KIJIJI'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################


response.menu = [['Post',True,URL('default', 'post')]]
              # ['Search Ads',True,URL('default', 'searchposts')]]

if auth.is_logged_in():
    response.menu += [['Profile',True,URL('default', 'profile')],
                      ['Contact Us',True,URL('default', 'ask')]]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################


def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (SPAN('web2py', _class='highlighted'), False, 'http://web2py.com', [
        (T('This App'), False, URL('admin', 'default', 'design/%s' % app), [
        (T('Controller'), False,
         URL(
         'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
        (T('View'), False,
         URL(
         'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
        (T('Layout'), False,
         URL(
         'admin', 'default', 'edit/%s/views/layout.html' % app)),
        (T('Stylesheet'), False,
         URL(
         'admin', 'default', 'edit/%s/static/css/web2py.css' % app)),
        (T('DB Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/db.py' % app)),
        (T('Menu Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/menu.py' % app)),
        (T('Database'), False, URL(app, 'appadmin', 'index')),
        (T('Errors'), False, URL(
         'admin', 'default', 'errors/' + app)),
        (T('About'), False, URL(
         'admin', 'default', 'about/' + app)),
        ])])]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
