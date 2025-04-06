import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Company } from './models';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {
  
  constructor(private client: HttpClient) { 

  }
  getCompanies():Observable<Company[]>{
    return this.client.get<Company[]>('http://127.0.0.1:8000/api/companies/')
  }


  getCompany(id: number): Observable<Company>{
    return this.client.get<Company>(`http://127.0.0.1:8000/api/companies/${id}/`);
  }

}

