import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { Company } from '../models';
import { CompaniesService } from '../companies.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-company-detail',
  imports: [RouterModule,CommonModule],
  templateUrl: './company-detail.component.html',
  styleUrl: './company-detail.component.css'
})
export class CompanyDetailComponent {
  company!: Company;
  isLoading = true; 

  constructor(private route: ActivatedRoute,
    private companiesService: CompaniesService) {

}

ngOnInit() {

  this.route.paramMap.subscribe((params) => {
  const companyID = Number(params.get('id'));


  this.companiesService.getCompany(companyID).subscribe((company: Company) => {
  this.company = company;
  this.isLoading = false;

  });


});
}
}
