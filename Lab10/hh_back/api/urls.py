from django.urls import path

from .views import *


urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', get_company),
    path('companies/<int:id>/vacancies/', VacanciesAPIView.as_view(), name='vacancies-list'),
    path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),
    path('positions/', position_list),
    path('positions/<int:id>/', get_position),

]