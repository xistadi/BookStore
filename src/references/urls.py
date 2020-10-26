from django.urls import path
from .views import show_references_view, show_reference_by_pk_view

urlpatterns = [
    path('', show_references_view),
    path('<str:title>/<int:ref_pk>/', show_reference_by_pk_view),
]