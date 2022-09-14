## Link Website
Berikut adalah sitenya, akses [disini](https://tugas-2-pbp-fernando.herokuapp.com/katalog/).

## Bagan *request client* ke Django
![](https://i.imgur.com/inHVqhq.jpg)

- User memberikan HTTP Request berupa URL,lalu langsung diteruskan ke `urls.py`
- Pada `urlpatterns` di `urls.py`dicek URL yang user minta. Jika ada langsung diteruskan ke `views.py`. Jika tidak ada pasti langsung keluar peringatan error.
- `views.py` lalu akan melakukan *query* ke `models.py`  jika dibutuhkan, dilanjutkan `models.py` dan Database melakukan tranksaksi data, lalu segera data yang dibutuhkan segera diberi ke `views.py`
- Sekarang `views.py` sudah mendapatkan data yang diinginkan. Segera `views.py` me*render* request tsb dengan memilih template html yang sesuai pada `/templates`. Template html tsb pastinya akan menggunakan data yang tadi sudah diminta dan akhirnya sudah didapat.
- HTML tersebut itulah yang tampil di web browser pengguna

## Virtual Environment
Virtual Environment adalah tools untuk membuat lingkungan Python virtual yang terisolasi. Terisolasi dalam arti tertutup dan tidak bisa diakses dari dunia luar.

### Mengapa menggunakan virtual environment?

Kita direkomendasikan untuk menggunakan venv setiap kali kita membuat project baru. Karena, hal ini berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan update di library yang sama pada project lain.

Contohnya seperti ini. Misalkan ada project A memakai library X versi 1, project ini dikatakan bergantung pada library X versi 1. Kemudian suatu ketika dilakukan update library X menjadi versi 2. Ini menyebabkan project 1 tidak bisa berjalan dengan baik menggunakan library X versi 2. Sedangkan beberapa project ada yang sudah terlanjur dibangun dengan library X versi 2. Untuk mengisolasi agar tiap project menggunakan library X dengan versinya masing-masing maka digunakanlah virtual environment

Akhirnya, kita bisa buat project A di virtual environment yang menggunakan library X versi 1 dan beberapa project yang lain di virtual environment yang lain dengan menggunakan library X versi 2.

### Apakah kita dapat membuat aplikasi Django tanpa virtual environment?

Tentunya tetap bisa. Namun ada banyak hambatan dan tantangan. Seperti penjelasan yang ada di atas, akan terjadi konflik antara beberapa project yang sudah pernah dibuat atau bahkan yang di masa depan akan dibuat. Terutama ketika memakai library yang sama di project-project tsb. Jadi tetap disarankan untuk memakai virtual environment.

## Penjelasan Implementasi
### Step 1
Agar bisa melakukan pengambilan data dari `models.py`, maka pertama *import* lah `CatalogItem` dari `models.py`.
Setelah itu saya membuat fungsi `show_catalog` yang menerima request dari user sebagai satu-satunya parameter, dan mengembalikan *render* HTML yang dipilih (yaitu `katalog.html`) sekaligus membawa context data yang dibutuhkan yaitu (nama, NPM, dan `CatalogItem.objects.all()`).


### Step 2
Pada `katalog/urls.py` daftarkan fungsi `show_catalog` yang sudah dibuat sebelumnya dengan implementasi `path('', show_katalog, name='show_katalog')`

Agar hal diatas dapat terlaksanakan dengan sempurna, perlu dibuat path juga pada `project_django/urls.py` sebagai berikut.
Membuat route baru yang bernama `katalog/` dengan implementasi `path('katalog/', include('katalog.urls'))` agar semua path (yang mana sebenarnya di katalog hanya ada 1) pada `katalog.urls` bisa dilaksanakkan.

### Langkah 3
Pada `katalog/templates/katalog.html` ubah `Fill Me!` menjadi ``{{nama}}`` dan `{{npm}}`. Lalu untuk menampilkan data, diperlukan perulangan untuk menampilkan semua katalog (pada implementasi saya namanya `all_Catalog`), dan jangan lupa pergunakan `{{}}`.

### Langkah 4
Beruntungnya `Procfile`, `github/workflows/dpl.yml`, pengaturan pada `settings.py` sudah dilengkapkan di template. Jadi saya hanya perlu mencantumkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` pada *Github* dan membuat app baru di *herokuapp*. Dan jalankan kembali *Actions* yang gagal setelah lakukan itu semua lalu berhasil deh!
