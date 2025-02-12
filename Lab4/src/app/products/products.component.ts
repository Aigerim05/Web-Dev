import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 

@Component({
  selector: 'app-products',
  imports: [CommonModule],
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})


export class ProductsComponent {
  products = [
    {
      name: 'Стекло А-case для Oppo A72',
      description: 'Это удобное и практичное решение для сохранения экрана устройства в хорошем состоянии. Они помогают минимизировать риск появления царапин, потертостей и следов от пальцев. Прозрачный материал обеспечивает высокую четкость изображения, сохраняя естественную цветопередачу и чувствительность сенсора.',
      rating: '5/5',
      imageUrl: '/p1.jpg',
      productLink: 'https://kaspi.kz/shop/p/steklo-a-case-dlja-oppo-a72-110400022/?c=750000000'
    },
    {
      name: 'Зарядное устройство Apple 18W USB-C Power Adapter USB Type-C белый',
      description: 'Адаптер Apple 18W USB-C Power Adapter представляет собой компактное и эффективное зарядное устройство, предназначенное для быстрой и эффективной зарядки ваших устройств.',
      rating: '5/5',
      imageUrl: '/p2.jpg',
      productLink: 'https://kaspi.kz/shop/p/apple-18w-usb-c-power-adapter-usb-type-c-belyi-102743952/?c=750000000'
    },
    {
      name: 'Чехол Для Apple iPhone 13 прозрачный',
      description: 'Надежный и стильный чехол для вашего смартфона, обеспечивающий защиту от царапин, ударов и загрязнений. Идеально повторяет форму устройства, сохраняя удобный доступ ко всем кнопкам, портам и камере.',
      rating: '5/5',
      imageUrl: '/p3.jpeg',
      productLink: 'https://kaspi.kz/shop/p/dlja-apple-iphone-13-prozrachnyi-106185651/?c=750000000'
    },
    {
      name: 'Зарядное устройство Apple 20W USB-C Power Adapter белый',
      description: 'Адаптер питания Apple USB‑C мощностью 20 Вт дает возможность быстро и эффективно заряжать гаджеты. Проверяется на основном сайте через QR на оригинальность.',
      rating: '5/5',
      imageUrl: '/p4.jpg',
      productLink: 'https://kaspi.kz/shop/p/apple-20w-usb-c-power-adapter-belyi-100984093/?c=750000000'
    },
    {
      name: 'Смартфон Xiaomi Redmi 13C 8 ГБ/256 ГБ черный',
      description: 'Этот смартфон сочетает в себе стильный дизайн, мощную производительность и инновационные функции, чтобы удовлетворить все ваши потребности.',
      rating: '4.7/5',
      imageUrl: '/p5.jpg',
      productLink: 'https://kaspi.kz/shop/p/xiaomi-redmi-13c-8-gb-256-gb-chernyi-114695323/?c=750000000'
    },
    {
      name: 'Смартфон Apple iPhone 13 128Gb черный',
      description: 'Apple iPhone 13 получил дисплей 6.1 дюйма Super Retina XDR, который отличается невероятно высокой плотностью пикселей — фотографии, видео и текст выглядят поразительно четко. А благодаря уменьшенной площади камеры TrueDepth на дисплее теперь больше места для изображения.',
      rating: '5/5',
      imageUrl: '/p6.jpg',
      productLink: 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-chernyi-102298404/?c=750000000'
    },
    {
      name: 'Чехол JS0000084 серебристый',
      description: 'Этот элегантный аксессуар не только эффективно защищает от повреждений, но и придает вашему устройству современный и изысканный стиль.',
      rating: '5/5',
      imageUrl: '/p10.jpg',
      productLink: 'https://kaspi.kz/shop/p/js0000084-serebristyi-110564899/?c=750000000'
    },
    {
      name: 'Чехол Для Apple iPhone 11 прозрачный',
      description: 'Легкий, но при этом максимально- надежный чехол для Apple iPhone 11. Усиленные углы чехла - снижают силу удара на 30%. Полная защита камеры и выступающие над поверхностью экрана бортики - создают дополнительную защиту для экрана и камеры телефона.',
      rating: '5/5',
      imageUrl: '/p7.jpg',
      productLink: 'https://kaspi.kz/shop/p/dlja-apple-iphone-11-prozrachnyi-103661424/?c=750000000'
    },
    {
      name: 'Чехол NRS1708 розовый',
      description: 'Чехол изготовлен из прочного и гибкого материала, который обеспечивает надежную защиту от повреждений при ежедневном использовании.',
      rating: '4.8/5',
      imageUrl: '/p8.jpg',
      productLink: 'https://kaspi.kz/shop/p/nrs1708-rozovyi-112638500/?c=750000000'
    },
    {
      name: 'Кабель Apple Lightning (M), USB TypeC (M) белый',
      description: 'Кабель Apple USB Type-C - Lightning длиной 1 м удобен для подключения iPhone, iPad или iPod с разъёмом Lightning к устройствам с портом USB Type-C или Thunderbolt 3 для синхронизации и подзарядки.',
      rating: '4.9/5',
      imageUrl: '/p9.jpeg',
      productLink: 'https://kaspi.kz/shop/p/kabel-apple-lightning-m-usb-typec-m-belyi-40500508/?c=750000000'
    }
  ];
  

  shareProduct(productLink: string): void {
    const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(productLink)}`;
    window.open(telegramUrl, '_blank');
  }
}
