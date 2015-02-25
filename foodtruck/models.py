from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    Time,
    ForeignKey,
    )
# from webhelpers.text import urlify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Truck(Base):
    __tablename__ = 'trucks'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    locations = relationship('Locations')
    cuisine = Column(Text)
    payment = Column(Text)
    twitter = Column(Text)
    website = Column(Text)

    @classmethod
    def all(cls):
        return DBSession.query(cls).order_by(cls.name).all()

    @classmethod
    def by_id(cls, id):
        return DBSession.query(cls).filter(cls.id == id).one()

    @classmethod
    def by_cuisine(cls, cuisine):
        return DBSession.query(cls).filter(cls.cuisine == cuisine).order_by(cls.name).all()

    @classmethod
    def add_truck(cls, request):
        name = request.params.get('name', None)
        cuisine = request.params.get('cuisine', None)
        payment = request.params.get('payment', None)
        twitter = request.params.get('twitter', None)
        website = request.params.get('website', None)
        new_entry = cls(name=name, cuisine=cuisine, payment=payment,
                        twitter=twitter, website=website)
        DBSession.add(new_entry)

    @classmethod
    def edit_truck(cls, request):
        id = request.matchdict.get('id', None)
        name = request.params.get('name', None)
        cuisine = request.params.get('cuisine', None)
        payment = request.params.get('payment', None)
        twitter = request.params.get('twitter', None)
        website = request.params.get('website', None)
        DBSession.query(cls).filter(cls.id == id).update({
            "name": name,
            "cuisine": cuisine,
            "payment": payment,
            "twitter": twitter,
            "website": website
            })


class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    truck_id = Column(Integer, ForeignKey('trucks.id'))
    day = Column(Text)
    start_time = Column(Time)
    end_time = Column(Time)
    address = Column(Text)
    neighborhood = Column(Text)

    def __str__(self):
        return self.neighborhood

    def __repr__(self):
        return self.neighborhood


Index('truck_index', Truck.name, unique=True, mysql_length=255)
