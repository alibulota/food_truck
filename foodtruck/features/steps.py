from lettuce import *
from .. views import *
from .. models import *
import os
from contextlib import closing


TEST_DSN = 'dbname=test_food_truck user=jakeanderson'
settings = {'db': TEST_DSN}
INPUT_BTN = '<input type="submit" name="add" value="Truck It!"/>'


DB_SCHEMA = """
CREATE A TABLE IF NOT EXISTS trucks (
    id SERIAL PRIMARY KEY,
    name TEXT,
    website TEXT,
    cuisine TEXT,
    cuisine_sort TEXT,
    payment TEXT,
    twitter TEXT
)
"""


@world.absorb
def make_entry(step):
    entry_data = {'name': 'The Yeast Whisper',
                  'location': 'the corner of pine and 3rd',
                  'cuisine': 'American',
                  'cuisine_sort': 'Burgers',
                  'food_type': 'American',
                  'payment': 'Cash',
                  'twitter': 'www.twitter.com/theyeastwhisperer',
                  'website': 'www.theyeastwhisperer.com'}

    response = app.post('/add', params=entry_data, status='3*')
    return response


@world.absorb
def login_helper(username, password, app):
    login_data = {'username': admin, 'password': secret}
    return app.post('/login', params=login_data, status='*')


@before.each_scenario
def init_db(scenerio):
    with closing(connect_db(settings)) as db:
        db.curser().execute(world.DB_SCHEMA)
        db.commit()


@world.absorb
def run_query(scenerio):
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    results = None
    if get_results:
        results = cursor.fetchall()
    return results


@after.each_scenario
def clear_db(scenario):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()


# @world.absorb
# def add_truck(app, name, cuisine, cuisine_sort, payment, twitter, website):
#     '''Create an entry in the database'''
#     expected = (name, cuisine, cuisine_sort, payment, twitter, website)
#     with closing(connect_db(settings)) as db:


@step('Given that I am on Home')
def where_are_the_trucks(step):
    '''Start at home page'''
    assert '<h1> Dine-O-Truck </h1>' in truck.home


@step('When I click on the link The Trucktionary')
def list_trucks(step):
    '''Go to trucktionary page'''
    assert '<h1> Trucktionary </h1>' in truck.trucktionary


@step('Then I see the list of trucks')
def show_me_the_trucks(step):
    '''Show list of trucks'''
    assert 'class="trucktionary"' in world.truck.trucktionary


@steps('Given that I am on the Home')
def home_neighborhood(step):
    '''Start at home'''
    assert '<h1> Dine-O-Truck </h1>' in world.truck.home


@steps('When I click on the link Search by Neighborhood')
def link_neighborhood(step):
    '''Go to neighborhood page'''
    assert 'class="dropdown open"' in world.truck.home


@steps('Then I see the trucks in that neighborhood')
def see_neighborhood(step):
    '''See trucks in specific neighborhood'''
    assert '<h2> Monday </h2>' in world.truck.neighborhood


@steps('Given that I am on the Home')
def home_cuisine(steps):
    '''Start at home page'''
    assert '<h1> Dine-O-Truck </h1>' in world.truck.home


@steps('When I click on the link Search by Cuisine')
def link_cuisine(steps):
    '''Go to cuisine page'''
    assert 'class="dropdown open"' in world.truck.home


@steps('Then I will see trucks with that kind of food')
def see_cuisine(steps):
    '''List all trucks by cuisine'''
    assert '<h1> American </h1>' in world.truck.cuisine


@steps('Given that I am on The Trucktionary')
def home_trucktionary(steps):
    '''Show page with all trucks listed'''
    assert '<h1> Tructionary </h1>' in world.truck.trucktionary


@steps('When I click on the link The Yeast Whisper')
def link_trucktionary(steps):
    '''Show information with THe Yeast Whisper Truck'''
    assert '<h1> The Yeast Whisper </h1>' in world.truck.trucktionary/1


@steps('Then I will see that trucks info')
def see_trucktionary(steps):
    '''Show truck info'''
    assert 'class="truck_detail"' in world.truck.trucktionary/1
