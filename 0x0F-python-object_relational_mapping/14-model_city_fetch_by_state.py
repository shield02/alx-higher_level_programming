#!/usr/bin/python3
"""print all City objects from hbtn_0e_14_usa database"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:\
                           {sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session.query(State, City)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
