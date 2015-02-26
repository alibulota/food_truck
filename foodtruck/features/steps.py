from lettuce import *


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
                  'cuisine': 'American'
                  'cuisine_sort': 'Burgers',
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


@world.absorb
def add_truck(app, name, cuisine, cuisine_sort, payment, twitter, website):
    '''Create an entry in the database'''
    expected = (name, cuisine, cuisine_sort, payment, twitter, website)
    with closing(connect_db(settings)) as db:

# con_string =  "dbname='food_truck' user='aabulota'"

# con = psycopg2.connect(con_string)
# cursor = con.cursor()

# try:
#     con = psycopg2.connect(con_string)
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS trucks")


@step('Dino homepage')
def get_home_page(step):
    response = world.app.get('/')
    assert response.status_code == 200


@step('Given that I am on Home')
def where_are_the_trucks(step):
    world.food = links(truck.home)


@step('When I click on the link The Trucktionary')
def list_trucks(step):
    
    world.food = string(trucks)


@step('Then I see the list of trucks')
def show_me_the_trucks(step):
    world.food = trucks(links)
