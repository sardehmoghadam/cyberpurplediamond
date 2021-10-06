from django.urls import path
from . import views
app_name = "temp"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("feature", views.feature, name="feature"),
    path("preattck", views.preattck, name="preattck"),
    path("mobile", views.mobile, name="mobile"),
    path("news", views.news, name="news"),
    path("about", views.about, name="about"),
    path("post", views.post, name="post"),
    path("register", views.register, name="register"),
    path("registerform", views.registerform, name="registerform"),
    path("logging", views.logging, name="logging"),
    path("log_out", views.log_out, name="log_out"),
    path("mitrematrix", views.mitrematrix, name="mitrematrix"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("updatemitre", views.updatemitre, name="updatemitre"),
    path("subscription", views.subscription, name="subscription"),
    path("hypothesis", views.hypothesis, name="hypothesis"),
    path("ai", views.ai, name="ai"),
    path("emulate", views.emulate, name="emulate"),
    path("makeadversary", views.makeadversary, name="makeadversary"),
    path("certification", views.certification, name="certification"),
]
