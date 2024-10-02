from django.urls import path
from .views import displayQuote  # นำเข้าฟังก์ชันที่คุณต้องการใช้งาน

urlpatterns = [
    path('pquote/', displayQuote, name='pquote'),  # เส้นทางสำหรับ pquote
]
