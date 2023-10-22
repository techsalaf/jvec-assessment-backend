# contacts/serializers.py

from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def validate_phone_number(self, value):
        # Add custom validation for phone number
        if not value.startswith('+'):
            raise serializers.ValidationError("Phone number must start with '+'")
        return value
