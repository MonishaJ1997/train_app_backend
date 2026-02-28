# serializers.py
from rest_framework import serializers
from .models import TrainBanner

class TrainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainBanner
        fields = '__all__'


# serializers.py
from rest_framework import serializers
from .models import SiteLogo

class SiteLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLogo
        fields = "__all__"



from rest_framework import serializers
from .models import TrainMap, Train

class TrainMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainMap
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


from rest_framework import serializers
from .models import Train, TrainSchedule


class TrainScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainSchedule
        fields = "__all__"


class TrainSerializer(serializers.ModelSerializer):
    schedules = TrainScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = "__all__"




        from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"











from rest_framework import serializers
from .models import Banner

class BannerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    


from rest_framework import serializers
from .models import TravelPackage

class TravelPackageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = TravelPackage
        fields = '__all__'




        from rest_framework import serializers
from .models import TourBanner

class TourBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourBanner
        fields = '__all__'



        # tour/serializers.py
from rest_framework import serializers
from .models import Slider

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'image', 'created_at')