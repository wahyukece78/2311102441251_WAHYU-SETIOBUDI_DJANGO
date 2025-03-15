# 2311102441251_WAHYU-SETIOBUDI_DJANGO

# Personal Portfolio

Website ini merupakan portfolio pribadi saya yang berisi tentang informasi diri saya.

## Ada apa saja isi dihalaman website saya?

1. alaman Home - Menampilkan ringkasan dari setiap halaman yang ada di website.
2. Halaman About - Berisi tulisan yang saya buat untuk memperkenalkan diri lebih jauh.

## setelah itu saya menambahkan apps pada project saya
1. app Berita - Menampilkan berita terkini.
2. app Pengguna - Mengelola data pengguna.

## Cara Menjalankan Project
1. buka command prompt
2. Arahkan ke folder tempat web kita berada
3. setelah itu kita buat venv, saya memakai env. dengan mengetik 
```
py -m venv .venv
```
4. untuk mengaktifkannya, kita masuk ke folder env, masuk lagi ke folder Scripts, setelah itu kita ketik 
```
activate
```
5. kita sudah didalam lingkungkan virtual, setelah itu kita install django-nya dengan mengetik 
```
pip install django
```
6. dan kemudian kita membuat project baru django dengan mengetik  (saya menggunakan portofolio)
```
django-admin startproject websiteku
```
7. setelah itu jika ingin membuat apps kita bisa mengetik
```
python manage.py startapp "kita dapat membuat sesuai keinginan kita"
```
8. serelah itu, untuk membuat migration kita dapat mengetikkan
```
python manage.py makemigrations "nama apps yang kita buat"
```
9. Setelah project dan apps telah dibuat dan untuk mengeceknya kita bisa mengetik 
```
py manage.py runserver
```