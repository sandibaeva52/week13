from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Company,Vacancy
from api.serializers import CompanySerializer2,VacancySerializer
from rest_framework import status


class CompanyListAPIView(APIView):
    def get(self,request):
        companies=Company.objects.all()
        serializer=CompanySerializer2(companies,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyDetailAPIView(APIView):
    def get_object(self,id):
        try:
             return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
    def get(self,request,company_id):
        company=self.get_object(company_id)
        serializer = CompanySerializer2(company)
        return Response(serializer.data)
    def put(self,request,company_id):
        company=self.get_object(company_id)
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    def delete(self,request,company_id):
        company=self.get_object(company_id)
        company.delete()
        return Response({'deleted': True})
class CompanyVacanciesListAPIView(APIView):
    def get(self, request, company_id):
        try:
            vacancies = Vacancy.objects.filter(company_id=company_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)
class CompanyWithVacanciesListAPUView(APIView):
    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VacancyListAPIView(APIView):
    def get(self, request):
        try:
            vacancies = Vacancy.objects.all()
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
        serializer = VacancySerializer(vacancies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacancyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        vacancy.delete()

        return Response({'deleted': True})


class TopVacanciesListAPIView(APIView):
    def get(self, request):
        try:
            top_vacancies = Vacancy.objects.order_by('-salary')[:10]
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = VacancySerializer(top_vacancies, many=True)
        return Response(serializer.data)