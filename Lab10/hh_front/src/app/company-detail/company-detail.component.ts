import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { Company } from '../models';
import { CompaniesService } from '../companies.service';

@Component({
  selector: 'app-company-detail',
  imports: [RouterModule,],
  templateUrl: './company-detail.component.html',
  styleUrl: './company-detail.component.css'
})
export class CompanyDetailComponent {
  company!: Company;


  constructor(private route: ActivatedRoute,
    private postsService: CompaniesService) {

}

ngOnInit() {

  this.route.paramMap.subscribe((params) => {
  const companyID = Number(params.get('id'));


  this.postsService.getCompany(companyID).subscribe((company: Company) => {
  this.company = company;

  });


});
}
}
