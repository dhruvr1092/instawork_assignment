from rest_framework import serializers

from team_management.models import team_member, roles

from django.contrib.auth.models import User

import re

class team_member_serializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email',required=True)
    role = serializers.CharField(source='role.name') 
    
    class Meta:
        model = team_member
        fields = ['first_name' , 'last_name', 'email' , 'phone', 'role' , "id"]

    def validate_role(self, value):
        """
        Check that role is a valid value.
        """
        if roles.objects.filter(name=value).count() == 0 :
            raise serializers.ValidationError("Role value is invalid.")
        return value

    def validate_phone(self, value):
        """
        Check that phone is a valid value.
        """      
        if not re.match(r'^[0-9]{10,14}$',value):
            raise serializers.ValidationError("Phone value is invalid.")
        return value

    def create(self, validated_data):
        usr = validated_data.pop('user')
        usr = User.objects.create(**usr, username = User.objects.all().count() + 1)
        
        role = validated_data.pop('role')        
        role =roles.objects.get(name=role["name"])        
        
        validated_data["user"] = usr
        validated_data["role"] = role

        try:
            tm = team_member.objects.create(**validated_data)
        except:
            usr.delete()
            raise serializers.ValidationError("Something wrong happened while creating team-member")
        return tm
    def update(self, instance, validated_data):
        
        #updating user data
        if "user" in validated_data:
            usr_data = validated_data.pop('user')

            usr = instance.user
        
            if "email" in usr_data:
                usr.email = usr_data["email"]
        
            if "first_name" in usr_data:
                usr.first_name = usr_data["first_name"]
        
            if "last_name" in usr_data:
                usr.last_name = usr_data["last_name"]
            
            usr.save()

        # udating proper role instance 
        if "role" in validated_data:
            roles_data = validated_data.pop('role')
            role = roles.objects.get(name=roles_data["name"])
            instance.role = role
            instance.save()

        if "phone" in validated_data:
            instance.phone = validated_data["phone"]

        instance.save()

        return instance