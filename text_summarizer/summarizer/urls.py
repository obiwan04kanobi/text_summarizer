from django.urls import path
from .views import summarize_text
from django.views.generic import TemplateView

urlpatterns = [
    path("summarize/", summarize_text, name="summarize_text"),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
]

