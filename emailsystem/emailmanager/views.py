from rest_framework.response import Response
from .models import EmailModel
from .serializers import EmailModelSerializer
from rest_framework.viewsets import ModelViewSet
from .emailprogram import email_func


class EmailModelViewSet(ModelViewSet):
    model = EmailModel
    serializer_class = EmailModelSerializer
    permission_classes = ()
    queryset = EmailModel.objects.all()

    def create(self, request):
        """
        author: veenit kumar shukla
        description: saves the data and the calls the email function
        :param request: self,request
        :return: response
        Method Allowed: POST
        """
        if request.method == "POST":
            EmailModel.objects.create(**request.data)
            email_func(request.data["sender_mail"], request.data["subject"], request.data["body"])
        return Response("hello")
