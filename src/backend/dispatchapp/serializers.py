from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'

    def validate_message(self, message):
        if len(message) > 10000:
            raise serializers.ValidationError("This message is way too long!!")
        return message
