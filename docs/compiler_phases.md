# Fase Pengembangan Compiler MinangScript

Proses pembuatan *mini compiler* ini harus dieksekusi secara berurutan dan disiplin mengikuti tahapan-tahapan berikut.

## Fase 1: Desain Bahasa (Selesai)
- Menentukan substitusi 35 keyword dan 68 built-in functions Python ke dalam bahasa Minang.
- Menyusun Tabel Simbol (Token) dan Tabel Grammar (CFG).
- **Status:** *Telah didokumentasikan di `project_setup.md`.*

## Fase 2: Lexer (Analisis Leksikal) (Selesai)
- **Proses:** Membaca source code (*.minang*) dan memecah karakter demi karakter menjadi daftar Token yang tervalidasi berdasarkan Tabel Simbol.
- **Output:** Aliran Token (*Token stream*).
- **Status:** *Telah diimplementasikan dan tervalidasi. Berjalan dengan aman, stabil, dan lancar (Lolos 100% unit tests untuk pattern matching dan penanganan error).*

## Fase 3: Parser (Analisis Sintaksis) (Selesai)
- **Proses:** Menganalisis aliran Token dari Lexer untuk memastikan sintaksnya benar sesuai aturan CFG yang telah disepakati.
- **Output Utama:** **Parse Tree / Concrete Syntax Tree (CST)** (Pohon sintaks utuh yang berisi seluruh urutan token secara eksplisit tanpa ada reduksi logika). Fase ini murni struktural.
- **Status:** *Telah diimplementasikan dan tervalidasi. Lolos 100% unit tests. Bukti Parse Tree CLI Printer berhasil mencetak struktur node hierarkis bersarang sempurna.*

## Fase 4: AST (Abstract Syntax Tree) (Selesai)
- **Proses:** Menyederhanakan *Parse Tree* dengan membuang token-token dekoratif (seperti tanda kurung kurawal `{ }` atau titik dua) untuk menyisakan hierarki murni dari logika eksekusi.
- **Output:** **Abstract Syntax Tree (AST)** (Pohon logika bersih tanpa *noise* sintaksis).
- **Status:** *Telah diimplementasikan menggunakan Visitor/Transformer (`ASTBuilder`). Lolos unit testing dengan bukti kemampuan visual mencetak `Parse Tree` mentah berdampingan dengan `AST` murni secara simultan untuk validasi komparasi hierarkis.*

## Fase 5: Semantic Analysis (Selesai)
- **Proses:** Melakukan pengecekan makna logis terhadap AST yang telah terwujud (misalnya mendeteksi jika ada pemanggilan variabel yang belum dideklarasikan).
- **Output:** AST yang valid secara konteks dan siap untuk dioptimasi.
- **Status:** *Telah diimplementasikan menggunakan Visitor Pattern (`SemanticAnalyzer`) dengan mekanisme scope tracking melalui `SymbolTable`. Terbukti mendeteksi penggunaan identifier (variabel/fungsi) yang belum dideklarasikan dan menangkap invalid flow (contoh: pemanggilan `baranti` di luar loop).*

## Fase 6: Code Optimization (Selesai)
- **Proses:** Memodifikasi AST untuk meningkatkan efisiensi eksekusi (seperti *constant folding* atau menghapus variabel yang tidak pernah digunakan).
- **Output:** AST teroptimasi.
- **Status:** *Telah diimplementasikan melalui `ASTOptimizer`. Mendukung penghitungan aritmatika dan Boolean statis (Constant Folding) serta pencabutan ranting node AST mati/berisi logika tidak sah (Dead Code Elimination).*

## Fase 7: Code Generation & Packaging (Selesai)
- **Proses:** Menerjemahkan AST teroptimasi ke bahasa target eksekusi (menyesuaikan arsitektur).
- **Output:** Kode mesin yang dapat dieksekusi atau *Installer (Executable file)*.
- **Status:** *Telah diimplementasikan. Code Generator berhasil mengembalikan makna Python ke dalam format string. Telah dipaketkan menggunakan `PyInstaller` untuk melahirkan `minang.exe` sebagai interpreter utuh.*
