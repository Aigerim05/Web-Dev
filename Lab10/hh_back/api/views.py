import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render

from .serializers import CompanySerializer, PositionSerializer, VacancySerializer

from .models import Company, Position, Vacancy
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

@api_view(http_method_names=["GET", "POST"]) 
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(http_method_names=["GET", "PUT", "DELETE"]) 
def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({"error" : str(e)}, status=status.HTTP_404_NOT_FOUND)
         
    if request.method == "GET":
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = CompanySerializer(instance=company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        company.delete()
        return Response({"message": "Company deleted successfully."}, status=status.HTTP_200_OK)


class VacanciesAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            raise NotFound(detail="Vacancy not found", code=404)
        
    def get(self, request, id):
        vacancies = Vacancy.objects.filter(company=self.get_object(id)) 
        serializer = VacancySerializer(vacancies, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
  
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
        



class VacancyDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({"error" : str(e)}, status=status.HTTP_404_NOT_FOUND)
        

    def get(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        vacancy = self.get_object(id)

        serializer = VacancySerializer(instance = vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, id):
        vacancy = self.get_object(id)
        vacancy.delete()
        return Response({"message": "vacancy deleted"}, status=status.HTTP_200_OK)







        
    
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


