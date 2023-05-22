# penjelasan singkat python-search
Percobaan 10 Binary Search_Rotation, Menemukan rotasi terkecil dalam sebuah list yang sudah dirotasi. 

1. Pertama, kita menginisialisasi dua variabel, low dan high. low diberi nilai 6, yang menunjukkan indeks awal yang akan digunakan dalam pencarian. high diberi nilai len(data) - 1, yang merupakan indeks terakhir dalam array.
2. Kemudian, kita menggunakan sebuah loop while untuk melakukan pencarian indeks rotasi terkecil. Loop ini akan berjalan selama low kurang dari high.
3. Di dalam loop, kita menghitung nilai tengah (mid) dari rentang pencarian saat ini dengan menggunakan rumus (low + high) // 2. Ini membagi interval pencarian menjadi dua bagian.
4. Selanjutnya, kita membandingkan elemen yang berada di indeks tengah (data[mid]) dengan elemen yang berada di indeks terakhir (data[high]). Jika elemen tengah lebih besar dari elemen terakhir, itu berarti rotasi terjadi di sebelah kanan elemen tengah. Oleh karena itu, kita mengubah low menjadi mid + 1 untuk mencari rotasi di sebelah kanan. Jika elemen tengah lebih kecil atau sama dengan elemen terakhir, itu berarti rotasi terjadi di sebelah kiri elemen tengah. Oleh karena itu, kita mengubah high menjadi mid untuk mencari rotasi di sebelah kiri.
5. Proses pencarian dilakukan dengan terus memperkecil rentang pencarian sampai low dan high memiliki nilai yang sama, yang menandakan bahwa kita telah menemukan indeks rotasi terkecil.
6. Setelah keluar dari loop, nilai low akan berisi indeks rotasi terkecil dalam array tersebut. Kita mengembalikan nilai low sebagai hasil dari fungsi binary_search_rotation().

Dalam contoh kode di atas, array my_list memiliki rotasi di indeks 4 (antara angka 9 dan 1). Oleh karena itu, hasil yang dicetak adalah "Indeks rotasi terkecil adalah 4"

Percobaan 11 Binary Search_Most Frequent, Menemukan elemen yang sering muncul paling banyak dalam sebuah list yang sudah diurutkan.

1. Pertama, kita menginisialisasi beberapa variabel. max_count untuk menyimpan frekuensi maksimum yang ditemukan, most_frequent untuk menyimpan elemen yang paling sering muncul, low sebagai indeks awal pencarian (diatur menjadi 0), dan high sebagai indeks akhir pencarian (diatur menjadi len(data) - 1).
2. Selama low kurang dari atau sama dengan high, kita melakukan langkah-langkah berikut:
a. Menghitung indeks tengah (mid) dari rentang pencarian saat ini dengan menggunakan rumus (low + high) // 2.
b. Kita menginisialisasi variabel count dengan nilai 1, yang akan digunakan untuk menghitung frekuensi kemunculan elemen.
c. Selanjutnya, kita menggunakan dua loop while untuk mencari elemen yang sama di sebelah kiri (left) dan sebelah kanan (right) elemen tengah. Loop tersebut akan berhenti ketika kita mencapai batas array atau ketika elemen yang dicek tidak sama dengan elemen tengah.
d. Di dalam loop, kita menambahkan 1 ke count setiap kali elemen yang sedang dicek sama dengan elemen tengah.
e. Setelah keluar dari loop, kita membandingkan nilai count dengan max_count. Jika count lebih besar dari max_count, maka kita mengupdate max_count dengan count dan most_frequent dengan elemen tengah (data[mid]).
f. Jika count adalah 1, itu berarti kita sudah menemukan elemen dengan frekuensi terbanyak dan tidak perlu mencari lebih lanjut. Oleh karena itu, kita keluar dari loop dengan menggunakan pernyataan break.
g. Jika masih ada kemungkinan elemen yang sama di sebelah kiri (left), kita mengubah high menjadi left untuk mencari lebih lanjut di sisi kiri.
h. Jika masih ada kemungkinan elemen yang sama di sebelah kanan (right), kita mengubah low menjadi right untuk mencari lebih lanjut di sisi kanan.
3. Setelah keluar dari loop, most_frequent akan berisi elemen yang paling sering muncul dalam array. Kita mengembalikan nilai most_frequent sebagai hasil dari fungsi binary_search_most_frequent().
Pada contoh kode di atas, array my_list memiliki elemen yang paling sering muncul adalah 8, dengan frekuensi 5. Oleh karena itu, hasil yang dicetak adalah "Elemen yang paling sering muncul adalah 8".

Percobaan 12 Binary Search_Name List, Mencari data dalam list terurut

Berikut adalah penjelasan langkah-langkah dalam kodingan tersebut:

1. Pertama, kita menginisialisasi variabel low dengan nilai 6 dan high dengan nilai len(data) - Ini menandakan rentang pencarian dalam list.
2. Selama low kurang dari atau sama dengan high, kita melakukan langkah-langkah berikut:
a. Menghitung indeks tengah (mid) dari rentang pencarian saat ini dengan menggunakan rumus (low + high) // 2.
b. Kita memeriksa apakah data yang berada di indeks tengah (data[mid]) sama dengan target yang dicari. Jika iya, itu berarti kita telah menemukan data target dan mengembalikan indeks tengah tersebut.
c. Jika data di indeks tengah kurang dari target, kita mengatur low menjadi mid + 1 untuk mencari di sebelah kanan.
d. Jika data di indeks tengah lebih besar dari target, kita mengatur high menjadi mid - 1 untuk mencari di sebelah kiri.
3. Jika kita keluar dari loop tanpa menemukan data target, artinya data target tidak ada dalam list. Oleh karena itu, kita mengembalikan nilai -1 sebagai penanda bahwa data tidak ditemukan.
4. Pada bagian utama kodingan, kita meminta pengguna memasukkan nama yang ingin dicari melalui input. Kemudian, kita menjalankan fungsi binary_search dengan argumen names (list yang akan dicari) dan target_name (nama yang ingin dicari).
5. Jika index tidak sama dengan -1, itu berarti nama ditemukan dalam list. Kita mencetak pesan "Nama ditemukan pada indeks" diikuti dengan nilai index.
6. Jika index sama dengan -1, itu berarti nama tidak ditemukan dalam list. Kita mencetak pesan "Nama tidak ditemukan".

Dengan menggunakan kodingan tersebut, pengguna dapat mencari data (nama) dalam list names yang telah terurut secara alfabetis.
