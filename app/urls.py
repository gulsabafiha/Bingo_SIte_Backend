from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('team/',views.team,name='team'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('price/',views.price,name='price'),
    path('blog/',views.blog,name='blog'),
    path('error-page/',views.error_page,name='errorpage'),
    path('single-post/',views.singlepost,name='singlepost'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'), 
]
urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
