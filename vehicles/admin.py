from django.contrib import admin
from vehicles.models import Vehicle, VehicleType

@admin.register(VehicleType)
class VeiicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name','description', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color','vehicle_type', 'owner', 'created_at', 'updated_at']
    search_fields = ['license_plate', 'brand', 'model', 'color']
    list_filter = ['vehicle_type']