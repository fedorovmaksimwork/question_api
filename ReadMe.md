## Описание
Данный проект представляет собой *API-сервис для вопросов и ответов*, реализованный с помощью *Django Rest Framework*.

## Установка
### 1. Клонируйте репозиторий:

	git clone https://github.com/fedorovmaksimwork/question_api

### 2. Перейдите в директорию с проектом:

	cd question

### 3. Установите зависимости:

`pip install -r requirements.txt`

### 4. Настройте переменные окружения в файле .env:

	SECRET_KEY=your_secret_key  
	DB_NAME=your_db_name  
	DB_USER=your_db_user  
	DB_PASSWORD=your_db_password  

## Запуск
### 1. Соберите и запустите контейнеры:

	docker-compose up --build
### 2. Выполните миграции:

	docker-compose exec django python manage.py migrate

### 3. Перейдите на один из доступных URL:

|Метод |                      URL                     |              Функционал             |
|:----:|:--------------------------------------------:|:-----------------------------------:|
|GET   | http://localhost:8000/questions/             |  Список всех вопросов               |
|GET   | http://localhost:8000/questions/{id}         |  Поучить вопрос и все ответы на него|
|GET   | http://localhost:8000/answers/{id}           |  Поучить конкретный ответ           |
|POST  | http://localhost:8000/questions/             |  Создать новый вопрос               |
|POST  | http://localhost:8000/questions/{id}/answers/|  Добавить ответ к вопросу           |
|DELETE| http://localhost:8000/answers/{id}           |  Удалить вопрос (вместе с ответами) |
|DELETE| http://localhost:8000/questions/{id}         |  Удалить ответ                      |

## Тесты
### Для запуска тестов выполните команду:
	docker-compose run --rm django pytest

## Остановка
### Для остановки и удаления контейнеров выполните:

	docker-compose down

