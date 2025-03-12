# 2311102441251_WAHYU-SETIOBUDI_DJANGO

# Personal Portfolio

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)


## Deskripsi Singkat
Proyek ini adalah website portofolio yang dibuat menggunakan Django, yang terdiri dari dua halaman utama: My Home dan My About.

## Ada apa saja di website ini
1. My Home: Halaman utama yang menampilkan informasi portofolio.
2. My About: Halaman tentang yang memberikan detail lebih lanjut tentang pembuat portofolio


# Cara menjalankan project
1. clone repository
```
git clone https://github.com/wahyukece78/2311102441251_WAHYU-SETIOBUDI_DJANGO.git
```
2. Buat virtual environment 
```
python -m venv .venv
```
3. Aktifkan virtual environment: 
```
.venv\Scripts\activate
```
4. Install Django:
```
pip install django
```
5. Cek apakah Django sudah terinstall:
```
pip list
```
6. Buat project Django:
```
django-admin startproject portofolio
``` 
7. Jalankan server:
```
py manage.py runserver
```
8. untuk melihat halaman my home
```
http://127.0.0.1:8000/
```
9. untuk melihat halaman my about
```
http://127.0.0.1:8000/about/
```