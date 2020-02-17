NEW: 
*	Vodeo 08: The font does not show as the tutorial font ?
*	ORM Videos 14, 15


Copied from ReadMe.txt
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
(Blogger) e:\_B\MD_BLOG\Blogger\src > cd ..
(Blogger) e:\_B\MD_BLOG\Blogger> git add .
(Blogger) e:\_B\MD_BLOG\Blogger > git commit -m "New project & two apps created"
	[ Go yo gthub website, signin, create new project, Follow 03, (06:30)]
(Blogger) e:\_B\MD_BLOG\Blogger >git remote add origin https://github.com/mohdfayed/blog-django-ar.git 
(Blogger) e:\_B\MD_BLOG\Blogger > git remote -v
	origin  https://github.com/mohdfayed/blog-django-ar.git (fetch)
	origin  https://github.com/mohdfayed/blog-django-ar.git (push)
(Blogger) e:\_B\MD_BLOG\Blogger > git push -u origin master
	[ Refresh github web page ]
	[ my repository: https://github.com/mohdfayed/blog-django-ar ]
	[ aabouissa's: https://github.com/aabouissa/blog-django-ar ]
	[ fork to take a copy to ; !!! ]
	[ 3 commits, to see the 3 commit tags you added ]
	 NB. : [ Enviroments is a wrong spelling, should be Environments ]
[ Run your project ] 
(Blogger) e:\_B\MD_BLOG\Blogger > cd src
(Blogger) e:\_B\MD_BLOG\Blogger\src > manage.py migrate
(Blogger) e:\_B\MD_BLOG\Blogger\src > manage.py createsuperuser
	[ admin, admin@admin.com, <my_default_admin_password> ]
(Blogger) e:\_B\MD_BLOG\Blogger\src > manage.py runserver
	[ ctrl+c to stop the server, then Run VSCode ]
(Blogger) e:\_B\MD_BLOG\Blogger\src > cd ..
(Blogger) e:\_B\MD_BLOG\Blogger> code . 
	Add the 2 apps to INSTALLED_APPS
	Add and commit to github through VSCode... <details !>
	Create Project wide static folder:
		Inside src create static folder, inside it create css, js, images, fonts folders
		At the bottom of settings.py, after 
		STATIC_URL = '/static/'
		add:
		STATICFILES_DIRS = [
			os.path.join(BASE_DIR, "static"),
			'E:\_B\MF_BLOG\Blogger\src\static', # path of static folders
			]
STATIC FILES:
A: Static files serves all apps in the project:
*	Create the template folders
*	Create home function in blog/views.py
*	Create blog/urls.py, fill it,
*	Update scr/urls.py
*	Create blog/templates/blog/index.html
*	Create static/CSS/main.css
*	Run the project.
A: Static files serves only blog app:
*	Move static folder to blog app (blog/static)
*	Create static/blog/ and move folders (css, js, fonts and images) to it.
*	COMMENT the STATICFOLDER_DIRS at bottom of settings.py
*	change reference of main.css in index file to read:
	<link rel="stylesheet" href="{% static 'blog/CSS/main.css' %}">
	instead of:
	<link rel="stylesheet" href="{% static 'CSS/main.css' %}">
*	Run the project.... it is ok.. Yesssss


(Blogger) e:\_B\MD_BLOG\Blogger\src > 
(Blogger) e:\_B\MD_BLOG\Blogger\src > 


(Blogger) e:\_B\MD_BLOG\Blogger >
(Blogger) e:\_B\MD_BLOG\Blogger > 





