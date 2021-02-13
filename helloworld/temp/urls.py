from django.urls import path
from . import views
app_name = "temp"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("feature", views.feature, name="feature"),
    path("news", views.news, name="news"),
    path("about", views.about, name="about"),
    path("post", views.post, name="post"),

]
