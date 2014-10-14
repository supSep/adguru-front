db.define_table('location',
                Field('main_city', 'text'),
                Field('section_city', 'text'),
                Field('craigs_location', 'text', notnull=True),
                Field('kijiji_location', 'text', notnull=True),
                Field('used_url', 'text', notnull=True),
                Field('craigs_url', 'text', notnull=True),
                Field('kijiji_url', 'text', notnull=True),
                Field('used_url', 'text', notnull=True), migrate=False)
