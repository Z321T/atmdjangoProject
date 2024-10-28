from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cardid = data.get('123456')
            password = data.get('123456')

            # Here you would add your authentication logic
            if cardid == '123456' and password == '123456':  # Example check
                return JsonResponse({'status': 'success', 'message': 'Login successful'})
            else:
                return JsonResponse({'status': 'failure', 'message': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'failure', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'}, status=405)
