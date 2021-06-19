from pony.orm import *

db = Database()


credentials = {
    'username': "admin",
    'password': "admin",
    'host': "roach1",
    'database': "test"
}


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)


def connect_to_db():
    db.bind(provider='cockroach', user=credentials['username'], password=credentials['password'], host=credentials['host'],
            database=credentials['database'])
    db.generate_mapping(create_tables=True)
    db.set_sql_debug(True)


if __name__ == '__main__':
    connect_to_db()
    # print("Hello 2")
