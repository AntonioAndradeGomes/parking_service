from django.contrib import admin
from parking.models import ParkingSpot, ParkingRecord

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied', 'created_at', 'updated_at']
    search_fields = ['spot_number']
    list_filter = ['is_occupied']

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['parking_spot', 'vehicle', 'entry_time', 'exit_time', 'created_at', 'updated_at']
    search_fields = ['vehicle__license_plate','parking_spot__spot_number']


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if(db_field.name == 'parking_spot' and not request.resolver_match.url_name.endswith('change')):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)