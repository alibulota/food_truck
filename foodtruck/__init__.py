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
    # FRONT END #
    config.add_route('home', '/')
    config.add_route('trucks', '/tructionary')
    config.add_route('truck_detail', '/tructionary/{name}')
    config.add_route('neighborhood', '/neighborhood/{neighborhood}')
    config.add_route('cuisine', '/cuisine/{cuisine}')
    # ADMIN #
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
