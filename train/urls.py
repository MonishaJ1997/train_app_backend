# urls.py
from django.urls import path
from .views import TrainBannerListView
from .views import SiteLogoView
from . import views
from .views import TrainMapListView,TrainListView
from .views import BannerView
from .views import TravelPackageListView
from rest_framework.routers import DefaultRouter
from .views import TrainViewSet
from .views import create_payment
from .views import StationViewSet
from .views import TourBannerListView
from .views import SliderListView

router = DefaultRouter()
router.register(r'trains', TrainViewSet)
router.register(r"stations", StationViewSet)

urlpatterns = [
    path('train-banner/', TrainBannerListView.as_view(), name='train-banner'),
    path("site-logo/", SiteLogoView.as_view()),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('map/', TrainMapListView.as_view(), name='train-map'),
    path('banners/', BannerView.as_view()),
    path('packages/', TravelPackageListView.as_view(), name='packages'),
    path("schedule/<int:train_id>/", views.train_schedule, name="train_schedule"),
     path("create-payment/", create_payment),
     path('tour-banner/', TourBannerListView.as_view(), name='tour-banner'),
path('slider/', SliderListView.as_view(), name='slider-list'),

]

urlpatterns += router.urls
