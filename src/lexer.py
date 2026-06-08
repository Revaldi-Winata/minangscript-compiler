import re
from typing import List
from src.token import Token, TokenType

# Himpunan keyword dan fungsi bawaan yang dipetakan dari project_setup.md
KEYWORDS = {
    'Bana', 'Salah', 'Kosong', # Boolean / Nilai Khusus yang masuk ke keyword
    'jo', 'atau', 'indak', 'kok', 'kok_lain', 'lainnyo', 'untuak', 'salamo', 
    'di', 'baranti', 'taruih', 'lewat', 'buek', 'baliakan', 'hasilkan', 
    'fungsi_ketek', 'kalas', 'awak', 'induak', 'cubo', 'kacuali', 'akhirnyo', 
    'angkek', 'pastikan', 'ambiak', 'dari', 'sagai', 'jo_ko', 'basamo', 
    'tunggu', 'cocok', 'kasus', 'sadoalah', 'indak_lokal', 'hapuih', 'ialah'
}

BUILTINS = {
    'cetak', 'tanyo', 'angko', 'desimal', 'teks', 'logika', 'kompleks',
    'daftar', 'kumpulan', 'himpunan', 'kamus', 'himpunan_baku', 'mutlak',
    'bulekkan', 'pangkek', 'bagisisa', 'jumlah', 'tatinggi', 'tarandah',
    'panjang', 'jarak', 'daftarkan', 'gabuang', 'ulang', 'lanjuik',
    'baliakkan', 'uruikkan', 'sadonyo', 'salah_satu', 'jinih', 'ujikate',
    'ujisub', 'tando', 'bisa_dipanggia', 'huruf', 'urutan', 'aski', 'biner',
    'oktal', 'heksa', 'ambiak_sifaik', 'atur_sifaik', 'ado_sifaik',
    'hapuih_sifaik', 'globalnyo', 'lokalnyo', 'variabelnyo', 'arah',
    'evaluasi', 'jalankan', 'kompilasi', 'bukak', 'bait', 'susunan_bait',
    'caliak_memori', 'petakan', 'sariang', 'properti', 'metode_statis',
    'metode_kalas', '__ambiak__', 'titiak_ranti', 'bantuak',
    'wakia', 'acak', 'tolong', 'potong', 'objek'
}

class LexerError(Exception):
    def __init__(self, message: str, line: int, column: int):
        super().__init__(f"LexerError at line {line}, col {column}: {message}")

class Lexer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.pos = 0
        self.line = 1
        self.column = 1
        
        # Spesifikasi Regex (berurutan, rule terpanjang didahulukan)
        self.rules = [
            ('SKIP', r'[ \t]+'),
            ('COMMENT', r'#.*'),
            ('NEWLINE', r'\n'),
            ('STRING', r'"[^"]*"|\'[^\']*\''),
            ('NUMBER', r'\d+\.\d+|\d+'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OPERATOR', r'==|!=|<=|>=|<|>|\+|-|\*|/|='),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('COMMA', r','),
            ('MISMATCH', r'.')
        ]
        
        self.regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.rules)
        self.scanner = re.compile(self.regex)

    def tokenize(self) -> List[Token]:
        tokens = []
        for match in self.scanner.finditer(self.source_code):
            kind = match.lastgroup
            value = match.group()
            
            if kind == 'SKIP' or kind == 'COMMENT':
                self.column += len(value)
                continue
            elif kind == 'NEWLINE':
                self.line += 1
                self.column = 1
                continue
            elif kind == 'MISMATCH':
                raise LexerError(f"Karakter Ilegal '{value}'", self.line, self.column)
            
            token_type = self._determine_token_type(kind, value)
            tokens.append(Token(token_type, value, self.line, self.column))
            self.column += len(value)
            
        tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return tokens
        
    def _determine_token_type(self, kind: str, value: str) -> TokenType:
        if kind == 'ID':
            if value in KEYWORDS:
                return TokenType.KEYWORD
            elif value in BUILTINS:
                return TokenType.BUILTIN
            else:
                return TokenType.IDENTIFIER
                
        mapping = {
            'STRING': TokenType.STRING,
            'NUMBER': TokenType.NUMBER,
            'OPERATOR': TokenType.OPERATOR,
            'LBRACE': TokenType.LBRACE,
            'RBRACE': TokenType.RBRACE,
            'LPAREN': TokenType.LPAREN,
            'RPAREN': TokenType.RPAREN,
            'COMMA': TokenType.COMMA
        }
        return mapping[kind]
