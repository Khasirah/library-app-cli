# Apliksasi perpustakaan

## (1) hal login

- (1.1) admin
- (1.2) pengguna
- (1.3) tamu
- (1.4) keluar aplikasi

## (2) hal punya admin

- (2.1) dashboard
  - (2.1.1) jumlah buku
  - (2.1.2) jumlah pengguna
  - (2.1.3) jumlah buku sedang dipinjam
    atau pun sudah dikembalikan
  - (2.1.4) jumlah buku mendekati
    jatuh tempo (3 hari)
  - (2.1.5) jumlah buku melewati batas pengembalian
- (2.2) tambah pengguna
  - (2.2.1) membuat file Pengguna.json (apabila blum ada)
  - (2.2.2) POST ke Pengguna.json
  - (2.2.3) {id, name, passsword, createdAt, updateAt, createdBy, updatedBy}
- (2.3) ubah pengguna
  - (2.3.1) GET menggunakan id user
  - (2.3.2) konfirmasi perubahan ke id user
  - (2.3.3) PUT {name, password, updateBy}
- (2.4) hapus pengguna
  - (2.4.1) DELETE menggunakan id user
  - (2.4.2) konfirmasi penghapusan id user
- (2.5) tambah buku
  - (2.5.1) membuat file Buku.json (apabila belum ada)
  - (2.5.2) POST ke Buku.json
  - (2.5.3) {id, namaBuku, penulis, lokasi, createAt, updateAt, createdBy, updatedBy}
- (2.6) ubah buku
  - (2.6.1) GET menggunakan id buku
  - (2.6.2) konfirmasi perubahan ke id buku
  - (2.6.3) PUT {namaBuku, penulis, lokasi, updateAt, updateBy}
- (2.7) hapus buku
  - (2.7.1) DELETE menggunakan id buku
  - (2.7.2) konfirmasi penghapusan id buku
- (2.8) input peminjaman buku
  - (2.8.1) membuat file Peminjaman.json (apabila blm ada)
  - (2.8.2) POST ke Peminjaman.json
  - (2.8.3) {id, idBuku, idPengguna, tglPengembalian, createdAt, createdBy, updatedBy}
- (2.9) input pengembalian buku
  - (2.9.1) PUT ke id peminjaman
  - (2.9.2) {tglPengembalian, createdBy}
- (2.10) daftar buku dipinjam
- (2.11) keluar (menuju halaman masuk)
