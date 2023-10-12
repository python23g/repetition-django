from django.urls import path
from .views import (
    add,
    subtract,
    multiply,
    divide,
    square,
    square_root,
)

urlpatterns = [
    path('add/', add),
    path('subtract/', subtract),
    path('multiply/', multiply),
    path('divide/', divide),
    path('square/', square),
    path('square_root/', square_root),
]
