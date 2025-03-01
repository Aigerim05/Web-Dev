import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-album-photos',
  imports: [CommonModule],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.scss'
})
export class AlbumPhotosComponent implements OnInit{
  photos: any[] = [];
  loaded: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private client: HttpClient,
    private router: Router
  ){}

  ngOnInit(): void{
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.client.get(`https://jsonplaceholder.typicode.com/albums/${id}/photos`).subscribe((photos: any) => {
      this.photos = photos;
      this.loaded = true;
    })
  }

  return(): void{
    this.router.navigate(['/albums']);
  }
}
