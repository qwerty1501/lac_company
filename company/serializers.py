from rest_framework import serializers as s

from .models import CreateStaff, Services, Partners, Reviews


class CreateStaffSerializers(s.ModelSerializer):
    
    class Meta:
        model = CreateStaff
        fields = ['image', 'name', 'position', 'id']
        
        
class ServicesSerializers(s.ModelSerializer):
    
    class Meta:
        model = Services
        fields = ['name', 'description', 'id']
        
        
class PartnersSerializers(s.ModelSerializer):
    
    class Meta:
        model = Partners
        fields = ['loga', 'description', 'id']
        
        
class ReviewsSerializers(s.ModelSerializer):
    
    class Meta:
        model = Reviews
        fields = ['name', 'description', 'id']