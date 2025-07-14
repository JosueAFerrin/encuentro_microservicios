from db.database import Base, engine
import models

def init():
    print("Creating events table...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()