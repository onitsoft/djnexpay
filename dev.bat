@echo on

set DJANGO_SETTINGS_MODULE=djnexpay.settings_dev

call C:\Users\wuelfhis.asuaje\Documents\GitHub\venv3\Scripts\activate.bat

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate 
python manage.py loaddata core\fixtures\01_bank.json 
python manage.py loaddata core\fixtures\02_parameter.json 
python manage.py runserver