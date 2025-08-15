from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    ctx = {}
    if request.method == 'POST':
        ctx['product_id'] = request.POST.get('product_id', '').strip()
    return render(request, 'products_qr/home.html', ctx)

