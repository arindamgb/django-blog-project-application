# Blog Project using Django 5.0.2

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

# Running this project in Docker
```
git clone https://github.com/arindamgb/django-blog-project-application.git
cd django-blog-project-application/
docker build -t arindamgb/django_blog_project:1.0 .
docker run -itd --name django_blog_project -p 8087:8000 arindamgb/django_blog_project:1.0
```

# Below configs kept for testing purpose
```
DEBUG = True
ALLOWED_HOSTS = ['*']
```

# Check Live Preview
## [Live Demo](https://blogproject.arindamgb.com/)

# Interesting Read about Django Project

I found 2 types of github repositories people mostly use to host their Django projects. They differ in respect of the project file structure as pushed in Github.

Please note, the ***tree*** representations uses generic names.

## First type

* ***Dockerfile*** and ***requirements.txt*** are kept out of the ***Django project directory***, at the ***root*** of the repository.
* ***manage.py*** is ***NOT*** at the ***root*** of the repository.

```
django-my-project-application/		# < github repo
├─ my_project/				# < Django Project root
│  ├─ app/				# < App code
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  ├─ my_project/			# < Django project settings dir
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ wsgi.py
│  ├─ manage.py				# < Django management tool
├─ .gitignore
├─ Dockerfile
├─ README.md
├─ requirements.txt			# < Python module list
```

## Second type

* ***Dockerfile*** and ***requirements.txt*** reside inside ***Django project directory***.
* ***manage.py*** is at the ***root*** of the repository.
* ***Dockerfile***, ***requirements.txt*** and ***manage.py*** is at the same level.
* ***Django project root*** and the ***repository root*** is the same.

```
my_project/				# < github repo + Django Project root
├─ app/					# < App code
│  ├─ apps.py
│  ├─ forms.py
│  ├─ urls.py
│  ├─ views.py
├─ my_project/			        # < Django project settings dir
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
├─ .gitignore
├─ Dockerfile
├─ manage.py			        # < Django management tool
├─ README.md
├─ requirements.txt		        # < Python module list
```

## What I did in this repository

* I combined the both types described above for my reference because the ***Dockerfile*** instructions changes for different structures.
* If you are at the ***repository root***, this is the ***First Type***.
* If you enter the directory ***django_blog_project***, it is the ***Second Type***.

```
django-my-project-application/		# < github repo
├─ my_project/				# < Django Project root
│  ├─ app/				# < App code
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  ├─ my_project/			# < Django project settings dir
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ wsgi.py
│  ├─ Dockerfile
│  ├─ manage.py				# < Django management tool
│  ├─ requirements.txt		        # < Python module list
├─ .gitignore
├─ Dockerfile
├─ README.md
├─ requirements.txt
```

I put this here for my future reference. Thank you!
