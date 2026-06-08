# MinangScript Mini Compiler

Status: Tahap Pengembangan (Under Development)

MinangScript Mini Compiler adalah proyek kompilator berukuran kecil yang mengadaptasi sebagian kosakata bahasa pemrograman ke dalam bahasa daerah Minangkabau. Proyek ini dibangun sebagai eksperimen dan implementasi praktikum untuk ranah ilmu Teknik Kompilasi. 

Perlu dicatat bahwa kompilator ini tidak menerjemahkan atau mengubah seluruh fitur bahasa Python secara penuh. Kompilator ini **murni sebuah bahasa *mini*** yang hanya menargetkan dan mendukung **subset kata kunci** serta operasi dasar tertentu untuk memvalidasi alur teori kompilasi dari awal hingga menjadi berkas eksekusi.

## Fitur Utama

- Sintaks Lokal Dasar: Mendukung kata kunci pemrograman esensial yang diubah ke bahasa Minang (seperti `buek` untuk mendefinisikan fungsi, `kok` untuk kondisi logika, `salamo` untuk perulangan). Rujukan lengkap terdapat pada berkas REFERENSI_BAHASA.md.
- Standalone Binary: Dilengkapi dengan pengaturan pemaketan agar skrip penyusun kompilator dapat dibungkus menjadi satu berkas `minang.exe` yang langsung berjalan di OS Windows.
- Pipeline Kompilasi Murni: Alur kerja menerapkan prinsip pembacaan leksikal, parsing AST, dan optimasi dasar seperti *Constant Folding* dan *Dead Code Elimination* sebelum eksekusi terjadi.

## Panduan Penggunaan `minang.exe`

Bagi pengguna yang sudah memiliki berkas `minang.exe` (atau mengunduhnya dari rilis), program ini dapat dijalankan langsung melalui Command Prompt atau PowerShell di Windows **tanpa memerlukan instalasi Python**.

### Persiapan Direktori & Environment Variables PATH
Agar eksekusi skrip berhasil, pastikan berkas kode berekstensi `.minang` yang ingin dieksekusi berada di **satu folder yang sama** dengan `minang.exe`. 

Namun, agar kompilator dapat dipanggil dari direktori mana saja tanpa harus selalu menyalin `minang.exe`, direktori penyimpanannya perlu didaftarkan ke dalam *Environment Variables PATH* Windows:
1. Buka *Start Menu* Windows, ketik **Edit the system environment variables**, lalu tekan *Enter*.
2. Klik tombol **Environment Variables...** di sudut kanan bawah.
3. Pada area *System variables* (atau *User variables*), pilih variabel bernama **Path**, lalu klik **Edit...**
4. Klik **New**, lalu tempel (*paste*) jalur (*Path*) lengkap menuju folder tempat `minang.exe` berada (contoh: `C:\Path\Menuju\Mini-Compiler\dist`).
5. Klik **OK** pada semua jendela. Setelah proses ini selesai, perintah `minang.exe` sudah bisa dieksekusi dari direktori mana pun di dalam terminal.

### Menjalankan Skrip
Perintah `jalan` digunakan untuk **mengeksekusi berkas kode** berekstensi `.minang` secara langsung.
```bash
minang.exe jalan (nama_file).minang
```

### Membangun Aplikasi Baru (Fitur Rilis)
Perintah `rilis` digunakan jika pembuat kode ingin **mempaketkan skrip** `.minang` miliknya menjadi sebuah **aplikasi `.exe` tersendiri**. Ini berguna agar hasil program buatan (misal aplikasi kalkulator Minang) bisa dibagikan dan dijalankan oleh orang lain, tanpa mengharuskan orang tersebut memiliki `minang.exe` di komputernya.
```bash
minang.exe rilis (nama_file).minang
```
## Setup Builder (Membangun Ulang Kompilator)

Jika ada pembaruan pada inti kompilator, berkas `minang.exe` dapat dibangun ulang melalui skrip utama `minang.py` menggunakan `PyInstaller`. Pembuatan ini disarankan dilakukan di dalam **lingkungan virtual Python (Virtual Environment) yang bersih**.

1. Lakukan instalasi pustaka pembuat berkas eksekusi:
   ```bash
   pip install pyinstaller
   ```

2. Bangun program melalui perintah berikut:
   ```bash
   pyinstaller --onefile --name minang minang.py
   ```

Hasil kompilasi mesin kompilator tersebut akan berada di dalam direktori `dist/`.

## Pengujian (Testing)

Proyek ini mendefinisikan beberapa lapisan pengujian (*testing*) untuk membuktikan bahwa `minang.exe` beroperasi secara stabil sesuai konsep awal perancangan kompilator.

### 1. Black Box & Functional Testing
Pengujian ini memvalidasi keluaran akhir tanpa mencampuri mesin kompilator di baliknya. Pengujian dilakukan secara otomatis menggunakan pustaka `pytest` yang berinteraksi langsung dengan berkas `minang.exe` via sub-proses OS.

```python
import subprocess
import pytest

# Menggunakan pola Parameterized untuk menguji berbagai kosakata dasar Minang
@pytest.mark.parametrize("kode_minang, output_harapan", [
    ("cetak(5 + 5)", "10\n"),
    ("x = 10\ncetak(x)", "10\n"),
])
def test_fungsional_minang(tmp_path, kode_minang, output_harapan):
    jalur_skrip = tmp_path / "test.minang"
    jalur_skrip.write_text(kode_minang)

    hasil = subprocess.run(["dist/minang.exe", "jalan", str(jalur_skrip)], capture_output=True, text=True)
    assert hasil.stdout == output_harapan
```
**Ekspektasi Penjelasan:** Jika script di atas dijalankan via `pytest test_minang.py`, terminal akan mencetak status `PASSED`. Ini membuktikan bahwa mekanisme kompilasi untuk alokasi memori (penugasan variabel) dan *output console* (cetak) sukses bekerja dengan akurat.

### 2. Stress Testing (Beban Kompilasi)
Pengujian ekstrem diberikan untuk melihat apakah *Parser* dan *AST Builder* mampu menangani beban sintaks yang dalam (seperti rekursi berlapis atau perhitungan tak terbatas) tanpa mengalami kebocoran memori atau *Stack Overflow*.

Sebagai contoh, dilakukan injeksi operasi aritmatika brutal sebanyak puluhan ribu token dalam satu baris:
```text
cetak(1 + 2 * 3 - 4 / 5 + 6 * 7 ... [berulang hingga 10.000 token])
```
**Ekspektasi Penjelasan:** Karena kompilator ini memiliki modul Optimasi Fase 6 (*Constant Folding*), program pembaca tidak akan mogok (*crash*), melainkan mesin akan mendeteksi kerumitan tersebut dan menyederhanakan perhitungan raksasanya menjadi sebuah angka final seketika di belakang layar, lalu langsung mencetaknya dalam hitungan milidetik.

### 3. Negative Testing (Penanganan Cacat Kode)
Pengujian ini dilakukan dengan sengaja mengumpankan kode yang cacat secara tata bahasa (misalnya blok kurung kurawal `{` yang tidak pernah ditutup, atau menggunakan variabel yang belum dibuat).
**Ekspektasi Penjelasan:** Kompilator tidak boleh mati membeku secara mendadak, melainkan harus melempar pesan *SyntaxError* atau *SemanticError* yang *graceful*, memberitahu letak baris kerusakan secara presisi.

## Struktur Repositori

Repositori ini memuat seluruh kode sumber kompilator mulai dari mesin inti hingga berkas eksekusi:

```text
minangscript-compiler/
│
├── src/                      # Modul Inti Kompilator (Leksikal hingga Code Gen)
├── minang.py                 # File Utama (Builder / CLI Setup)
├── trace_compiler.py         # Skrip Diagnostik (mencetak log visual Token & AST di terminal untuk debugging)
├── REFERENSI_BAHASA.md       # Daftar Kosakata MinangScript
├── README.md                 # Dokumentasi Proyek
├── LICENSE                   # Lisensi MIT
└── dist/
    └── minang.exe            # Aplikasi Kompilator Mandiri
```

## Rencana Pengembangan (Roadmap)

Kompilator mini ini sedang dipersiapkan untuk peningkatan pada beberapa aspek:
- Penyempurnaan pelacakan error berbasis nomor baris (line number).
- Restrukturisasi presedensi operator aritmatika.
- Penambahan stabilitas pemetaan kata kunci kontrol bahasa.

