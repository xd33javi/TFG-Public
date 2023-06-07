from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="index"),
    path('nuevasala/',views.crear_sala),
    path("removes/<str:sala_id>/", views.borrar_sala, name="borrar sala"),
    path("<str:room_name>/", views.home),
    path("gs/<str:sala_id>/", views.guardar_sala, name="guardar sala"),
    path("rms/<str:sala_id>/", views.borrar_sala_lista, name="borrar sala de la lista"),
]
