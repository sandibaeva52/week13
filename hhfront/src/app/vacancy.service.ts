import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import {Vacancy} from './vacancy';


@Injectable({
  providedIn: 'root'
})
export class VacancyService {

  BASE_URL='http://localhost:8000'

  constructor(private http: HttpClient) {
  }

  getVacanciesByCompanyId(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
  }
}