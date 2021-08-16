from django.contrib import admin
from django.urls import path,include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),  # redirect application 'catalog/' url initialy 

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
