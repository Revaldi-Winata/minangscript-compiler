# Dokumentasi Fase 2: Lexer

**Status**: Selesai, Stabil, Aman.
**Tanggal Verifikasi**: 2026-06-08

## Hasil Implementasi
Lexer telah sukses dibangun menggunakan Regular Expression (Sequence Matching) tanpa bergantung pada dependensi eksternal, menjamin proses berjalan linear dan cepat.
File yang divalidasi:
- `src/token.py`: Struktur `TokenType` Enum dan struktur `Token`.
- `src/lexer.py`: Komponen Lexer *engine*.
- `tests/test_lexer.py`: *Test suites* unit test untuk pembuktian stabilitas.

## Pembersihan Logika
Sesuai revisi arsitektur, `EXCEPTIONS` dan `CONSTANTS` dihapus secara fisik dan konseptual dari Lexer. Tipe konstanta murni yang relevan seperti `Bana` (True), `Salah` (False), dan `Kosong` (None) kini diperlakukan secara natif sebagai `KEYWORD` agar sesuai dengan struktur Python 3.

## Hasil Validasi
- Seluruh 3 rangkaian uji tuntas dalam 0.002 detik (100% *Pass*).
- Membuktikan ketahanan terhadap pemrosesan block kurung kurawal `{ }`, *built-in function scanning*, pemecahan operator matematika secara presisi, dan deteksi baris/kolom terhadap *illegal characters*.
