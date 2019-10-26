### Описание

 Асинхронный сервер реализован с помощью фреймворка sanic. Имеет один endpoint **/get_topic**. Так как по условию мы не используем никакой базы данных я придумал немного тем и соответствующие им фразы.  Данные (небольшой словарик) лежат в файле data.py.


### Установка и тестирование

- для уcтановки пакета необходимо клонировать репозиторий в свою систему - git clone

- для запуска сервера выполняем либо **python -m topic_detector.server** либо **run_sanic**. Сервер стартует на 8000 порту.

- для запуска тестов выполняем команду **python setup.py test**