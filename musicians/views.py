from rest_framework.views import APIView, Response, Request
from django.forms.models import model_to_dict
from musicians.models import Musician


# Create your views here.
class MusicianView(APIView):
    def post(self, request: Request) -> Response:
        musician = Musician.objects.create(**request.data)
        return Response(model_to_dict(musician), 201)

    def get(self, request: Request):
       # musicians = Musician.objects.all()
       # musicians_dict = []

        # for musician in musicians:
        #    musicians_dict.append(model_to_dict(musician))

        musicians_dict = [
            model_to_dict(musician)
            for musician in Musician.objects.all()
        ]

        return Response(musicians_dict)

