from django.urls import path, re_path
from .views import company_list,company_detail, vacancy_list,vacancy_detail, company_vacancies,top_ten_vacancies
urlpatterns=[
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top_ten_vacancies),

]
