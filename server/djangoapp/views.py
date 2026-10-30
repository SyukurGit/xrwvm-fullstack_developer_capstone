import json
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel

logger = logging.getLogger(__name__)

# Mock datasets for dealers and reviews (matching microservice endpoints)
DEALERS_DATA = [
    {"id": 1, "city": "El Paso", "state": "Texas", "address": "3 Nova Court", "zip": "88563", "lat": 31.6948, "long": -106.3, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership"},
    {"id": 2, "city": "Minneapolis", "state": "Minnesota", "address": "6337 Butternut Crossing", "zip": "55402", "lat": 44.9762, "long": -93.2759, "short_name": "Temp", "full_name": "Temp Car Dealership"},
    {"id": 3, "city": "Birmingham", "state": "Alabama", "address": "9477 Twin Pines Center", "zip": "35285", "lat": 33.5446, "long": -86.9292, "short_name": "Sub-Ex", "full_name": "Sub-Ex Car Dealership"},
    {"id": 4, "city": "Dallas", "state": "Texas", "address": "85800 Hazelcrest Circle", "zip": "75241", "lat": 32.6722, "long": -96.7774, "short_name": "Solarbreeze", "full_name": "Solarbreeze Car Dealership"},
    {"id": 5, "city": "Baltimore", "state": "Maryland", "address": "93 Golf Course Pass", "zip": "21203", "lat": 39.2847, "long": -76.6205, "short_name": "Regrant", "full_name": "Regrant Car Dealership"},
    {"id": 8, "city": "Topeka", "state": "Kansas", "address": "288 Larry Place", "zip": "66642", "lat": 39.0429, "long": -95.7697, "short_name": "Bytecard", "full_name": "Bytecard Car Dealership"},
    {"id": 15, "city": "San Antonio", "state": "Texas", "address": "5057 Pankratz Hill", "zip": "78225", "lat": 29.3875, "long": -98.5245, "short_name": "Tempsoft", "full_name": "Tempsoft Car Dealership"}
]

REVIEWS_DATA = {
    15: [
        {"id": 1, "name": "Berkly Shepley", "dealership": 15, "review": "Total grid-enabled service-desk", "purchase": True, "purchase_date": "07/11/2020", "car_make": "Audi", "car_model": "A6", "car_year": 2010, "sentiment": "neutral"},
        {"id": 37, "name": "Albrecht Collen", "dealership": 15, "review": "Pre-emptive heuristic solution", "purchase": True, "purchase_date": "10/10/2020", "car_make": "Lexus", "car_model": "IS F", "car_year": 2009, "sentiment": "positive"},
        {"id": 38, "name": "Prudi Minchi", "dealership": 15, "review": "Mandatory homogeneous groupware", "purchase": True, "purchase_date": "01/06/2021", "car_make": "Saturn", "car_model": "L-Series", "car_year": 2001, "sentiment": "neutral"},
        {"id": 51, "name": "Syukur", "dealership": 15, "review": "Exceptional customer service! Highly recommend this dealership.", "purchase": True, "purchase_date": "06/15/2026", "car_make": "Toyota", "car_model": "Camry", "car_year": 2023, "sentiment": "positive"}
    ]
}

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        return JsonResponse({"userName": username, "status": "Failed"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})

@csrf_exempt
def registration(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({"userName": username, "error": "Already Registered"})

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

def get_dealerships(request, state="all"):
    if state == "all":
        return JsonResponse({"status": 200, "dealers": DEALERS_DATA})
    dealers = [d for d in DEALERS_DATA if d['state'].lower() == state.lower()]
    return JsonResponse({"status": 200, "dealers": dealers})

def get_dealer_details(request, dealer_id):
    dealer = next((d for d in DEALERS_DATA if d['id'] == dealer_id), None)
    if dealer:
        return JsonResponse(dealer)
    return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)

def get_dealer_reviews(request, dealer_id):
    reviews = REVIEWS_DATA.get(dealer_id, [])
    return JsonResponse({"status": 200, "reviews": reviews})

@csrf_exempt
def add_review(request):
    if request.user.is_anonymous is False:
        data = json.loads(request.body)
        dealer_id = data.get('dealership')
        if dealer_id not in REVIEWS_DATA:
            REVIEWS_DATA[dealer_id] = []
        REVIEWS_DATA[dealer_id].append(data)
        return JsonResponse({"status": 200, "message": "Review added successfully"})
    return JsonResponse({"status": 403, "message": "Unauthorized"}, status=403)

def get_cars(request):
    car_models = CarModel.objects.select_related('car_make').all()
    cars_list = []
    for model in car_models:
        cars_list.append({
            "CarModel": model.name,
            "CarMake": model.car_make.name
        })
    if not cars_list:
        cars_list = [
            {"CarModel": "Pathfinder", "CarMake": "Nissan"},
            {"CarModel": "Qashqai", "CarMake": "Nissan"},
            {"CarModel": "XTRAIL", "CarMake": "Nissan"},
            {"CarModel": "A-Class", "CarMake": "Mercedes"},
            {"CarModel": "C-Class", "CarMake": "Mercedes"},
            {"CarModel": "E-Class", "CarMake": "Mercedes"},
            {"CarModel": "A4", "CarMake": "Audi"},
            {"CarModel": "A5", "CarMake": "Audi"},
            {"CarModel": "A6", "CarMake": "Audi"},
            {"CarModel": "Sorrento", "CarMake": "Kia"},
            {"CarModel": "Carnival", "CarMake": "Kia"},
            {"CarModel": "Cerato", "CarMake": "Kia"},
            {"CarModel": "Corolla", "CarMake": "Toyota"},
            {"CarModel": "Camry", "CarMake": "Toyota"},
            {"CarModel": "Kluger", "CarMake": "Toyota"}
        ]
    return JsonResponse({"CarModels": cars_list})
