from django.urls import path


from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    completed_status_change,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/status-change/",
        completed_status_change,
        name="completed-status-change"
    ),
]

app_name = "todo"
