from django.urls import path
from api import views
from api.views.views_cbv import CompanyListAPIView,CompanyDetailAPIView,CompanyWithVacanciesListAPUView,VacancyListAPIView,VacancyDetailAPIView,TopVacanciesListAPIView
# from api.views.views_generic import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView,VacancyDetailAPIView, CompanyWithVacanciesListAPUView, TopVacanciesListAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    # path('companies/', companies_list),
    # path('companies/<int:company_id>/', companies_detail),
    # path('companies/<int:company_id>/vacancies/', company_vacancies),
    # path('vacancies/', vacancies_list),
    # path('vacancies/<int:vacancy_id>/', vacancies_detail),
    # path('vacancies/top_ten/', topvacancies)
    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyWithVacanciesListAPUView.as_view()),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', TopVacanciesListAPIView.as_view())

]
