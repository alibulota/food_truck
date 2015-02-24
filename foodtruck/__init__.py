from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import (
    DBSession,
    Base,
    )
import os
from pyramid.session import SignedCookieSessionFactory
from cryptacular.bcrypt import BCRYPTPasswordManager
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['sqlalchemy.url'] = os.environ.get(
        'DATABASE_URL', 'postgresql://jwarren:@localhost:5432/food_truck')

    manager = BCRYPTPasswordManager()
    settings['auth.username'] = os.environ.get('AUTH_USERNAME', 'admin')
    settings['auth.password'] = os.environ.get(
        'AUTH_PASSWORD', manager.encode('secret')
    )
    secret = os.environ.get('JOURNAL_SESSION_SECRET', 'itsaseekrit')
    session_factory = SignedCookieSessionFactory(secret)
    auth_secret = os.environ.get('JOURNAL_AUTH_SECRET', 'anotherseekrit')
    config = Configurator(
        settings=settings,
        session_factory=session_factory,
        authentication_policy=AuthTktAuthenticationPolicy(
            secret=auth_secret,
            hashalg='sha512',
            debug=True
        ),
        authorization_policy=ACLAuthorizationPolicy(),
    )

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # FRONT END #
    config.add_route('home', '/')
    config.add_route('trucks', '/tructionary')
    config.add_route('truck_detail', '/tructionary/{name}')
    config.add_route('neighborhood', '/neighborhood/{neighborhood:(slu|downtown|ballard)}')
    config.add_route('cuisine', '/cuisine/{cuisine}')
    # ADMIN #
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('add', '/admin/add')
    config.add_route('admin', '/admin')
    config.scan()
    return config.make_wsgi_app()
