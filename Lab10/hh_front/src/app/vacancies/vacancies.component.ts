import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-vacancies',
  imports: [CommonModule,],
  templateUrl: './vacancies.component.html',
  styleUrl: './vacancies.component.css'
})
export class VacanciesComponent {
  vacancies: any[] = [];
  constructor(
    private route: ActivatedRoute,
    private client: HttpClient,
    private router: Router
  ){}

  ngOnInit(): void{
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.client.get(`http://127.0.0.1:8000/api/companies/${id}/vacancies/`).subscribe((vacancies: any) => {
      this.vacancies = vacancies;
      
    })
  }
}
