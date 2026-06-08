# Desain Bahasa MinangScript

## 1. Pendekatan Sintaksis (Syntax Approach)
* **Blok Kode:** Menggunakan kurung kurawal `{ }` untuk kemudahan di sisi Parser.
* **Deklarasi Variabel:** Dinamis/Implisit (seperti Python), tanpa keyword khusus. Contoh: `x = 5`.
* **Operator:** Standar bawaan (`+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=`).

---

## 2. Pemetaan Seluruh Keyword Python (Per Kategori)

### Boolean / Nilai Khusus
* `True` -> `Bana`
* `False` -> `Salah`
* `None` -> `Kosong`

### Logika
* `and` -> `jo`
* `or` -> `atau`
* `not` -> `indak`

### Percabangan
* `if` -> `kok`
* `elif` -> `kok_lain`
* `else` -> `lainnyo`

### Perulangan
* `for` -> `untuak`
* `while` -> `salamo`
* `in` -> `di`
* `break` -> `baranti`
* `continue` -> `taruih`
* `pass` -> `lewat`

### Fungsi
* `def` -> `buek`
* `return` -> `baliakan`
* `yield` -> `hasilkan`
* `lambda` -> `fungsi_ketek`

### Class / OOP
* `class` -> `kalas`
* `self` -> `awak`
* `super` -> `induak`

### Exception Handling
* `try` -> `cubo`
* `except` -> `kacuali`
* `finally` -> `akhirnyo`
* `raise` -> `angkek`
* `assert` -> `pastikan`

### Import
* `import` -> `ambiak`
* `from` -> `dari`
* `as` -> `sagai`

### Context Manager
* `with` -> `jo_ko`

### Async Programming
* `async` -> `basamo`
* `await` -> `tunggu`

### Pattern Matching (Python 3.10+)
* `match` -> `cocok`
* `case` -> `kasus`

### Scope / Namespace
* `global` -> `sadoalah`
* `nonlocal` -> `indak_lokal`

### Deletion
* `del` -> `hapuih`

### Reserved (Soft / Historical)
* `is` -> `ialah`

---

## 3. Pemetaan Seluruh Fungsi Bawaan (Built-in Functions) Python

### Input / Output
* `print` -> `cetak`
* `input` -> `tanyo`

### Type Conversion
* `int` -> `angko`
* `float` -> `desimal`
* `str` -> `teks`
* `bool` -> `logika`
* `complex` -> `kompleks`

### Collection Constructors
* `list` -> `daftar`
* `tuple` -> `kumpulan`
* `set` -> `himpunan`
* `dict` -> `kamus`
* `frozenset` -> `himpunan_baku`

### Numeric
* `abs` -> `mutlak`
* `round` -> `bulekkan`
* `pow` -> `pangkek`
* `divmod` -> `bagisisa`
* `sum` -> `jumlah`
* `max` -> `tatinggi`
* `min` -> `tarandah`

### Iteration
* `len` -> `panjang`
* `range` -> `jarak`
* `enumerate` -> `daftarkan`
* `zip` -> `gabuang`
* `iter` -> `ulang`
* `next` -> `lanjuik`
* `reversed` -> `baliakkan`
* `sorted` -> `uruikkan`

### Logic
* `all` -> `sadonyo`
* `any` -> `salah_satu`

### Type / Reflection
* `type` -> `jinih`
* `isinstance` -> `ujikate`
* `issubclass` -> `ujisub`
* `id` -> `tando`
* `callable` -> `bisa_dipanggia`

### Character / Encoding
* `chr` -> `huruf`
* `ord` -> `urutan`
* `ascii` -> `aski`
* `bin` -> `biner`
* `oct` -> `oktal`
* `hex` -> `heksa`

### Object Utilities
* `getattr` -> `ambiak_sifaik`
* `setattr` -> `atur_sifaik`
* `hasattr` -> `ado_sifaik`
* `delattr` -> `hapuih_sifaik`

### Namespace Utilities
* `globals` -> `globalnyo`
* `locals` -> `lokalnyo`
* `vars` -> `variabelnyo`
* `dir` -> `arah`

### Execution
* `eval` -> `evaluasi`
* `exec` -> `jalankan`
* `compile` -> `kompilasi`

### File
* `open` -> `bukak`

### Memory / Buffer
* `bytes` -> `bait`
* `bytearray` -> `susunan_bait`
* `memoryview` -> `caliak_memori`

### Functional
* `map` -> `petakan`
* `filter` -> `sariang`

### Class Utilities
* `property` -> `properti`
* `staticmethod` -> `metode_statis`
* `classmethod` -> `metode_kalas`
* `super` -> `induak`

### Import System
* `__import__` -> `__ambiak__`

### Debugging
* `breakpoint` -> `titiak_ranti`

### Misc
* `format` -> `bantuak`
* `repr` -> `wakia`
* `hash` -> `acak`
* `help` -> `tolong`
* `slice` -> `potong`
* `object` -> `objek`

---

# Tabel Bahasa

## Tabel Simbol (Token)
Tabel ini merepresentasikan output dasar dari proses **LEXER** untuk mendeteksi semua entitas di atas.

| Nama Token | Pola Regex | Deskripsi |
|---|---|---|
| `KEYWORD` | Sesuai list kategori di atas (`kok`, dll) | Kata kunci bahasa |
| `BUILTIN` | Sesuai list kategori fungsi (`cetak`, dll) | Fungsi bawaan |
| `IDENTIFIER` | `[a-zA-Z_][a-zA-Z0-9_]*` | Nama variabel atau nama fungsi buatan |
| `NUMBER` | `\d+(\.\d+)?` | Nilai angka bulat (int) maupun desimal (float) |
| `STRING` | `"[^"]*"` atau `'[^']*'` | Teks yang diapit kutip tunggal/ganda |
| `OPERATOR` | `+`, `-`, `*`, `/`, `=`, `==`, `<`, `>`, `<=`, `>=` | Operator logika dan aritmatika |
| `LBRACE` | `{` | Kurung kurawal buka (awal blok) |
| `RBRACE` | `}` | Kurung kurawal tutup (akhir blok) |
| `LPAREN` | `(` | Kurung biasa buka |
| `RPAREN` | `)` | Kurung biasa tutup |
| `COMMA` | `,` | Pemisah argumen fungsi |

## Tabel Grammar (CFG) Minimal
Meskipun lexer mengenali seluruh tipe di atas, CFG berikut digunakan sebagai *baseline* bagi Parser untuk eksekusi yang valid. 
*(Catatan Arsitektur: CFG ini akan dicetak utuh sebagai Concrete Syntax Tree pada Fase 3, dan baru akan disederhanakan menjadi AST pada Fase 4).*

```text
program -> statement*

statement -> assignment_stmt
           | if_stmt
           | while_stmt
           | for_stmt
           | function_def_stmt
           | function_call_stmt
           | return_stmt
           | class_def_stmt
           | try_stmt
           | import_stmt
           | from_import_stmt
           | with_stmt
           | async_stmt
           | match_stmt
           | unary_ctrl_stmt
           | simple_ctrl_stmt
           | expression_stmt
           
assignment_stmt -> IDENTIFIER "=" expression

if_stmt -> "kok" "(" expression ")" "{" statement* "}"
           ("kok_lain" "(" expression ")" "{" statement* "}")*
           ("lainnyo" "{" statement* "}")?

while_stmt -> "salamo" "(" expression ")" "{" statement* "}"
for_stmt -> "untuak" "(" IDENTIFIER "di" expression ")" "{" statement* "}"

function_def_stmt -> "buek" IDENTIFIER "(" parameters? ")" "{" statement* "}"
parameters -> (IDENTIFIER | "awak") ("," (IDENTIFIER | "awak"))*

class_def_stmt -> "kalas" IDENTIFIER ("(" IDENTIFIER ")")? "{" statement* "}"

try_stmt -> "cubo" "{" statement* "}" 
            ("kacuali" (IDENTIFIER ("sagai" IDENTIFIER)?)? "{" statement* "}")* 
            ("akhirnyo" "{" statement* "}")?

import_stmt -> "ambiak" IDENTIFIER ("sagai" IDENTIFIER)?
from_import_stmt -> "dari" IDENTIFIER "ambiak" IDENTIFIER
with_stmt -> "jo_ko" expression ("sagai" IDENTIFIER)? "{" statement* "}"
async_stmt -> "basamo" (function_def_stmt | for_stmt | with_stmt)
match_stmt -> "cocok" expression "{" ("kasus" expression "{" statement* "}")* "}"

simple_ctrl_stmt -> ("baranti" | "taruih" | "lewat")
unary_ctrl_stmt -> ("angkek" | "pastikan" | "hapuih" | "sadoalah" | "indak_lokal" | "hasilkan") expression

return_stmt -> "baliakan" expression?

function_call_stmt -> (BUILTIN | IDENTIFIER) "(" arguments? ")"
arguments -> expression ("," expression)*

expression -> IDENTIFIER | NUMBER | STRING | KEYWORD (Bana | Salah | Kosong | awak | induak)
            | "indak" expression
            | ("+" | "-") expression
            | "tunggu" expression
            | "fungsi_ketek" parameters "{" expression "}"
            | expression OPERATOR expression
```
