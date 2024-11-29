# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то не сможете его запустить, так как у вас нет доступа к БД, но вы можете свободно использовать код вёрстки, или посмотреть, как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропусков сотрудников нашего банка.

### Как установить

Переменные окружения: 

DB_ENGINE - необходимый драйвер. 

DB_HOST, DB_PORT - адрес хоста и порт для подключения

DB_NAME - имя базы данных

DB_PASSWORD, DB_USER - пароль и логин для доступа.

DB_SECRETKEY - ключ для шифровки паролей

ALLOWED_HOSTS - настройка разрешённых доменов

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).