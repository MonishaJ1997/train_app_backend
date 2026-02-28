# views.py
from rest_framework.generics import ListAPIView
from .models import TrainBanner
from .serializers import TrainBannerSerializer

class TrainBannerListView(ListAPIView):
    queryset = TrainBanner.objects.all().order_by('-created_at')
    serializer_class = TrainBannerSerializer


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SiteLogo
from .serializers import SiteLogoSerializer

class SiteLogoView(APIView):
    def get(self, request):
        logo = SiteLogo.objects.last()  # latest logo
        serializer = SiteLogoSerializer(logo)
        return Response(serializer.data)
    


# train/views.py
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password:
                return JsonResponse({"message": "All fields are required"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"message": "Username already exists"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email already exists"}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({"message": "User created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"message": "Method not allowed"}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                })
            else:
                return JsonResponse({"message": "Invalid username or password"}, status=401)
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"message": "Method not allowed"}, status=405)







from rest_framework import generics
from .models import TrainMap, Train
from .serializers import TrainMapSerializer, TrainSerializer


# Get Map Image
class TrainMapListView(generics.ListAPIView):
    queryset = TrainMap.objects.all()
    serializer_class = TrainMapSerializer



from rest_framework.generics import ListAPIView
from .models import Train
from .serializers import TrainSerializer
from rest_framework import viewsets
class TrainListView(ListAPIView):
    serializer_class = TrainSerializer

    def get_queryset(self):
        queryset = Train.objects.all()

        source = self.request.query_params.get('source')
        destination = self.request.query_params.get('destination')

        if source:
            queryset = queryset.filter(source__icontains=source)

        if destination:
            queryset = queryset.filter(destination__icontains=destination)

        return queryset


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()   # ✅ REQUIRED
    serializer_class = TrainSerializer

    def get_queryset(self):
        queryset = Train.objects.all()

        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")
        train_number = self.request.query_params.get("train_number")
        search = self.request.query_params.get("search")

        if source and destination:
            queryset = queryset.filter(
                source__icontains=source,
                destination__icontains=destination
            )

        if train_number:
            queryset = queryset.filter(
                train_number__icontains=train_number
            )

        if search:
            from django.db.models import Q
            queryset = queryset.filter(
                Q(train_name__icontains=search) |
                Q(train_number__icontains=search)
            )

        return queryset
from django.http import JsonResponse
from .models import TrainSchedule





















##def train_schedule(request, train_id):
    ##schedules = TrainSchedule.objects.filter(
        #train_id=train_id
   # ).order_by("route_number")

    #data = list(schedules.values())
    #return JsonResponse(data, safe=False)





from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TrainSchedule

@api_view(["GET"])
def train_schedule(request, train_id):
    schedules = TrainSchedule.objects.filter(train_id=train_id)

    data = [
        {
            "station_name": s.station_name,
            "arrival_time": s.arrival_time,
            "departure_time": s.departure_time,
            "day_number": s.day_number
        }
        for s in schedules
    ]

    return Response(data)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Banner
from .serializers import BannerSerializer

class BannerView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True, context={'request': request})
        return Response(serializer.data)
    

    from rest_framework import generics
from .models import TravelPackage
from .serializers import TravelPackageSerializer

class TravelPackageListView(generics.ListAPIView):
    queryset = TravelPackage.objects.filter(is_active=True)
    serializer_class = TravelPackageSerializer





# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import stripe
import os

# Make sure you have your Stripe secret key in environment variables
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")  # or hardcode for testing

@api_view(['POST'])
def create_payment(request):
    try:
        data = request.data

        total_amount = data.get("totalAmount")
        if total_amount is None:
            return Response({"error": "totalAmount is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Stripe expects amount in paise/cents
        total_cents = int(float(total_amount) * 100)

        # Create PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=total_cents,
            currency="inr",
            payment_method_types=["card"],
        )

        return Response({
            "clientSecret": intent.client_secret,
            "totalAmount": total_amount
        })

    except Exception as e:
        print("Stripe Payment Error:", str(e))
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



    from rest_framework import viewsets
from django.db.models import Q
from .models import Station
from .serializers import StationSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def get_queryset(self):
        queryset = Station.objects.all()
        search = self.request.query_params.get("search")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(code__icontains=search)
            )

        return queryset
    



    from rest_framework.generics import ListAPIView
from .models import TourBanner
from .serializers import TourBannerSerializer

class TourBannerListView(ListAPIView):
    queryset = TourBanner.objects.all().order_by('-created_at')
    serializer_class = TourBannerSerializer




# tour/views.py
from rest_framework import generics
from .models import Slider
from .serializers import SliderSerializer

class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all().order_by('id')
    serializer_class = SliderSerializer