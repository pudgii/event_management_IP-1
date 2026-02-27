from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def validate_slots(self, value):
        if value < 0:
            raise serializers.ValidationError("Slots must not be below 0.")
        return value
    def validate_price(self, value):
        if value < 0:
         raise serializers.ValidationError("Price must not be negative.")
        return value

