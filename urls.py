from django.urls import path

from front import views

app_name = 'front'

urlpatterns = [
    path("", views.index, name='index'),
    path("notfound/", views.not_found, name='not_found'),
    path("blank/", views.blank, name='blank'),
    path("buttons/", views.buttons, name="buttons"),
    path("cards/", views.cards, name="cards"),
    path("charts/", views.charts, name="charts"),
    path("forget_pwd/", views.forget_pwd, name="forget_pwd"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("tables/", views.tables, name="tables"),
    path("animation/", views.animation, name="animation"),
    path("border/", views.border, name="border"),
    path("color/", views.color, name="color"),
    path("other/", views.other, name="other"),

]
