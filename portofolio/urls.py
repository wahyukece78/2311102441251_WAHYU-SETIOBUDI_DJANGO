from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from .views import home, about, contact, detail_artikel
from portofolio.authentikasi import akun_login, akun_registrasi, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('artikel/<slug:slug>/', detail_artikel, name="detail_artikel"),
    
    path('dashboard/', include("berita.urls")),
    path('authentikasi/', akun_login, name="akun_login"),
    path('authentikasi/registrasi/', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/login', user_logout, name="user_logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)