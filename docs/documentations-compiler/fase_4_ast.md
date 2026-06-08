# Dokumentasi Fase 4: Abstract Syntax Tree (AST)

**Status**: Selesai, Stabil, Aman.
**Tanggal Verifikasi**: 2026-06-08

## Hasil Implementasi
Pada fase ini, kita mengimplementasikan `ASTBuilder` (sebuah Transformer berbasis pola *Visitor*) yang bertugas menyederhanakan *Parse Tree (CST)* yang sarat akan karakter dekoratif sintaks (kurung, kurawal, dll.) menjadi struktur representasional murni yang siap untuk dianalisis dan dieksekusi. 

File yang telah diimplementasikan:
1. `src/ast_nodes.py`: Menampung puluhan kelas representasi logika murni (`Program`, `IfStmt`, `BinaryOp`, `Assignment`, `Literal`, dsb.). Base class `ASTNode` juga dibekali *CLI Printer* (`print_ast()`).
2. `src/ast_builder.py`: Mesin *Transformer* yang secara cerdas mendeteksi root node (contoh: `if_stmt`), menelusuri struktur anak-anaknya, membuang token non-esensial, lalu me-return representasi `IfStmt` yang bersih.
3. `tests/test_ast.py`: Unit testing yang menggabungkan seluruh pipeline dari Fase 2, 3, hingga 4 (Lexer -> Parser -> AST Builder).

## Verifikasi Ganda (Double Validation)
Sesuai mandat arsitektural dari *user* (tercatat dalam `AGENTS.md`), skrip pengujian **wajib menampilkan komparasi simultan antara produk Fase 3 (mentah) dan Fase 4 (bersih)**. Hal ini dibuktikan dari test case berikut:

### Input Source
```javascript
kok (x > 5) {
    cetak("Gadang")
} lainnyo {
    x = (2 + 3) * 5
}
```

### 1. Pohon Mentah CST (Fase 3)
```text
program
  if_stmt
    'kok' (KEYWORD)
    '(' (LPAREN)
    comparison_expression
      primary
        'x' (IDENTIFIER)
      '>' (OPERATOR)
      primary
        '5' (NUMBER)
    ')' (RPAREN)
    '{' (LBRACE)
    function_call_stmt
      'cetak' (BUILTIN)
      '(' (LPAREN)
      arguments
        primary
          '"Gadang"' (STRING)
      ')' (RPAREN)
    '}' (RBRACE)
    'lainnyo' (KEYWORD)
    '{' (LBRACE)
    assignment_stmt
      'x' (IDENTIFIER)
      '=' (OPERATOR)
      factor_expression... (dst)
```
*Terlihat seluruh kurung, kurawal, dan noise keyword ('kok', 'lainnyo') terbawa.*

### 2. Pohon Logika Murni AST (Fase 4)
```text
Program
  statements:
    IfStmt
      condition:
        BinaryOp
          left:
            Identifier
              name: x
          operator: >
          right:
            Literal
              value: 5.0
      then_branch:
        FunctionCall
          name:
            Identifier
              name: cetak
          args:
            Literal
              value: Gadang
      else_branch:
        Assignment
          target:
            Identifier
              name: x
          value:
            BinaryOp
              left:
                BinaryOp
                  left:
                    Literal
                      value: 2.0
                  operator: +
                  right:
                    Literal
                      value: 3.0
              operator: *
              right:
                Literal
                  value: 5.0
```
*Node telah sangat bersih. Hanya tersisa percabangan logika esensial (Program -> If -> Condition / Then / Else).*

## Kesimpulan
Kompilator secara utuh mampu membedakan sintaks murni dan sintaks tereksekusi. Kode `if_stmt` berhasil tereduksi dari 30+ token di *Parse Tree* menjadi hanya struktur pohon biner esensial di *AST*. Tahap berikutnya adalah **Fase 5 (Semantic Analysis)** atau bisa saja langsung dieksekusi dengan membangun interpreter logika di atas node AST.
