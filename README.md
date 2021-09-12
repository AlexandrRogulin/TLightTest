# TLightTest
Решение ТЗ для https://cpa.tl/

Для запуска проекта на своем компьютере скопируйте данный проект на ПК в нужную директоию.

Затем установите виртуальное окружение.
```
python -m venv venv
```
Запуск виртуального окружения на Windows выполняется командой:
```
source venv/Scripts/activate
```
Перейдите в папку <b>myproject</b> и выполните установку необходимых пакетов, сохраненных в файле <b>requirements.txt</b>
```
cd myproject
pip install -r requirements.txt
```
Выполните миграции. При необходимости создайте суперпользователя
```
python manage.py migrate
python manage.py createsuperuser
```
Заполните базу данных информацией из файлов <b>posts_customuser.json</b> и <b>posts_post.json</b>
```
./manage.py loaddata posts_customuser.json
./manage.py loaddata posts_post.json
```
Запустите сервер командой
```
python manage.py runserver
```
На открывшемся сайте будет представлена таблица с результами: 
- Имя пользователя
- Тема поста
- Текст поста

Для быстрого поиска текста имеется форма, куда можно ввести интересующую информацию.

Результаты поиска будут отображаться в новой таблице.

<a target="_blank" href="http://g.recordit.co/zU8HsOzRvr.gif"><img src="preview.gif" /></a>
