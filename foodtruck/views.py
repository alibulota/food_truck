from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Truck,
    )


@view_config(route_name='home', renderer='templates/index.jinja2')
def index(request):
    try:
        pass
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'': ''}


@view_config(route_name='trucks', renderer='templates/tructionary.jinja2')
def tructionary(request):
    try:
        pass
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'': ''}


@view_config(route_name='neighborhood', renderer='templates/neighborhood.jinja2')
def neighborhood(request):
    neighborhood = request.matchdict.get('neighborhood', None)
    return {'neighborhood': neighborhood}


@view_config(route_name='cuisine', renderer='templates/cuisine.jinja2')
def cuisine(request):
    cuisine = request.matchdict.get('cuisine', None)
    return {'cuisine': cuisine}


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
            return HTTPFound(request.route_url('home'), headers=headers)
    return {'error': error, 'username': username}


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
