
from django.contrib import admin
from django.urls import path
from itemapp.views import CreateCheckoutSessionView, ProductLandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<pk>/', ProductLandingPageView.as_view(), name='landing')
]
