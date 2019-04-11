from app import db, flask_bcrypt

class Person(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    national_id = db.Column(db.Integer, unique=True)
    phone_number = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    residence = db.Column(db.Boolean, nullable=False, default=False)
    land_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    land = db.relationship("Person", uselist=False, remote_side=[id])
    land_lord = db.Column(db.Boolean, nullable=True, default=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'),
         default=1)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(100), nullable=True)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Person '{}'>".format(self.first_name)

class County(db.Model):
    """ Area model for storing details of specific County"""
    __tablename__ = "county"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    constituencies = db.relationship('Constituency', backref='county', lazy=True)

    def __repr__(self):
        return "<County '{}'>".format(self.name)

class Constituency(db.Model):
    """ Area model for storing details of an constituency instance in a county"""
    __tablename__ = "constituency"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'))
    wards = db.relationship("Ward")

    def __repr__(self):
        return "<Constituency '{}'>".format(self.name)

class Ward(db.Model):
    """ Area model for storing details of an ward instance in a constituency"""
    __tablename__ = "ward"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id'))
    areas = db.relationship("Area")

    def __repr__(self):
        return "<Ward '{}'>".format(self.name)

class Area(db.Model):
    """ Area model for storing details of an area instance in a ward"""
    __tablename__ = "area"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    Lattitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    ward_id = db.Column(db.Integer, db.ForeignKey('ward.id'))
    people = db.relationship('Person', backref='area', lazy=True)

    def __repr__(self):
        return "<Area '{}'>".format(self.name)
