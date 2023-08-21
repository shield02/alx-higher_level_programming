#!/usr/bin/python3
"""create the state “California” with the city “San Francisco”
hbtn_0e_100_usa database"""

if __name__ == "__main__":

    import sys
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:\
                           {sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add_all([new, new_city])
    session.commit()
    session.close()
