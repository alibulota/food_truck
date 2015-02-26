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


@world.absorb
def login_helper(username, password, app):
    login_data = {'username': admin, 'password': secret}
    return app.post('/login', params=login_data, status='*')


@world.absorb
def init_db(scenerio):
    with closing(connect_db(settings)) as bd:
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


@world.absorb
def clear_db(scenario):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()


@world.absorb
def j

# @step('Dino homepage')
# def get_home_page(step):
#     response = world.app.get('/')
#     assert response.status_code == 200


# @step('I want to know where the food is coming from')
# def where_are_the_trucks(step):
#     word.food = links(truck.trucktionary)


# @step('I want a certain kind of food')
# def what_kind_of_genres(step):
#     world.food = string(trucks)


# @step('I want to contact the food truck')
# def show_me_the_trucks(step):
#     world.food = trucks(links)
