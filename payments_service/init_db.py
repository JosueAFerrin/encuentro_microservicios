from db.database import Base, engine
from models import Payment

def init():
    print("Creating payments table...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
