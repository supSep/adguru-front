__author__ = 'sepehrtaheri'


from robobrowser import RoboBrowser


def usedeverywhere_post(record_id):
    browser = RoboBrowser(history=True)
    browser.open('http://rapgenius.com/')
    return record_id