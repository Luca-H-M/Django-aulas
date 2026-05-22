from django.urls import path
from loja.views.HomeView import home_view urlpatterns = [path("", home_view),]

def home_view(request):
    return render(request, template_name='home/home.html', status=200)