# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    if not auth.is_logged_in():
        response.flash = T("Welcome to web2py!")
        return dict(message=T('Hello World'))
    if auth.is_logged_in():
        response.flash = T("")
        query = (db.vancouver)
        sortorder = [db.vancouver.dateCreated]
        exportclasses=dict(
                csv_with_hidden_cols=False,
                xml=False,
                html=False,
                csv=False,
                json=False,
                tsv_with_hidden_cols=False,
                tsv=False)
        ads = SQLFORM.grid(query=query, deletable=False, editable=False,
                           orderby=sortorder, paginate=10, exportclasses=exportclasses, maxtextlength=64)
        return dict( content=ads)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

@auth.requires_login()
def profile():
    response.title = "User Profile"
    userId = request.vars['uid']
    if userId == None:
        query = (db.vancouver.user_id == auth.user.id)
    else:
        query = (db.vancouver.user_id == userId)
    sortorder = [db.vancouver.dateCreated]
    exportclasses=dict(
            csv_with_hidden_cols=False,
            xml=False,
            html=False,
            csv=False,
            json=False,
            tsv_with_hidden_cols=False,
            tsv=False)
    ads = SQLFORM.grid(query=query, deletable=False, editable=False,
                       orderby=sortorder, paginate=25, exportclasses=exportclasses, maxtextlength=64)
    return dict(form=ads, user=auth.user)


def search():
    response.title = "Search Ads"
    #response.view = 'default/searchposts.html'
    response.flash = 'search submitted'
    searchform = SQLFORM.factory(
                  Field("searchbhar"),
                  formstyle='divs',
                  submit_button="Search").process()
    query = db.vancouver.isAdValid == 1
    print "SEARCHING"
    print searchform.vars.searchbhar
    if searchform.accepted:
        print 'aCCEPte2'
    if(searchform.vars.searchbhar != '' and searchform.vars.searchbhar !=  None):
        print "ACCEPTED"
        keywordvars = searchform.vars.searchbhar
        keywords = keywordvars.split(" ")
        for searchkey in keywords:
            query |= db.vancouver.adTitle.contains(searchkey)
            query |= db.vancouver.adDesc.contains(searchkey)
        count = db(query).count()
        searchresults = db(query).select(db.vancouver.dateCreated, db.vancouver.location_vancouver_id, db.vancouver.category_id,
                                     db.vancouver.adTitle, db.vancouver.adPrice, orderby=~db.vancouver.dateCreated)
        redirect(URL('default',  'searchresults', vars={searchresults, count, searchform}), client_side=True)
    return dict(form=searchform)
    #return response.render('default/searchposts.html', context)

def test():
    return "SEPSEP"


def searchposts(searchresults, count, form):
    return dict(results=searchresults, count=count, form=form)

@auth.requires_login()
def post():
    response.title = "Post an ExpressAd"
    form = SQLFORM(db.vancouver, showid=False, hidden=dict(user_id=auth.user_id, isAdValid=1))
    if form.process().accepted:
        response.flash = 'form accepted'
        createpost(form.vars)
        # redirect url
        # send to ad posting controller
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


def createpost(form):
    from applications.listEmAlpha.modules.vancouver_poster import post
    post(form, auth.user['zip'])
    return form


def ask():
    response.title = "Ask a question"
    if  auth.is_logged_in():
        form=SQLFORM.factory(
            Field('your_email',default=auth.user.email, requires=IS_EMAIL(), readable=False, writable=False),
            Field('user', default=auth.user_id, readable=False, writable=False),
            Field('question',requires=IS_NOT_EMPTY()))
    else:
        form=SQLFORM.factory(
            Field('name',requires=IS_NOT_EMPTY()),
            Field('your_email', requires=IS_EMAIL()),
            Field('question',requires=IS_NOT_EMPTY()))

    if form.process().accepted:
        if mail.send(to='admin@example.com',
                  subject='from %s' % form.vars.your_email,
                  message = form.vars.question):
            response.flash = 'Thank you'
            response.js = "jQuery('#%s').hide()" % request.cid
        else:
            form.errors.your_email = "Unable to send the email"
    return dict(form=form)


