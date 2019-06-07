from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
    path('siyoon/', wordcount.views.siyoon, name="siyoon"),
    path('sy_result/', wordcount.views.sy_result, name="sy_result"),
]