from django.urls import path, include
from Nature_Web_Blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.allpost,name="allpost"),
    path('<int:Nature_Web_Blog_id>/',views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)