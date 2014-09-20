import datetime


email=''
phone=''
if(auth.is_logged_in()):
    email=auth.user.email
    phone=auth.user.phone

db.define_table('vancouver',
                Field('location_vancouver_id'),  #, db.location_vancouver),
                Field('category_id'),  #, db.category, notnull=True),
                Field('user_id', db.auth_user, default=auth.user_id, writable=False, readable=False),
                Field('adTitle', 'string', notnull=True),
                Field('email',default=email, requires=IS_EMAIL(), notnull=True),
                Field('phone_number',default=phone, requires=IS_MATCH('[\d\-\(\) ]+'), notnull=True),
                Field('adDesc', 'text', notnull=True),
                Field('adPrice', 'integer', notnull=True),
                Field('isAdValid', 'integer', requires=IS_INT_IN_RANGE(0, 2), default=1, writable=False, readable=False),
                Field('dateCreated', 'datetime', notnull=True, writable=False, readable=False, default=datetime.datetime.now()),
                Field('dateEnded', 'datetime'), migrate=False)


