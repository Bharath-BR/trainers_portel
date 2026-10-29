from django.urls import path
from . import views


urlpatterns=[
    path('createstudent/',views.create_view,name="create"),
    path('',views.display_view ,name="display"),
    path("updatestudent/<int:student_id>",views.update_view,name="update"),
    path("deletestudent/<int:student_id>",views.delete_view,name="delete"),
]
