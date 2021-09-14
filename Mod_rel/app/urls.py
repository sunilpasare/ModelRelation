from django.urls import path
from .import views

urlpatterns=[
    path('stu/',views.Student_register_view,name='stu'),
    path('lec/',views.Lecturer_register_view,name='lec'),
    path('stud/',views.Student_list_view,name='stud'),
    path('home/',views.Homeview,name='home'),
    path('lecd/',views.Lecturer_list_view,name='lecd'),
    path('updatelec/<int:update>',views.Lecture_update_view,name='uplec'),
    path('deletelec/<int:delet>',views.Lecture_delete_view,name='del'),
    path('updatestu/<int:update>',views.Student_update_view,name='upstud'),
    path('deletestu/<int:delet>',views.Student_delete_view,name='delstud'),


]
