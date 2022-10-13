## Link Website
Link bisa diakses di [sini](https://tugas-2-pbp-fernando.herokuapp.com/todolist).
## Perbedaan antara Asynchronous Programming dengan Synchronous Programming
Synchronous Programming menjalankan code secara berurutan, baris per baris. Jadi baris selanjutnya tidak akan diproses jika baris sebelumnya belum selesai.

Asynchronous Programming berarti tidak perlu menunggu baris sebelumnya selesai. Ini membuat banyak operasi/baris bisa dijalankan sekaligus. Menghemat banyak waktu dibanding synchronous programming.
## Event-Driven Programming
Event-driven programming adalah suatu paradigma dimana alur yang dijalankan suatu program didasarkan atas event atau perilaku yang dilakukan antar user dan client. Seperti arti secara harafiah, programmnya disetir sama event-event. Sehingga terjadi pengiriman "pesan" yaitu event yang ingin diproses, lalu program akan memanggil perintah-perintah berdasarkan event yang didapat.

Pada Tugas 6, contoh Event-Driven Programming ini dilakukan ketika user pencet tombol submit (`document.getElementById("submit").onclick = addTodolist`) setelah isi form add task lalu program akan melaksanakan `/add` untuk menambahkan ke HTML.

## Asynchronous Programming pada AJAX
Karena menggunakan AJAX, website mengirimkan request dan menerima response secara asynchronous. Ketika response dari server sampai ke browser, AJAX akan melakukan update website dari background. Karena response diterima secara asynchronous, website masih bisa **digunakan** oleh user meskipun AJAX sedang menunggu response server. Jadi, user dapat terus menerus menggunakan website tanpa perlu menunggu setiap kali user melakukan sesuatu dalam website. Jadi pada intinya, browser akan berjalan seperti biasa walau ada operasi yang sedang berjalan pada AJAX.

## Penjelasan Implementasi

### Step 1
Menambahkan fungsi `show_todolist_json` pada `todolist/views.py` yang mengembalikan data JSON, sekaligus menambah routenya (`/json`) pada `urls.py`

### Step 2
Menambahkan fungsi `add_task_ajax` pada `todolist/views.py` sekaligus menambahkan routenya (`add/`) pada `urls.py`. Fungsi ini berfungsi untuk menambahkan task setelah pencet tombol submit pada form `Add task`.

### Step 3
Untuk AJAX GET, karena sudah ada `todolist/json`, kita lakukan fetch untuk mengambil data JSON ketika diperlukan.

### Step 4
Memodifikasi `todolist.html` dengan memakai modal pada Bootstrap untuk formnya dengan bisa memilih banyak pilihan pada link [berikut](https://getbootstrap.com/docs/5.2/components/modal/).

### Step 5
Untuk AJAX POST, karena sudah ada `todolist/add`, Buatlah fungsi `addTodolist` yang hanya dijalankan ketika menekan tombol submit dengan menambahkan onclick pada script. Fungsi tersebut akan melakukan fetch pada `/todolist/add` dan akan melakukan refresh secara asinkronus menggunakan fungsi AJAX GET yang sudah dibuat sebelumnya.

## Akun

Berikut adalah dua akun dummy yang bisa dipakai untuk coba-coba

```
Username : dummy
Password : Chelsea1221

Username : dummy1
Password : Chelsea1221
```