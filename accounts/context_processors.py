from vendor.models import Vendor
from .models import UserProfile
from django.conf import settings

def get_vendor(request):
    try:
        vendor=Vendor.objects.get(user=request.user)
    except:
        vendor=None
    return dict(vendor=vendor)

def get_google_api(request):
    return {'GOOGLE_API_KEY':settings.GOOGLE_API_KEY}

def get_user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = None
    return dict(user_profile=user_profile)        

def get_paypal_id(request):
    return {'PAYPAL_CLIENT_ID':settings.PAYPAL_CLIENT_ID}