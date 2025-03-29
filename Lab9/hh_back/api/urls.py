from django.urls import path

from .views import *


urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', get_company),
    path('companies/<int:id>/vacancies/', vacancies_list),
    path('vacancies/<int:id>/', get_vacancy),
    path('vacancies/top_ten/', top_ten),

]