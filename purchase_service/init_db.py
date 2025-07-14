from db.database import Base, engine
import models

def init():
    print("Creating purchases table...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()