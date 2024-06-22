from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('news/', views.main, name='main'),
    path('news/<int:id>/', views.detail_news, name='detail_news')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
