from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
        #Ruta que se despliega al abrir la aplicacion (la url de la aplicacion)
    path('', HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name="about")
]