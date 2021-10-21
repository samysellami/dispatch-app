from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'

    def validate_message(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("This message is way too long!!")
        return value

    def validate_subject(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("This subject is way too long!!")
        return value
