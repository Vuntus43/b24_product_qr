# local_settings.py
DEBUG = True
ALLOWED_HOSTS = ['*', 'c5b354d95473.ngrok-free.app']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

APP_SETTINGS = LocalSettingsClass(
    portal_domain='b24-q0k90e.bitrix24.ru',      # замени на свой портал при необходимости
    app_domain='c5b354d95473.ngrok-free.app',   # без схемы, как в is_demo
    app_name='b24_product_qr',
    salt='dev_salt_change_me',
    secret_key='dev_secret_change_me',
    application_bitrix_client_id='local.689f89c326bf69.20828235',   # вставь из карточки "Локальное приложение" в Б24
    application_bitrix_client_secret='tVTsGdadEI7AW45XACLXN73HzIYklTA7R0mNgv02wGxFFOzqjq', # вставь секрет оттуда же
    application_index_path='/',                      # входная точка приложения
)

# для публичных ссылок/редиректов (пригодится позже)
DOMAIN = 'https://c5b354d95473.ngrok-free.app'
