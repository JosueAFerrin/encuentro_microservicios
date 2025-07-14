from db.database import engine
from models.ticket import Base

def init():
    print("Creating tickets table...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()