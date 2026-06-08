# Dokumentasi Fase 3: Parser (Analisis Sintaksis)

**Status**: Selesai, Stabil, Aman.
**Tanggal Verifikasi**: 2026-06-08

## Hasil Implementasi
Parser telah berhasil dibangun untuk menerima token dari Lexer dan merakitnya menjadi **Parse Tree (Concrete Syntax Tree)** murni menggunakan algoritma *Recursive Descent Parsing*. Sesuai arsitektur yang disepakati, Parser tidak melakukan reduksi AST pada tahapan ini, melainkan menyimpan setiap elemen sintaksis mentah.

File yang dibuat:
- `src/cst_nodes.py`: Mendefinisikan class `ParseNode` untuk pembentukan *tree* hirarkis bersarang dan berisi *printer* visual.
- `src/parser.py`: Engine *Recursive Descent* Parser lengkap yang menangani Presedensi Operator Matematika (Kali/Bagi > Tambah/Kurang), Blok Kode, Percabangan (kok, kok_lain, lainnyo), Perulangan, Deklarasi Fungsi, dan Pemanggilan Fungsi.
- `tests/test_parser.py`: Suite pengujian (unit testing).

## Bukti Validasi (Visualisasi Terminal CLI)
Seluruh 4 *test case* berhasil *pass* dalam **0.002s** tanpa *error* dan mampu mencetak pohon secara rekursif sempurna:

### Contoh Parse Tree Assignment (`x = 5`)
```text
program
  assignment_stmt
    'x' (IDENTIFIER)
    '=' (OPERATOR)
    primary
      '5' (NUMBER)
```

### Contoh Parse Tree Kompleks (`x = (2 + 3) * 5`)
```text
program
  assignment_stmt
    'x' (IDENTIFIER)
    '=' (OPERATOR)
    factor_expression
      grouping
        '(' (LPAREN)
        term_expression
          primary
            '2' (NUMBER)
          '+' (OPERATOR)
          primary
            '3' (NUMBER)
        ')' (RPAREN)
      '*' (OPERATOR)
      primary
        '5' (NUMBER)
```

## Tindak Lanjut
Fase 3 secara sah telah selesai. Seluruh validasi syntax dan integritas hierarkis berjalan lancar. Proses berikutnya akan berfokus eksklusif pada **Fase 4: AST (Abstract Syntax Tree)**, di mana *Parse Tree* ini akan dipangkas dari entitas dekoratifnya (seperti `'('`, `'{'`) menjadi struktur operasi fundamental.
