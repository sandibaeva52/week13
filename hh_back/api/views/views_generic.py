from rest_framework import generics
from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer, CompanyWithVacanciesSerializer
from rest_framework.permissions import IsAuthenticated


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    # permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class CompanyWithVacanciesListAPUView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyWithVacanciesSerializer


class TopVacanciesListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer
