from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import AuthCode, User
from accounts.serializers import UserSerializer
from datetime import datetime, timedelta
from django.utils import timezone


@api_view(['POST'])
def register_user_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = User.objects.filter(phone_number=phone_number)
        if user:
            return Response({'error': 'User with this phone number already exists.'})
        if password != password2:
            return Response({'error': 'Check if both passwords are the same.'})
        user = User.objects.create_user(phone_number=phone_number, password=password, is_active=False)
        send_mail('Confirmation code', '123456',
              'askarjon.abdullayev@gmail.com', [email], fail_silently=False)
        code = AuthCode.objects.create(code='123456', sent_to_adress=email, user=user)
        serializer = UserSerializer(user).data
        return Response(serializer, status=201)


@api_view(['POST'])
def confirm_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        email = request.POST.get('email')
        current_time = datetime.now()
        one_minute_ago = current_time - timezone.timedelta(minutes=1)

        code2 = AuthCode.objects.filter(code=code, sent_to_adress=email).last()
        if not code2:
            return Response({'error': 'Wrong code.'}, status=400)
        user = code2.user
        user.is_active = True
        user.save()
        return Response({'message': 'Your account was successfuly confirmed.'})