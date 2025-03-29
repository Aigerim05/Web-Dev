from django.http import JsonResponse
from django.shortcuts import render

from .serializers import CompanySerializer, VacancySerializer

from .models import Company, Vacancy

def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error" : str(e)}, status=404)
         
    if request.method == "GET":
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False, status=200)
    

def vacancies_list(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error" : str(e)}, status=404)
         
    if request.method == "GET":
        vacancies = Vacancy.objects.filter(company=company) 
        serializer = VacancySerializer(vacancies, many=True)  
        return JsonResponse(serializer.data, safe=False, status=200)
    

def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"error" : str(e)}, status=404)
         
    if request.method == "GET":
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False, status=200)
    
def top_ten(request):
    if request.method == "GET":
        top_vacancies = Vacancy.objects.order_by('-salary')[:10]  
        serializer = VacancySerializer(top_vacancies, many=True)  
        return JsonResponse(serializer.data, safe=False, status=200)


        
    
    

