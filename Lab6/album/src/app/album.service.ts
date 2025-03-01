import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Album } from './models';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {

  constructor(private client: HttpClient) {}


  getAlbums(): Observable<Album[]>{
    return this.client.get<Album[]>('https://jsonplaceholder.typicode.com/albums');
  }

  getAlbum(id: number): Observable<Album> {
    return this.client.get<Album>(`https://jsonplaceholder.typicode.com/albums/${id}`);
  }

  updateAlbum(album: Album): Observable<Album>{
    return this.client.put<Album>(`https://jsonplaceholder.typicode.com/albums/${album.id}`, album);

  }

  deleteAlbum(id: number): Observable<void>{
    return this.client.delete<void>(`https://jsonplaceholder.typicode.com/albums/${id}`);
  }

}
