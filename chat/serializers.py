from rest_framework import serializers
from .models import message
from rest_framework.authtoken.models import Token

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = message
        fields = ['sender','content', 'reciever']



class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')

    

        
        

