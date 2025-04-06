from django.urls import path

from .views import *


urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', get_company),
    path('companies/<int:id>/vacancies/', VacanciesView.as_view(), name='vacancies-list'),
    path('vacancies/<int:id>/', VacancyDetailView.as_view()),
    path('positions/', position_list),
    path('positions/<int:id>/', get_position),

]