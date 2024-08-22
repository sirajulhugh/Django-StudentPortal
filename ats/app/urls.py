from django.urls import path,include
from .import views

urlpatterns = [

path('',views.loginpage,name='loginpage'),
path('register',views.signuppage,name='signuppage'),
path('add_details',views.add_details,name='add_details'),
path('log',views.log,name='log'),
path('adminmod',views.adminmod,name='adminmod'),
path('usermod/<int:id>',views.usermod,name='usermod'),
path('lgout',views.lgout,name='lgout'),
path('page1', views.page1, name='page1'),
path('add_course', views.add_course, name='add_course'),
path('addcourse', views.addcourse, name='addcourse'),
path('add_student', views.add_student, name='add_student'),
path('addstudent', views.addstudent, name='addstudent'),
path('student_list', views.student_list, name='student_list'),
path('edit_student/<int:id>', views.edit_student, name='edit_student'),
path('editstudent/<int:id>', views.editstudent, name='editstudent'),
path('deletestudent/<int:id>', views.deletestudent, name='deletestudent'),
path('delteacher/<int:id>', views.delteacher, name='delteacher'),
path('teacher_list', views.teacher_list, name='teacher_list'),
path('edit_user/<int:id>', views.edit_user, name='edit_user'),
path('update/<int:id>', views.update, name='update'),
path('card_teacher/<int:id>', views.card_teacher, name='card_teacher'),


]
