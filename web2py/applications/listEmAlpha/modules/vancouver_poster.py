__author__ = 'sepehrtaheri'


def post(form, zip):
    #usedeverywhere_post(form)
    #kijiji_post(form)
    #print craigslist_post(form, zip)
    return "success"


def usedeverywhere_post(form):
    #import usedeverywhere_post
    return form


def kijiji_post(form):
    #import kijiji_post
    return form


def craigslist_post(form, zip):
    from applications.listEmAlpha.modules.craigslist_poster import postcl
    clposted = postcl(form, zip)
    return clposted