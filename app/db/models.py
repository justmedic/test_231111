from sqlalchemy import Column, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.settings import settings

Base = declarative_base()
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PasswordEntry(Base):
    __tablename__ = "passwords"
    service_name = Column(String(255), primary_key=True)
    encrypted_password = Column(Text, nullable=False)


Base.metadata.create_all(bind=engine)
