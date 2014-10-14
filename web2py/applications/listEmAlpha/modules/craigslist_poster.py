__author__ = 'sepehrtaheri'

from robobrowser import RoboBrowser


def postcl(form, zip):
    formpics = 0
    # Browse to Rap Genius
    browser = RoboBrowser(history=True)
    browser.open('https://post.craigslist.org/c/van?lang=en')

    # db(db_category.location == form.category)
    # db(db_location.location == form.location)

    cl_category = 'Video Games'
    cl_location = 'North Van'

    type = browser.get_form(class_='catpick picker')

    type['id'].value = 'fso'

    browser.submit_form(type)

    category = browser.get_form(class_='catpick picker')
    category['id'].value = '151'

    browser.submit_form(category)

    subarea = browser.get_form(class_='subareapick picker')
    subarea['n'].value = '2'

    browser.submit_form(subarea)

    #post = browser.get_form(id_='postingForm')
    post = browser.get_forms()[0]


    post['ConfirmEMail'].value = form['email']
    post['FromEMail'].value = form['email']
    post['contact_phone_ok'].value = '1'
    post['contact_phone'].value = form['phone_number']
    post['PostingTitle'].value = form['adTitle']
    post['Ask'].value = form['adPrice']
    post['postal'].value = zip
    post['GeographicArea'].value = form['location_vancouver_id']
    post['PostingBody'].value = form['adDesc']

    browser.submit_form(post)

    if(str(browser.url).find('geoverify') > 0):
        geoverify = browser.get_forms()[0]
        browser.submit_form(geoverify)

    if(str(browser.url).find('editimage') > 0 and formpics > 0):
        browser.follow_link(browser.get_link('classic'))
        editimage = browser.get_form(class_='add')
        for i in range(formpics):
            editimage['file'].value = open('path/to/file.txt', 'r')
        browser.submit_form(browser.get_forms()[2])

    else:
        #editimage = browser.get_forms()[0]
        browser.submit_form(browser.get_forms()[2])

    publish = browser.get_forms()[0]
    browser.submit_form(publish)

    return str(browser.url).find('mailoop') > 0