from rest_framework import generics

from workers.models import Worker
from workers.serializers import WorkerSerializer


# Create your views here.


class TeamWorkerListAPIView(generics.ListAPIView):
    serializer_class = WorkerSerializer

    def get_queryset(self):
        queryset = Worker.objects.filter(team=self.request.parser_context['kwargs']['pk'])
        return queryset


class WorkerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
