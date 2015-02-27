from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    Time,
    ForeignKey,
    )
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
    locations = relationship('Locations', backref='truck')
    cuisine = Column(Text)
    payment = Column(Text)
    twitter = Column(Text)
    website = Column(Text)
    cuisine_sort = Column(Text)

    @classmethod
    def all(cls):
        return DBSession.query(cls).order_by(cls.name).all()

    @classmethod
    def by_id(cls, id):
        return DBSession.query(cls).filter(cls.id == id).one()

    @classmethod
    def by_cuisine(cls, cuisine_sort):
        return DBSession.query(cls).filter(
            cls.cuisine_sort == cuisine_sort).order_by(cls.name).all()

    @classmethod
    def add_truck(cls, request):
        name = request.params.get('name', None)
        cuisine = request.params.get('cuisine', None)
        payment = request.params.get('payment', None)
        twitter = request.params.get('twitter', None)
        website = request.params.get('website', None)
        cuisine_sort = request.params.get('cuisine_sort', None)
        new_entry = cls(name=name, cuisine=cuisine, payment=payment,
                        twitter=twitter, website=website,
                        cuisine_sort=cuisine_sort)
        DBSession.add(new_entry)

    @classmethod
    def edit_truck(cls, request):
        id = request.matchdict.get('id', None)
        name = request.params.get('name', None)
        cuisine = request.params.get('cuisine', None)
        payment = request.params.get('payment', None)
        twitter = request.params.get('twitter', None)
        website = request.params.get('website', None)
        cuisine_sort = request.params.get('cuisine_sort', None)
        DBSession.query(cls).filter(cls.id == id).update({
            "name": name,
            "cuisine": cuisine,
            "payment": payment,
            "twitter": twitter,
            "website": website,
            "cuisine_sort": cuisine_sort
            })

    @classmethod
    def del_truck(cls, request):
        id = request.matchdict.get('id', None)
        removed_truck = DBSession.query(cls).filter(cls.id == id).one()
        DBSession.delete(removed_truck)


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

    @classmethod
    def add_location(cls, request):
        truck_id = request.matchdict.get('id', None)
        day = request.params.get('day', None)
        start_time = request.params.get('start_time', None)
        end_time = request.params.get('end_time', None)
        address = request.params.get('address', None)
        neighborhood = request.params.get('neighborhood', None)
        new_location = cls(truck_id=truck_id, day=day, start_time=start_time,
                           end_time=end_time, address=address,
                           neighborhood=neighborhood)
        DBSession.add(new_location)

    @classmethod
    def del_location(cls, request):
        id = request.matchdict.get('id', None)
        old_location = DBSession.query(cls).filter(cls.id == id).one()
        DBSession.delete(old_location)

    @classmethod
    def by_neighborhood(cls, neighborhood):
        return DBSession.query(cls).filter(
            cls.neighborhood == neighborhood).order_by(cls.day).all()


Index('truck_index', Truck.name, unique=True, mysql_length=255)
