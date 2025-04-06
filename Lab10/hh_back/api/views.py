import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render

from .serializers import CompanySerializer, PositionSerializer, VacancySerializer

from .models import Company, Position, Vacancy

@csrf_exempt
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        company_json = [c.to_json() for c in companies]
        return JsonResponse(company_json, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)

        try:
            company = Company.objects.create(
                name=data["name"],
                description=data["description"],
                city=data["city"],
                address=data["address"]
            )
        except Exception as e:
            return JsonResponse({"error":str(e)})
        return JsonResponse(company.to_json(), status=201)


@csrf_exempt
def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error" : str(e)}, status=404)
         
    if request.method == "GET":
        return JsonResponse(company.to_json(), safe=False)
    
    elif request.method == "PUT":
        data = json.loads(request.body)

        try:
            company.name = data.get("name", company.name)
            company.description = data.get("description", company.description)
            company.city = data.get("city", company.city)
            company.address = data.get("address", company.address)
            company.save()
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


    elif request.method == "DELETE":
        company.delete()
        return JsonResponse({"message": "Company deleted successfully."}, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class VacanciesView(View):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return JsonResponse({"error" : str(e)}, status=404)
            
        vacancies = Vacancy.objects.filter(company=company) 
        serializer = VacancySerializer(vacancies, many=True)  
        return JsonResponse(serializer.data, safe=False, status=200)
  
    def post(self,request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return JsonResponse({"error" : str(e)}, status=404)
            
        data = json.loads(request.body)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save(company=company)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        


@method_decorator(csrf_exempt, name='dispatch')  
class VacancyDetailView(View):
    def get(self, resuest, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({"error": str(e)}, status=404)

        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False, status=200)
    
    def put(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({"error": str(e)}, status=404)

        data = json.loads(request.body)

        try:
            vacancy.name = data.get("name", vacancy.name)
            vacancy.description = data.get("description", vacancy.description)
            vacancy.salary = data.get("salary", vacancy.salary)
            vacancy.company = data.get("company", vacancy.company)
            vacancy.position = data.get("position", vacancy.position)
            vacancy.save()
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    def delete(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({"error": str(e)}, status=404)
        
        vacancy.delete()
        return JsonResponse({"message": "vacancy deleted"}, status=200)







        
    
def position_list(request):
    if request.method == "GET":
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    
def get_position(request, id):
    try:
        position = Position.objects.get(id=id)
    except Position.DoesNotExist as e:
        return JsonResponse({"error" : str(e)}, status=404)
         
    if request.method == "GET":
        serializer = PositionSerializer(position)
        return JsonResponse(serializer.data, safe=False, status=200)


