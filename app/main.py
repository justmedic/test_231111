from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import security
from app.db.models import PasswordEntry, get_db


class PasswordCreate(BaseModel):
    password: str


class PasswordResponse(PasswordCreate):
    service_name: str

    class Config:
        orm_mode = True


app = FastAPI()


@app.post("/password/{service_name}", response_model=PasswordResponse)
def create_password(
    service_name: str, password: PasswordCreate, db: Annotated[Session, Depends(get_db)]
):
    encrypted = security.encrypt_password(password.password)
    db_entry = PasswordEntry(service_name=service_name, encrypted_password=encrypted)
    db.merge(db_entry)
    db.commit()
    return {"service_name": service_name, "password": password.password}


@app.get("/password/{service_name}", response_model=PasswordResponse)
def get_password(service_name: str, db: Annotated[Session, Depends(get_db)]):
    entry = db.get(PasswordEntry, service_name)
    if not entry:
        raise HTTPException(status_code=404)
    return {
        "service_name": service_name,
        "password": security.decrypt_password(entry.encrypted_password),
    }


@app.get("/password/", response_model=list[PasswordResponse])
def search_passwords(service_name: str, db: Annotated[Session, Depends(get_db)]):
    entries = (
        db.query(PasswordEntry).filter(PasswordEntry.service_name.ilike(f"%{service_name}%")).all()
    )
    return [
        {
            "service_name": e.service_name,
            "password": security.decrypt_password(e.encrypted_password),
        }
        for e in entries
    ]
