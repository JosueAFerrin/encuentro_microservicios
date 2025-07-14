from db.database import Base, engine
import models

def init():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()