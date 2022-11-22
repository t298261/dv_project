
from django.urls import path
from . import views






urlpatterns = [

    # path("update_server/", views.git_pythonanywhere, name="update"),
    
    path('generate_pdf1', views.generate_pdf, name="generate-pdf1"),
    path('auto_download_pdf1', views.auto_download_pdf1, name="download-pdf1"),


    path('generate_pdf2', views.generate_pdf2, name="generate-pdf2"),
    path('auto_download_pdf2', views.auto_download_pdf2, name="download-pdf2"),

    path('generate_pdf3', views.generate_pdf3, name="generate-pdf3"),
    path('auto_download_pdf3', views.auto_download_pdf3, name="download-pdf3"),

    path('generate_pdf4', views.generate_pdf4, name="generate-pdf4"),
    path('auto_download_pdf4', views.auto_download_pdf4, name="download-pdf4"),

]