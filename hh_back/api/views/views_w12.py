from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from api.models import Company,Vacancy
from api.serializers import CompanySerializer,VacancySerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# def companies_list(request):
#     if request.method=='GET':
#         companies=Company.objects.all()
#         json_companies= [company.to_json() for company in companies]
#         return JsonResponse(json_companies,safe=False)

@csrf_exempt
def companies_list(request):
    if request.method=='GET':
        companies=Company.objects.all()
        serializer=CompanySerializer(companies,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        data=json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors)

@csrf_exempt
def companies_detail(request,company_id):
    try:
        company=Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
            return JsonResponse({'error':str(e)})
    if request.method=='GET':
        serializer=CompanySerializer(company)
        return JsonResponse(serializer.data,status=200)
    elif request.method=='PUT':
        data=json.loads(request.body)
        serializer=CompanySerializer(instance=company,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors)
    elif request.method=='DELETE':
        company.delete()
        return JsonResponse({},status=204)
    # return JsonResponse(company.to_json())

@csrf_exempt
def company_vacancies(request, company_id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        vacancies = company.vacancies.all()

        # try:
        #     vacancies = Vacancy.objects.filter(company_id=company_id)
        # except Vacancy.DoesNotExist as e:
        #     return JsonResponse({'error': str(e)})

        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)

    elif request.method == 'POST':
        return JsonResponse({'data': 'Vacancy post request'})
# def company_vacancies(request,company_id):
#     try:
#         company=Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#             return JsonResponse({'error':str(e)})
#     vacancies=company.vacancy_set.all()
#     vacancies_json=[vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json,safe=False)


#to get values of vacancies we have to call all function
#company.vacancy_set return related manager
#to connect company and vacancy we use foreign key
#it means it automatically adds to company related name
#Company.vacancies_set.all()-return all vacancies of this company


@csrf_exempt
def  vacancies_list(request):
    if request.method=='GET':
        vacancies=Vacancy.objects.all()
        serializer=VacancySerializer(vacancies,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        data=json.loads(request.body)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors)

# def vacancies_list(request):
#     vacancies=Vacancy.objects.all()
#     json_vacancies= [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(json_vacancies,safe=False)

@csrf_exempt
def vacancies_detail(request,vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
            return JsonResponse({'error':str(e)})
    if request.method=='GET':
        serializer=VacancySerializer(vacancy)
        return JsonResponse(serializer.data,status=200)
    elif request.method=='PUT':
        data=json.loads(request.body)
        serializer=VacancySerializer(instance=vacancy,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors)
    elif request.method=='DELETE':
        vacancy.delete()
        return JsonResponse({},status=204)


# def vacancies_detail(request,vacancy_id):
#     try:
#         vacancy=Vacancy.objects.get(id=vacancy_id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error':str(e)})
#     return JsonResponse(vacancy.to_json())



@csrf_exempt
def vacancies_top(request):
    vac_top = Vacancy.objects.order_by('-salary')[:10]
    vac_json = [vacancy.to_json() for vacancy in vac_top]
    if request.method == 'GET':
        return JsonResponse(vac_json, safe=False)


# def topvacancies(request):
#     vac_top=Vacancy.objects.order_by("-salary")[:10]
#     vac_json=[vacancy.to_json() for vacancy in vac_json]
#     return JsonResponse(vac_json,safe=False)