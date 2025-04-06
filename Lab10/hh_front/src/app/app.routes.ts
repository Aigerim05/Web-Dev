import { Routes } from '@angular/router';
import { CompaniesComponent } from './companies/companies.component';
import { CompaniesService } from './companies.service';
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import { VacanciesComponent } from './vacancies/vacancies.component';

export const routes: Routes = [
    {path: 'companies', component:CompaniesComponent},
    {path: 'companies/:id', component:CompanyDetailComponent},
    {path: 'companies/:id/vacancies', component:VacanciesComponent}
];
