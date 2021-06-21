from pony.orm import *

db = Database()

credentials = {
    'username': "admin",
    'password': "admin",
    'host': "roach1",
    'database': "defaultdb"
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
    print(credentials['host'])
    db.bind(provider='cockroach', user=credentials['username'], password=credentials['password'],
            host=credentials['host'], database=credentials['database'], sslmode='disable', port=26257)
    try:
        db.generate_mapping(create_tables=True)
        sql_debug(True)
    except Exception as err:
        print(err)
        print('didnt work')

@db_session
def create_entities():
    p1 = Person(name='John', age=20)
    p2 = Person(name='Mary', age=22)
    p3 = Person(name='Bob', age=30)
    c1 = Car(make='Toyota', model='Prius', owner=p2)
    c2 = Car(make='Ford', model='Explorer', owner=p3)
    # there is no need to call commit() here -
    # Pony does it automatically on leaving the db_session scope

    print('created data in db')

@db_session
def query_example():
    query = select(p for p in Person 
            if p.age > 20)
    for q in query:
        print(q.name)


if __name__ == '__main__':
    connect_to_db()
    create_entities()
    query_example()
