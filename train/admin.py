# admin.py
from django.contrib import admin
from .models import TrainBanner

@admin.register(TrainBanner)
class TrainBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')



    # admin.py
from django.contrib import admin
from .models import SiteLogo

@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo", "created_at")


    from django.contrib import admin
from .models import TrainMap, Train


@admin.register(TrainMap)
class TrainMapAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']



from django.contrib import admin
from .models import Train, TrainSchedule


class TrainScheduleInline(admin.TabularInline):
    model = TrainSchedule
    extra = 1


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ("train_number", "train_name", "source", "destination")
    inlines = [TrainScheduleInline]


from django.contrib import admin
from .models import Banner

admin.site.register(Banner)



from django.contrib import admin
from .models import TravelPackage

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    prepopulated_fields = {"slug": ("title",)}






    from django.contrib import admin
from .models import Station

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "address")
    search_fields = ("name", "code")



    from django.contrib import admin
from .models import TourBanner

@admin.register(TourBanner)
class TourBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')




# tour/admin.py
from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'created_at')