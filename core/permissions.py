from rest_framework import permissions

class IsOwnerOfVehicleOrRecord(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        
        #se existe o atributo 'owner' no objeto, vem do modelo Vehicle
        if(hasattr(obj, 'owner')):
           return obj.owner and obj.owner.user == user
        
        #se existe o atributo 'vehicle' no objeto, vem do modelo ParkingRecord
        if(hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner')):
            return obj.vehicle.owner and obj.vehicle.owner.user == user
        return False