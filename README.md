# Blog Project using Django 5.0.2

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

## How to run this project with Docker
```sh
git clone https://github.com/arindamgb/django-blog-project-application.git
cd django-blog-project-application/
docker build -t arindamgb/django_blog_project:1.0 .
docker run -itd --name django_blog_project -p 8087:8000 arindamgb/django_blog_project:1.0
```

Pleae note that, below configs are left open for testing purpose:
`DEBUG = True`
`ALLOWED_HOSTS = ['*']`

## [Live Demo](https://blogproject.arindamgb.com/)
