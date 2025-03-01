import { Component, OnInit } from '@angular/core';
import { Album } from '../models';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AlbumService } from '../album.service';

@Component({
  selector: 'app-albums',
  imports: [CommonModule, RouterModule ],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.scss'
})
export class AlbumsComponent implements OnInit{
  albums!: Album[];
  loaded: boolean = false;

  constructor(private albumService: AlbumService){
  }

  ngOnInit(){
    this.loaded = false;
    this.albumService.getAlbums().subscribe((albums: Album[]) => {
      this.albums = albums;
      this.loaded = true;
    })
  }

  deleteAlbum(id:number): void{
    this.albumService.deleteAlbum(id).subscribe(()=>{
      this.albums = this.albums.filter(album => album.id !== id)
    })
  }
}
