import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { CommonModule } from '@angular/common';
import { CompaniesService } from '../companies.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-companies',
  imports: [CommonModule,RouterModule],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent implements OnInit{
  companies!: Company[];

  constructor(private companiesService: CompaniesService){
    
  }

  ngOnInit(){
    this.companiesService.getCompanies().subscribe((companies: Company[]) => {
      this.companies = companies;
      
    })
  }
}
