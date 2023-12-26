from rest_framework import serializers
from .models import Customer,Firstclass


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ["id", "user", "first_name", "last_name", "short_name",
                  "email", "address", "pincode", "mobile", "created_at", "modified_at"]


class Firstclassserializer(serializers.ModelSerializer):
    class Meta:
        model = Firstclass
        fields = "__all__"
