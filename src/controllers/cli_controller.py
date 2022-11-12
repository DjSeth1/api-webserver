from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.appointment import Appointment
from models.barber import Barber
from models.service import Service


db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    '''Creates all tables via the models.'''
    db.create_all()
    print('Tables Created!')

@db_commands.cli.command('drop')
def drop_db():
    '''Drops all tables from database via the models'''
    db.drop_all()
    print('Tables Dropped!')

@db_commands.cli.command('seed')
def seed_db():
    '''Seeds the database tables with relevant information declared in the models'''
    services = [
        Service(
            type = 'Hair',
            price = 30
        ),
        Service(
            type = 'Hair and Beard',
            price = 45
        )

    ]

    db.session.add_all(services)
    db.session.commit()

    users = [
        User(
            f_name = 'Jack',
            l_name = 'Delany',
            email = 'delany.jack@gmail.com',
            password = bcrypt.generate_password_hash('dogsandcats').decode('utf-8'),
            phone = '021746435',
            is_admin = False,

        ),

        User(
            f_name = 'Aditya',
            l_name = 'Arora',
            email = 'aditya@gmail.com',
            password = bcrypt.generate_password_hash('dogsandcats1').decode('utf-8'),
            phone = '0245322134',
            is_admin = False,


        )

    ]

    db.session.add_all(users)
    db.session.commit()

    barbers = [
        Barber(
            f_name = "Byron",
            l_name = "Hogan",
            email = 'byronhogan@gmail.com',
            password = bcrypt.generate_password_hash('dogsandcats2').decode('utf-8'),
            phone = '0214253543', 
            is_admin = True,
            time_slots = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00'],

        )
    ]

    db.session.add_all(barbers)
    db.session.commit()

    appointments = [
        Appointment(
            user = users[1],
            service = services[1],
            barber = barbers[0],
            time = '10:00'
        )
    ]

    db.session.add_all(appointments)
    db.session.commit()
    print('Tables Seeded!')



