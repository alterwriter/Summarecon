# Final Project Python - Subdomain-Reconnaissance

## LEMON SQUASH
:fire: (An Automatic Scanning Tool) :fire:

Sebuah tool yang biasa kita dengar dengan scraping, namun dalam scanning, kita hanya
memetakan serta mendeteksi kumpulan data dan lalu lintas yang berada pada sebuah
jaringan. Bisa dianalogikan dengan tindakan penilangan atau survey terhadap suatu wilayah
berdasarkan lokasi, jaringan, dan katalog sublist pada sebuah website.

## Fitur :
1. Subdomain Scanning
Memetakan dan mendapatkan list subdomain dari domain tertentu sehingga
mempermudah dalam sebuah akses penelusuran website.

2. Server & Network Scanning
Memetakan layanan, lalu lintas transfer data & protocol yang berada pada server &
network.
3. Web Scanning
Memetakan teknologi dan vulnerabilities yang ada pada suatu web dan bisa di-
integrasikan dengan fitur subdomain scanning


## Todo List

**AFI**
- [x] Membuat fungsi pengecekan apakan nmap sudah terinstall
- [x] Membuat fungsi install nmap apabila belum di install
- [x] Membuat fungsi pengecekan apakah argument nya adalah domain atau ip, apabila domain resolve ke ip
- [x] Membuat fungsi pengecekan apakah ip tersebut IP CLOUDFLARE atau bukan, apabila iya jangan di scan : https://s.id/joXlb
- [x] Membuat fungsi pengecekan apakah Server Down/Up sebelum discan
- [x] Membuat fungsi scanning common port dengan nmap, dan return nya hanya berupa port yang open, misal {"IPNYA" : [443, 8080], "domain" : "DOMAINNYA"}
- [x] Menyimpan hasil scanning ke dalam database, databasenya menggunakan sqlite [Not Needed]

**EXCEL**
- [x] Membuat fungsi pengecekan apakah library/module Wappalyzer sudah diinstall
- [x] Membuat fungsi install Wappalyzer apabila belum di install
- [x] Membuat fungsi scanning teknologi website menggunakan library/module Wappalyzer
- [x] Menyimpan hasil scanning ke dalam database, databasenya menggunakan sqlite [Not Needed]

**RHAMA**
- [x] Membuat fungsi passive scanning subdomain
- [x] Membuat module utama LemonSquash.py
- [x] Menyimpan hasil scanning ke dalam database, databasenya menggunakan sqlite [Not Needed]
- [x] Membuat web report dari hasil semua scan *AFI*, dan *EXCEL* [Not Needed]
- [x] Membuat bot telegram untuk report [Not Needed]

## Cara Pengerjaan

1. Pastikan pembuatan module menggunakan fungsi/def untuk setiap tugas
2. Simpan semua module di dalam directory :

- **core/netscan** - untuk module Server & Network Scanning

- **core/webscan** - untuk module Web Scanning

- **core/subdomain** - untuk module subdomain

3. Import module yang dibuat di file utama **LemonSquash.py** untuk dijalankan
4. Setiap *todo* yang sudah selesai, centang dengan tanda X
