from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

# Specify the db with a relative path.
url = 'sqlite:///test.db'

# Specify the db with an absolute path.
# url = 'sqlite:////data/test.db'

engine = create_engine(
    url=url,
    echo=False,
    connect_args={
        'check_same_thread': False
    }
)

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), unique=True, index=True)
    birthday = Column(Date)
    is_active = Column(Boolean, default=True)
    create_time = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"User(name={self.name}, is_active={self.is_active}, create_time={self.create_time})"

Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)
