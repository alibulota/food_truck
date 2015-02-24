from lettuce import *


TEST_DSN = 'dbname=test_food_truck user=jakealope'
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


@step('I am hungry and I want food')
def fine_the_truck(step):
    world.food = string(trucks.links)


@step('I know where I am and I want to know where the food is coming from')
def where_are_the_trucks(step):
    word.food = links(truck.links)


@step('I want a certain kind o food')
def what_kind_of_genres(step):
    world.food = string(trucks)

@step('I want to contact the food truck')
def show_me_the_trucks(step):
    world.food = trucks(links)
