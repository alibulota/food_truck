from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import (
    DBSession,
    Base,
    )
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['sqlalchemy.url'] = os.environ.get(
        'DATABASE_URL', 'postgresql://jwarren:@localhost:5432/food_truck')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('trucks', '/tructionary')
    config.add_route('truck_detail', '/tructionary/{name}')
    config.add_route('slu', '/slu')
    config.add_route('downtown', '/downtown')
    config.add_route('ballard', '/ballard')
    # will need to add routes for cuisines
    config.scan()
    return config.make_wsgi_app()
