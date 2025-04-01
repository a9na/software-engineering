# Images app
## Rute
- localhost:8000/  - homepage
- localhost:8000/images/ - index slika
- localhost:8000/images/:id/ - detail slike

## Viewovi
- homepage -> views.home
- index -> views.index
- detail -> views.detail

## Templatei
- homepage -> home.html
- index -> index.html
- detail -> detail.html

## Modeli

Image
---------
id -> int primary key autoincrement
title -> string
url -> string
created_at -> datetime