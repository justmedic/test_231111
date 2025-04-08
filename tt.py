from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key.decode())  # Скопируйте этот ключ и используйте его в вашем конфиге
