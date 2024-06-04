from django.shortcuts import render, redirect
from .models import GFG
from django.contrib import messages
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    hotels = GFG.objects.all()
    return render(request, 'home.html', {'hotels': hotels})


def get_hotel(request):
    try:
        Ans_objs = GFG.objects.all()

        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            Ans_objs = Ans_objs.filter(hotel_price__lte=amount)

        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                Ans_objs = Ans_objs.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                Ans_objs = Ans_objs.order_by('-hotel_price')

        payload = []
        for Ans_obj in Ans_objs:
            payload.append({
                'name': Ans_obj.hotel_name,
                'price': Ans_obj.hotel_price,
                'description': Ans_obj.hotel_description,
            })
        return JsonResponse(payload, safe=False)

    except Exception as e:
        logger.error("An error occurred while fetching hotel details: %s", e)
        return JsonResponse({'message': 'Something went wrong!', 'error': str(e)}, status=500)
    
def add_hotel(request):
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel_name')
        hotel_price = request.POST.get('hotel_price')
        hotel_description = request.POST.get('hotel_description')
        
        if hotel_name and hotel_price and hotel_description:
            GFG.objects.create(
                hotel_name=hotel_name,
                hotel_price=hotel_price,
                hotel_description=hotel_description
            )
            messages.success(request, 'Hotel details added successfully')
            return redirect('home')  

    return render(request, 'add_hotel.html')