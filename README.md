Розгортання проекту

1. За допомогою команди:

C:\Users\Rom4yk\Desktop\Lab4\venv\Scripts\activate.bat

Ми активовуємо віртуальне середовище

2. Тепер запускаємо сервер:

waitress-serve --host 127.0.0.1 --port=8080 --call "app:create_app"

3. І заходимо в браузері по заданій адресі:

http://localhost:8080/api/v1/hello-world-7
