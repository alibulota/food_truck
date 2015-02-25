from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden, HTTPInternalServerError
from sqlalchemy.exc import DBAPIError
from pyramid.security import remember, forget
from cryptacular.bcrypt import BCRYPTPasswordManager
from .models import (
    DBSession,
    Truck,
    Locations,
    )


cuisine_dict = {
    'american': 'American',
    'asian': 'Asian',
    'bbq': 'BBQ',
    'intl': 'International',
    'medi': 'Mediterranean',
    'mex': 'Mexican',
    'sweets': 'Sweets'
}

neighborhood_dict = {
    'slu': 'South Lake Union',
    'ballard': 'Ballard',
    'downtown': 'Downtown',
}


@view_config(route_name='home', renderer='templates/index.jinja2')
def index(request):
    try:
        trucks = Truck.all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'trucks': trucks}


@view_config(route_name='trucks', renderer='templates/tructionary.jinja2')
def tructionary(request):
    try:
        trucks = Truck.all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'trucks': trucks}


@view_config(route_name='truck_detail', renderer='templates/truck_detail.jinja2')
def truck_detail(request):
    try:
        id = request.matchdict.get('id', None)
        truck = Truck.by_id(id)
    except DBAPIError:
        return HTTPInternalServerError
    return {'truck': truck}


@view_config(route_name='neighborhood', renderer='templates/neighborhood.jinja2')
def neighborhood(request):
    neighborhood_ = request.matchdict.get('neighborhood', None)
    neighborhood_name = neighborhood_dict[neighborhood_]
    return {'neighborhood_name': neighborhood_name}


@view_config(route_name='cuisine', renderer='templates/cuisine.jinja2')
def cuisine(request):
    cuisine_ = request.matchdict.get('cuisine', None)
    cuisine_type = cuisine_dict[cuisine_]
    cuisine = Truck.by_cuisine(cuisine_type)
    return {'cuisine': cuisine, 'cuisine_type': cuisine_type}


####################
# LOG IN / LOG OUT #
####################
@view_config(route_name='login', renderer="templates/login.jinja2")
def login(request):
    """authenticate a user by username/password"""
    username = request.params.get('username', '')
    error = ''
    if request.method == 'POST':
        error = "Login Failed"
        authenticated = False
        try:
            authenticated = do_login(request)
        except ValueError as e:
            error = str(e)
        if authenticated:
            headers = remember(request, username)
            return HTTPFound(request.route_url('admin'), headers=headers)
    return {'error': error, 'username': username}


def do_login(request):
    username = request.params.get('username', None)
    password = request.params.get('password', None)
    if not (username and password):
        raise ValueError('both username and password are required')
    settings = request.registry.settings
    manager = BCRYPTPasswordManager()
    if username == settings.get('auth.username', ''):
        hashed = settings.get('auth.password', '')
        return manager.check(hashed, password)


@view_config(route_name='logout')
def logout(request):
    """remove authentication from a session"""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)


#########
# ADMIN #
#########
@view_config(route_name='add', request_method='POST')
def add_truck(request):
    if request.authenticated_userid:
        try:
            Truck.add_truck(request)
            return HTTPFound(request.route_url('admin'))
        except DBAPIError:
            return HTTPInternalServerError
    else:
        return HTTPForbidden()


@view_config(route_name='add_location', request_method='POST')
def add_location(request):
    if request.authenticated_userid:
        try:
            Locations.add_location(request)
            return HTTPFound(request.route_url('admin'))
        except DBAPIError:
            return HTTPInternalServerError
    else:
        return HTTPForbidden()


@view_config(route_name='admin', renderer='templates/admin.jinja2')
def admin(request):
    if request.authenticated_userid:
        try:
            trucks = Truck.all()
        except DBAPIError:
            return HTTPInternalServerError
        return {'trucks': trucks}
    else:
        return HTTPForbidden()


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit(request):
    if request.authenticated_userid:
        if request.method == 'GET':
            try:
                id = request.matchdict.get('id', None)
                truck = Truck.by_id(id)
            except DBAPIError:
                return HTTPInternalServerError
            return {'truck': truck}
        elif request.method == 'POST':
            try:
                Truck.edit_truck(request)
            except DBAPIError:
                return HTTPInternalServerError
            return HTTPFound(request.route_url('admin'))
    else:
        return HTTPForbidden()


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_FoodTruck_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
