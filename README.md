Urparser - веб приложение написанное на Django, которое принимает на вход url и ищет определяет количество уникальный и вложенных тегов(смотреть пример)

#Подготовка

1.pip install pipenv

2.Запускаем скрипт install_rabbit_mq.sh

3. pipenv shell

4. pipenv sync 

5. pipenv install celery

#конфигирируем бд

6. sudo -u postgres psql

7. CREATE DATABASE myproject;

8. CREATE USER myprojectuser WITH PASSWORD 'password';

9.  

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';

ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';

ALTER ROLE myprojectuser SET timezone TO 'UTC';

10. GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

11. \q

#Запуск


1. sh run_rabbit.sh (запускаем rabbitmq)

2. python manage.py runserver

3. sh run_celery.sh (запускаем celery)

#Описание endpount 

чтобы запросить 


| Methods        | ENPOINTS       | RESPONSE  |
| ------------- |:-------------:| -----:|
| GET           | http://127.0.0.1:8000/admin/api/scan/url=YOUR_URL | task_id |
| GET      | http://127.0.0.1:8000/admin/api/results/id=task_id      |  количество уникальных и вложенных html тегов на странице |


#Примеры


![изображение](https://user-images.githubusercontent.com/41837845/131410286-c566209b-a701-40e6-a179-1de86bc0e176.png)

![изображение](https://user-images.githubusercontent.com/41837845/131410366-3d92ed84-03a2-4c77-8a21-0c9c778d155f.png)







  
