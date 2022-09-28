## Link Website
Link bisa diakses di [sini](https://tugas-2-pbp-fernando.herokuapp.com/todolist).
## `{% csrf_token %}`

Kegunaan `{% csrf_token %}` adalah untuk generate token random yang tidak dapat diketahui siapapun. Jadi jika ada request tanpa CSRF Token yang tepat, maka pasti request tersebut ditolak. 

Terkadang oknum-oknum orang tidak bertanggung jawab menyematkan file berupa link, image dll. yang mana jika dibuka bisa terdapat malicious code. Yang mana membuat kita tidak sadar mengirim request ke website yang sedang digunakan. Di kejadian seperti inilah `{% csrf_token %}` berguna.

Jika tidak ada {% csrf_token %} maka penyerang/hacker dapat melakukan CSRF terhadap request yang berhubungan dengan form tersebut.

## `<form>` manual

Tentunya bisa membuat `<form>` manual tanpa `{{form.as_table}}`. Kita bisa melakukan sesuka hati kita pada HTML. Untuk membuat sebuah <form>, berarti berisi beberapa <input> yang bertype = "text" (yang menjadi data2 yang ingin disubmit) dan satu <input> yang bertype = submit (yang menjadi tombol untuk disubmit). Contoh kode seperti pada `create-task.html` milik saya sebagai berikut
```py
<form method="POST" >  
            {% csrf_token %}  
            <table>  
                <tr>
                    <td>Judul: </td>
                    <td><input type="text" name="title" placeholder="Title"></td>
                </tr>
                        
                <tr>
                    <td>Deskripsi: </td>
                    <td><input type="text" name="description" placeholder="Description"></td>
                </tr>
    
                <tr>
                    <td></td>
                    <td><input type="submit" value="Submit"></td>
                </tr>
            </table>  
        </form>
```
    
## Alur data

User submit data melalui HTML form, data tersebut akan dilihat dalam variabel `request.POST`, lalu akan diambil `views.py` dan dilakukan `save()` atau `create()` lalu data tersebut tersimpan di db.sqlite3.

Jika ingin ditampilkan dalam HTML, ambilah dari database melalui `views.py` lalu barulah beri ke HTML yang diinginkan untuk ditampilkan

## Penjelasan Implementasi

### Step 1
Karena memakai proyek dari tugas 3, maka pertama kali yang kita lakukan adalah membuat app baru dengan cara ini `python manage.py startapp todolist`, jangan lupa tambahkan `todolist` pada `settings.py`.

### Step 2
Membuat models baru dengan nama "Task" di `todolist/models.py` sesuai dengan attribute-attribute yang disebutkan pada deskripsi tugas

### Step 3
Untuk `login` dan `register` ikuti seperti Tutorial 3 (tambahkan di pathnya dan bikin fungsi di     `views`, bikin html juga). Khususnya untuk `register`, menggunakan `UserCreationForm` dan pada htmlnya menggunakan {{ form.as_table }}.

### Step 4
Menyiapkan 2 html file pada `templates` yaitu `create-task.html` dan `todolist.html`, lalu siapkan kerangkanya. Terutama untuk `todolist.html`, siapkan tempat untuk memberitahu pemilik akun sekarang dan 2 tombol yaitu tombol logout dan tombol `Bikin task baru`.

### Step 5
Menambahkan `show_todolist` pada `views.py`.
```python
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    all_tasks = Task.objects.filter(user = request.user)
    context = {
        'list_tasks': all_tasks,
        'pemilik': request.user,
    }
    return render(request, "todolist.html", context)
```
Perhatikan bahwa kita harus login terlebih dahulu, dan membawa `request.user` dan `all_tasks` yaitu tasks yang pernah dibuat user tersebut, yang akan dikirim ke `todolist.html`.

### Step 6
Menambahkan `create_task` pada `views.py`.
```python
def create_task(request):
    if request.method == 'POST':
        judul = request.POST.get("title")
        desc = request.POST.get("description")
        Task.objects.create(user = request.user, date = timezone.now(), title = judul, description = desc)

        messages.success(request, 'Task baru telah berhasil ditambah!')
        return redirect('todolist:show_todolist')

    context = {}
    return render(request, 'create-task.html', context)
```
Perhatikan bahwa `request.method` harus `POST`, yang berarti memang sudah terbuat task baru, lalu kita dapatkan `title` dan `description` yang diinput dan masukkan waktu sekarang dan usernya, lalu langsung direct ke `show_todolist`. Perhatikan untuk ke `create-task.html` kita ga perlu bawa data apa-apa.

### Step 7
Pada `todolist/urls.py` daftarkan fungsi `login`, `logout`, `register`, `create_task`, `show_todolist` yang sudah dibuat sebelumnya.

Agar hal diatas dapat terlaksanakan dengan sempurna, perlu dibuat path juga pada `project_django/urls.py` sebagai berikut.
Membuat route baru yang bernama `todolist/` dengan implementasi `path('todolist/', include('todolist.urls'))` agar semua path pada `todolist.urls` bisa dilaksanakkan.

### Step 7
Melakukan `makemigrations`, `migrate`, `runserver`.

### Step 8
Push ke Github, dan deployment pada herokuapp akan berjalan secara otomatis.

## Akun

Berikut adalah dua akun dummy yang bisa dipakai untuk coba-coba

```
Username : dummy
Password : Chelsea1221

Username : dummy1
Password : Chelsea1221
```