#!/usr/bin/python3
"""
script that adds the State object Louisiana to the database hbtn_0e_6_usa
"""


import MySQLdb
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State
from model_state import Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    instance = session.query(State).filter(State.name == "Louisiana").first()
    if instance is not None:
        print("{}".format(instance.id)
    else:
        print("Not found")

    session.close()
