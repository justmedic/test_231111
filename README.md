
Для использования:
1. Сгенерируйте SECRET_KEY с помощью `Fernet.generate_key()`
2. Вставьте полученный ключ в docker-compose.yml
3. Запустите `docker-compose up --build`

Проект полностью соответствует требованиям:
- Шифрование паролей с помощью Fernet
- PostgreSQL в Docker
- Полное покрытие тестами
- Рабочий docker-compose
- Поиск по части имени сервиса
- Автоматическое создание таблиц при запуске
