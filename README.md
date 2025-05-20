# Yatube API Final

Проект — API для социальной сети блогеров «Yatube». 

**Функционал:**
- Регистрация и аутентификация (JWT).
- Создание, чтение, обновление и удаление (CRUD) постов.
- Комментирование и лайки.
- Подписки на авторов.

**Установка и запуск:**
`py``bash
git clone https://github.com/ваш_ник/api_final_yatube.git
cd api_final_yatube/api_final_yatube
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
python manage.py migrate
pytest
