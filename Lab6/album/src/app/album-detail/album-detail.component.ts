import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router, RouterModule } from '@angular/router';
import { Album } from '../models';
import { AlbumService } from '../album.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-album-detail',
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.scss'] 
})
export class AlbumDetailComponent implements OnInit { 
  album!: Album; 
  loaded: boolean = false;

  constructor(private route: ActivatedRoute,
              private albumService: AlbumService, 
              private router: Router) {

    this.loaded = false;
  }

  ngOnInit() {
    this.route.paramMap.subscribe((params) => {
      const albumID = Number(params.get('id')); 

      this.loaded = false;

      this.albumService.getAlbum(albumID).subscribe((album:Album) => {
        this.album = album;
        this.loaded = true;
      })
    });
  }

  save(): void{
    this.albumService.updateAlbum(this.album).subscribe(() => {
      alert('updated title successfully');
    } )
  }

  return(): void{
    this.router.navigate(['/albums']);
  }
}
