from django . urls import path
from . import views

app_name="task"


urlpatterns=[

     path('todo',views.todo,name="todo"),

]