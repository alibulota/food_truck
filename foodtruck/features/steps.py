from lettuce import *


TEST_DSN = 'dbname=test_food_truck user=jakeanderson'
settings = {'db': TEST_DSN}
INPUT_BTN = '<input type="submit" name="add" value="Truck It!"/>'


@world.absorb
def make_entry(step):
    entry_data = {'name': 'The Yeast Whisper',
                  'location': 'the corner of pine and 3rd',
                  'food_type': 'American',
                  'payment': 'Cash',
                  'twitter': 'www.twitter.com/theyeastwhisperer',
                  'website': 'www.theyeastwhisperer.com'}

    response = app.post('/add', params=entry_data, status='3*')
    return response


@step('Journal homepage')
def get_home_page(step):
    response = world.app.get('/')
    assert response.status_code == 200


@step('I know where I am and I want to know where the food is coming from')
def where_are_the_trucks(step):
    word.food = links(truck.trucktionary)


@step('I want a certain kind o food')
def what_kind_of_genres(step):
    world.food = string(trucks)


@step('I want to contact the food truck')
def show_me_the_trucks(step):
    response = world.app.get('trucktionary/1')
    assert response.status_code == 200
    assert 'The Yeast Whisper' in response.body
