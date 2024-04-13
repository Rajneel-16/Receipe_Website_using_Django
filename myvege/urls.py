from django.contrib import admin
from django.urls import path,include
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('receipes/',receipes,name='receipes'),

    path('',receipes,name='receipes'),
    path('delete-receipe/<id>/',delete_receipe,name='delete_receipe'),
    path('update-receipe/<id>/',update_receipe,name='update_receipe'),

    path('login',login_page,name="login_page"),
    path('register',register_page,name="register_page"),
    path('logout',logout_page,name="logout_page"),        
    # path('contacts/',contacts,name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)