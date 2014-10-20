import json
from applications.adguru.models.category.categoryMapper import title_category
from applications.adguru.models.location.locationMapper import title_location

__author__ = 'sepehrtaheri'


def createpost(form):
    import requests
    posturl = 'http://localhost:5000/vancouver/post/'
    headers = {'content-type': 'application/json'}
    #location = title_location[form['location_vancouver_id']]
    #category = title_category[form['category_id']]
    payload  = {
        'id': form['id'],
        'category': form['category_id'],
        'location': form['location_vancouver_id'],
        'title' : form['adTitle'],
        'email': form['email'],
        'phone': form['phone_number'],
        'description': form['adDesc'],
        'price': form['adPrice']
    }
    response = requests.post(posturl, data=json.dumps(payload), headers=headers)
    print response.text
    return response.text