from rest_framework.viewsets import ModelViewSet

from .models import Session

class SessionView(ModelViewSet):
    queryset = Session.objects.all()
    #permission_classes = [IsAuthenticated]
    #serializer_class = SessionSerializer
