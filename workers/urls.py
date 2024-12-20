from django.urls import path

from workers.apps import WorkersConfig
from workers.views import WorkerRetrieveAPIView, TeamWorkerListAPIView

app_name = WorkersConfig.name

urlpatterns = [
    path('team/<int:pk>/WorkerList', TeamWorkerListAPIView.as_view(), name='team_workers_list'),
    path('worker/<int:pk>/', WorkerRetrieveAPIView.as_view(), name='view_worker')
]
