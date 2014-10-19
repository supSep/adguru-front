db.define_table('category',
                Field('category_title', 'text'),
                Field('craigslist', 'text', notnull=True),
                Field('kijiji', 'text', notnull=True),
                Field('usedeverywhere', 'text', notnull=True), migrate=False)
