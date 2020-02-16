> md Blogger
> cd Blogger
> git init
> python -m virtualenv .
> git status
> git add .
> git commit -m "Installed Virtual Enviroment"
> .\Scripts\activate
(Blogger) > pip install django
(Blogger) > pip freeze
	asgiref==3.2.3
	Django==3.0.3
	pytz==2019.3
	sqlparse==0.3.0
(Blogger) > git status
(Blogger) > git add .
(Blogger) > git commit -m "Installed Django 3.0.3"
(Blogger) > md src && cd src
	[ Create the project ]
(Blogger) > django-admin startproject my_blog .
	[ Create the applications ]
(Blogger) e:\_B\MD_BLOG\Blogger\src > manage.py startapp blog
(Blogger) e:\_B\MD_BLOG\Blogger\src > manage.py startapp user
(Blogger) e:\_B\MD_BLOG\Blogger\src > 
(Blogger) e:\_B\MD_BLOG\Blogger\src > 







