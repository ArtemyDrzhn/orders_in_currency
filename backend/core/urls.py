from django.contrib import admin
from django.urls import path

from parse.views import OrderingListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OrderingListView.as_view())
]
