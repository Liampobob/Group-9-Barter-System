from rest_framework import serializers
import json

class WorkerSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=128)
    business_name = serializers.CharField(required=True, max_length=128)
    #working_days = serializers.CharField(required=True, many=True, )
    #work_tags = serializers.CharField(required=True, max_length=128)
    description = serializers.CharField(required=True, max_length=128)
    contact = serializers.CharField(required=True, max_length=128)
    start_time = serializers.IntegerField(required=True, min_value=0)
    end_time = serializers.IntegerField(required=True, min_value=0)

    def validate(self, data):
        """
        Check that the model is valid.
        """
        if not data['name']:
            raise serializers.ValidationError("Name cannot be empty")
        if not data['business_name']:
            raise serializers.ValidationError("business_name cannot be empty")
        if not data['description']:
            raise serializers.ValidationError("description cannot be empty")
        if not data['contact']:
            raise serializers.ValidationError("contact cannot be empty")
        if type(data['start_time']) != int:
            raise serializers.ValidationError("start_time cannot be empty")
        if type(data['end_time']) != int:
            raise serializers.ValidationError("end_time cannot be empty")
        """
        Check that the start date and the end date are valid (<24).
        """
        if data['start_time'] > 24:
            raise serializers.ValidationError(
                "start_time must be between 0 and 24")
        if data['end_time'] > 24:
            raise serializers.ValidationError(
                "end_time must be between 0 and 24")
        """
        Check that the start date is before the end date.
        """
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError(
                "start_time must be before end_time")
        return data
