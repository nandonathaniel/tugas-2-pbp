## Link Website
HTML : [link](https://tugas-2-pbp-fernando.herokuapp.com/mywatchlist/html)
XML  : [link](https://tugas-2-pbp-fernando.herokuapp.com/mywatchlist/xml)
JSON : [link](https://tugas-2-pbp-fernando.herokuapp.com/mywatchlist/json)
## JSON, XML, HTML

Secara garis besar, HTML, JSON, XML merupakan format data delivery yang sering dipakai di Django. Tetapi, XML dan JSON lebih menitikberatkan struktur dan konteks data tersebut. Sedangkan HTML menitikberatkan bagaimana format tampilan dari data tersebut muncul di halaman web.

Berdasarkan cara menyimpan elemennya, JSON lebih efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien. Berdasarkan penerapannya, JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.

- XML
*Extensible Markup Language* (XML) adalah bahasa komputer yang dibuat oleh World Wide Web Consortium (W3C) untuk menyederhanakan proses pertukaran dan penyimpanan data. Pada implementasinya menggunakan format *markup* seperti HTML.

- JSON
*JavaScript Object Notation* (JSON) adalah turunan JavaScript yang digunakan dalam transfer dan penyimpanan data. Pada implementasinya banyak menggunakan kurung krawal `{}` yang berisi data berformat *key* dan *value* yang mirip dengan *dictionary* nya Python.

- HTML
*HyperText Markup Language* (HTML) adalah bahasa *markup* yang digunakan untuk menampilkan halaman website. Biasanya disandingkan dengan CSS untuk membuat halaman website.

## Data Delivery

Data delivery digunakan untuk alat komunikasi antara client dan server. Client ingin halaman web menampilkan sesuatu yang dia inginkan, digunakan Data delivery untuk mempercepat pengiriman data. Penyampaian data seringkali dalam format JSON, XML, atau format penyampaian data lainnya. 

## Penjelasan Implementasi

### Step 1
Karena memakai proyek dari tugas 2, maka pertama kali yang kita lakukan adalah membuat app baru dengan cara ini `python manage.py startapp mywatchlist`, jangan lupa tambahkan `mywatchlist` pada `settings.py`.

### Step 2
Membuat models baru dengan nama "MyWatchList" di `mywatchlist/models.py` sesuai dengan attribute-attribute yang disebutkan pada deskripsi tugas

### Step 3
Membuat file json yang menjadi data film-film pada `initial_mywatchlist_data.json` pada `mywatchlist/fixtures/`.

### Step 4
Lakukan `makemigrations`, `migrate`, `loaddata`

### Step 5
Buat `show_html`, `show_xml`, `show_json` di `mywatchlist/views.py`. Untuk `show_html`, sekalian bawa `nama`, `npm`, isi-isi dari `MyWatchList` dan boolean yang menyatakan apakah sudah banyak menonton film (caranya tinggal iterasi dari seluruh film, berapa banyak yang sudah ditonton dan belum (bonus)). Untuk `show_xml` dan `show_json` hanya membawa isi-isi dari `MyWatchList`.

### Step 6
Pada `mywatchlist/urls.py` daftarkan fungsi `show_html`, `show_xml`, `show_json` yang sudah dibuat sebelumnya.

Agar hal diatas dapat terlaksanakan dengan sempurna, perlu dibuat path juga pada `project_django/urls.py` sebagai berikut.
Membuat route baru yang bernama `mywatchlist/` dengan implementasi `path('mywatchlist/', include('mywatchlist.urls'))` agar semua path pada `mywatchlist.urls` bisa dilaksanakkan.

### Step 7
Membuat `mywatchlist.html` pada `mywatchlist/templates`

### Step 8
Membuat `tests.py` agar bisa mengembalikan respon HTTP 200 OK

### Step 9
Update `Procfile` dan tambahkan `python manage.py loaddata initial_watchlist_data.json`

### Step 10
Push ke Github, dan deployment pada herokuapp akan berjalan secara otomatis.

## Postman

### XML
![](https://i.imgur.com/gVsZJEv.jpg)
### JSON
![](https://i.imgur.com/A0H2DJQ.jpg)
### HTML
![](https://i.imgur.com/YO3JwZ7.jpg)