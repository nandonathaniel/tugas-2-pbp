## Link Website
Link bisa diakses di [sini](https://tugas-2-pbp-fernando.herokuapp.com/todolist).
## Inline, Internal, External CSS


### Inline CSS
Inline CSS digunakan untuk tag HTML tertentu. Atribut ``<style>`` digunakan kepada tag HTML tertentu. Cara ini kurang disarankan, karena setiap tag HTML kita harus memberi `<style>` masing-masing yang mana akan membuang waktu dan lebih sulit untuk di-*handle*. Sebaliknya jika dilakukan pada moment  tertentu justru inline CSS menjadi berguna. Contohnya, ketika kita hanya ingin memberi CSS pada satu tag dan yang lain tidak ingin diberi CSS. Akibat dari penggunaan Inline CSS juga dia akan mengoverride seluruh CSS yang ada alias dia prioritas pertama.
Berikut adalah contoh Inline CSS
`<p style="color:white;">He's Cobham's Finest</p>`

### Internal CSS
Internal CSS diimplementasi pada `head` dalam suatu page HTML, pada tag`<style>`. Jadi semua fitur CSS pada Internal CSS hanya dijalankan pada page tersebut. Jadi berguna untuk ketika ingin mengubah CSS hanya pada satu halaman saja. Namun kelemahannya adalah memperlambat *load website* karena setiap ketika pindah page CSS harus di*load* ulang.
Berikut adalah contoh Internal CSS.
```
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: blue;
}
h1 {
    color: red;
    padding: 60px;
} 
</style>
</head>
<body>
 
<h1>He's one of our own</h1>
<p>There is no doubt</p>
 
</body>
</html>
```

### External CSS
External CSS diimplementasi pada file terpisah dengan page HTML. Jadi pada `body` HTML harus mengexport CSS. Keuntungannya ukuran file HTML jadi jauh lebih kecil dan kita tidak harus mengimplementasikan CSS berulang kali. Ini juga biasanya dilakukan jika ingin membuat website yang setiap pagenya CSSnya mirip-mirip. Jika ingin ada beda bisa menggunakan Inline CSS.
Berikut adalah contoh penggunaaan External CSS
```
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
```

## Tag HTML5

`<a>` tag element untuk hyperlink.
`<p>` tag element untuk paragraf/text
`<div>` tag element untuk mendefinisikan suatu division.
`<h1> <h2> <h3> <h4> <h5> <h6>` tag element untuk header yang ada bermacam ukuran
`<form>` tag element untuk form. Form akan berisi beberapa tag `<input>` untuk menyimpan data input dari user.
`<input>` tag element agar user dapat memberikan input.
`<style>` tag element untuk mendefinisikan internal CSS dalam suatu halaman HTML
`<head>` tag element untuk  metadata html.
`<body>` tag element untuk data html.
`<div>` tag element untuk unordered list
`<ol>` tag element untuk ordered list
`<li>` tag element untuk isi2 dari dari list `<ul>` atau `<ol>`.
`<img>` tag element untuk gambar.
`<button>` tag element untuk menekan tombol
`<table>` tag element untuk mendefinisikan tabel
dan masih banyak lagi.

## CSS Selector

- Element Selector
Selector yang langsung memanfaatkan tag HTML sebagai selector-nya. Untuk implementasinya, langsung memakai nama tag tersebut, seperti
```
h1 {
    color: blue;
}
```

- Class Selector
Selector yang langsung menggunakan class yang sudah didefinisikan pada tag sebagai selector-nya. Untuk implementasinya, memakai nama class pada tag tersebut, dan diberi `.` di depan
Berikut contohnya jika *class* nya bernama `student`
```
.student {
    color: blue;
}
```

- ID Selector
Selector yang langsung menggunakan ID yang sudah didefinisikan pada tag sebagai selector-nya. Untuk implementasinya, memakai nama id pada tag tersebut, dan diberi `#` di depan.
Berikut contohnya jika id nya bernama `thisimg`
```
#thisimg {
    color: blue;
}
```

## Penjelasan Implementasi

### Step 1
Memasukkan *Bootstrap* pada semua html dengan cara memasukkan link `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">` pada `base.html`. Karena semua page adalah `base.html` yang diextend.

### Step 2
Memodifikasi `login.html` mengganti nama *class* menjadi `login containers-fluid text-center mt-5` yang berarti ingin ditengah dan ada margin atas. Lalu button pada `login.html` lakukan mengganti nama *class* menjadi `btn btn-primary btn-lg btn-block`. Ini adalah kegunaan bootstrap. Lalu saya juga ada buat External CSS dengan melakukan Class Selector dll.

### Step 3
Memodifikasi `register.html` dengan tidak mengikut sertakan `form.as_table` agar lebih bisa diotak-atik. Jadi inspect HTML dari yang sebelumnya (yang memakai `form.as_table`). Lalu saya banyak menambahkan ID Selector untuk page ini.

### Step 4
Memodifikasi `todolist.html` dengan memakai `card` nya Bootstrap bisa memilih banyak pilihan pada link [berikut](https://getbootstrap.com/docs/4.0/components/card/). Lalu saya memberikan CSS class selector untuk mengatur margin dari card.

### Step 5
Memodifikasi `create-task.html` dengan memakai metode yang sama dengan `register.html`.

### Step 6
Menambah navbar untuk mempercantik pada semua page yang bisa dipilih pada link [berikut](https://getbootstrap.com/docs/4.0/components/navbar/).

### Step 7
Mengecek *responsive* sejauh yang saya lihat ketika memperbesar dan memperkecil ukuran dan membuka pada HP sudah cukup baik

### Step 8
Untuk hover card, menggunakan `.card:hover` pada `style.css`. Animasi yang dilakukan adalah memperbesar ukuran card sebesar 5%.

### Step 9
`add`, `commit`, `push` ke GitHub dan selesai.

## Akun

Berikut adalah dua akun dummy yang bisa dipakai untuk coba-coba

```
Username : dummy
Password : Chelsea1221

Username : dummy1
Password : Chelsea1221
```