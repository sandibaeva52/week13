import { Component, OnInit } from '@angular/core';
import { Company } from '../company';
import { CompanyService } from '../company.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import {Vacancy} from '../vacancy';
import {VacancyService} from '../vacancy.service';
@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
company:Company;
vacancies: Vacancy[];
  constructor(
    private companyService:CompanyService,
    private vacancyService: VacancyService,
    private route:ActivatedRoute,
    private location: Location) { }

  ngOnInit(): void {
    this.getCompany();
    this.getVacanciesByCompanyId();
  }
  getCompany() {
    const id = +this.route.snapshot.paramMap.get('id');

    this.companyService.getCompany(id).subscribe(company => this.company = company);
}
goBack(): void {
  this.location.back();
}

getVacanciesByCompanyId() {
  const id = +this.route.snapshot.paramMap.get('id');
  this.vacancyService.getVacanciesByCompanyId(id)
    .subscribe(vacancies => this.vacancies = vacancies);
}

}
