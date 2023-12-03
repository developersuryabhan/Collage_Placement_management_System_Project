from django.urls import path
from placement_app import views


urlpatterns = [
    path('',views.index),
    path('register_student',views.register_student),
    path('register_company',views.register_company),
    path('interviews',views.interviews_page),
    path('interviews_update/<int:id>',views.interview_update),
    path('placements',views.placements),
    path('login', views.Login, name="login"),

]
