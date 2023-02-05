from ..models import MyModel
from rest_framework import viewsets, permissions
from .serializer import MyModelSerializer


class MyModelViesSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MyModelSerializer
