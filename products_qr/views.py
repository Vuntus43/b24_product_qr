from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from django.core.files.base import ContentFile
import qrcode

from products_qr.models import Product, ProductQRLink


@csrf_exempt
def home(request):
    ctx = {'last_products': Product.objects.order_by('-created_at')[:5]}

    if request.method == 'POST':
        pid = (request.POST.get('product_id') or '').strip()

        # Служебные POST от Б24 приходят без наших полей — просто рендерим страницу
        if not pid:
            return render(request, 'products_qr/home.html', ctx)

        if not pid.isdigit():
            ctx['error'] = 'Введите числовой ID товара'
            return render(request, 'products_qr/home.html', ctx)

        product = Product.objects.filter(id=int(pid), is_active=True).first()
        if not product:
            ctx['error'] = 'Товар не найден или выключен'
            return render(request, 'products_qr/home.html', ctx)

        # 1) Создаём секретную ссылку (UUID генерится сам)
        link = ProductQRLink.objects.create(product=product)

        # 2) Публичный URL вида /p/<uuid>/
        public_url = request.build_absolute_uri(
            reverse('public_product_page', args=[link.token])
        )

        # 3) Генерим PNG с QR-кодом на этот URL
        qr = qrcode.QRCode(
            version=1,
            box_size=8,
            border=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
        )
        qr.add_data(public_url)
        qr.make(fit=True)
        img = qr.make_image()

        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        link.qr_image.save(f"qr_{link.token}.png", ContentFile(buf.read()), save=True)

        ctx.update({'product': product, 'link': link, 'public_url': public_url})

    return render(request, 'products_qr/home.html', ctx)

@csrf_exempt
def public_product_page(request, token):
    link = get_object_or_404(ProductQRLink, token=token, is_active=True)
    product = link.product
    return render(request, 'products_qr/public.html', {'product': product, 'link': link})
