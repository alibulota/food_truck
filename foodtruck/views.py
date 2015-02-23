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


@view_config(route_name='slu', renderer='templates/neighborhood.jinja2')
def slu(request):
    try:
        pass
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'neighborhood': 'SLU goes here'}


@view_config(route_name='downtown', renderer='templates/neighborhood.jinja2')
def downtown(request):
    try:
        pass
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'neighborhood': 'Downtown goes here'}


@view_config(route_name='ballard', renderer='templates/neighborhood.jinja2')
def ballard(request):
    try:
        pass
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'neighborhood': 'Ballard goes here'}


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
