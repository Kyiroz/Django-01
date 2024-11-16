from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
        #Ruta que se despliega al abrir la aplicacion (la url de la aplicacion)
        #La ruta vacia en home significa que es la pagina inicial, la ruta llena en about/ significa que es la pagina de about
        #El parametro name es el pseudonimo que se usara en _base.html
    path('', HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name="about")
]