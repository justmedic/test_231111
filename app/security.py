from cryptography.fernet import Fernet

from app.settings import settings

fernet = Fernet(settings.secret_key.encode())


def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(encrypted: str) -> str:
    return fernet.decrypt(encrypted.encode()).decode()
