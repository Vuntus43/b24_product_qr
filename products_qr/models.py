import uuid
from django.db import models

class Product(models.Model):
    """Локальная карточка товара для публичной страницы по секретной ссылке."""

    name = models.CharField(max_length=255, help_text="Название товара.")
    sku = models.CharField(max_length=64, blank=True, db_index=True, help_text="Артикул/код (необязательно).")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Цена.")
    currency = models.CharField(max_length=8, default='RUB', help_text="Валюта цены.")
    photo = models.ImageField(upload_to='products/photos/', null=True, blank=True, help_text="Локальный файл фото")
    bitrix_id = models.IntegerField(null=True, blank=True, db_index=True, help_text="ID товара в Битрикс24 (необязательно).")
    description = models.TextField(blank=True, help_text="Описание/характеристики.")
    is_active = models.BooleanField(default=True, help_text="Быстро выключить товар.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Когда создано.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Когда обновлялось.")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name} (ID {self.pk})"

class ProductQRLink(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='qr_links')
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)
    qr_image = models.ImageField(upload_to='products/qr/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Секретная ссылка на товар"
        verbose_name_plural = "Секретные ссылки на товар"

    def __str__(self):
        return f"{self.product_id} — {self.token}"