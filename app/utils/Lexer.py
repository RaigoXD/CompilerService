import sly


class LexerMiniC(sly.Lexer):
    tokens = {
        # PALABRAS RESERVADAS
        STATIC,
        EXTERN,
        INT,
        FLOAT,
        CHAR,
        CONST,
        RETURN,
        BREAK,
        CONTINUE,
        IF,
        ELSE,
        WHILE,
        TRUE,
        FALSE,
        FOR,
        # LITERALES
        INUMBER,
        FNUMBER,
        CHARACTER,
        STRING,
        # OPERADORES
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        LT,
        LE,
        GT,
        GE,
        EQ,
        NE,
        LAND,
        LOR,
        LNOT,
        MEMREF,
        MODULO,
        # MISELANEOS
        ASSIGN,
        SEMI,
        LPAREN,
        RPAREN,
        LBRACE,
        RBRACE,
        COMMA,
        ELLIPSE,
        LBRACKET,
        RBRACKET,
        ADDEQ,
        SUBEQ,
        DIVEQ,
        MULEQ,
        TIMESE,
        # identificadores
        ID,
    }

    # IGNORES
    # IGNORE ALL WHITE-SPACES
    ignore = " \t\r"

    # ignore commets
    @_(r"//.*\n")  # // <- comments
    def ignore_cppcomment(self, t):
        print("cpp comment find")
        self.lineno += t.value.count("\n")

    @_(r"/\*(|.|\n)*\*/")  # /**/ <- comments
    def ignore_commet(self, t):
        print("long comment find: %s", t.value.count("\n"))
        self.lineno += t.value.count("\n")

    # ignore newline
    @_(r"\n+")
    def ignore_newline(self, t):
        print(f"{self.lineno} : newline find")
        self.lineno += t.value.count("\n")  # cuenta los saltos de linea y los ignora

    # Getting all string
    STRING = r"\".*\""
    # CHAR = r"\'.\'"

    # literales
    literals = "+-*/%!=;,(){}[]"
    # rules

    LE = r"<="
    LT = r"<"

    GE = r">="
    GT = r">"

    NE = r"!="
    LNOT = r"!"

    LAND = r"&&"
    MEMREF = r"&"

    LOR = r"\|\|"

    ADDEQ = r"\+="
    PLUS = r"\+"

    SUBEQ = r"-="
    MINUS = r"-"

    TIMESE = r"\*="
    TIMES = r"\*"

    DIVEQ = r"/="
    DIVIDE = r"/"

    MULEQ = r"%="
    MODULO = r"%"

    # espacial case for equality
    EQ = r"=="
    ASSIGN = r"="

    LPAREN = r"\("
    RPAREN = r"\)"

    LBRACE = r"\{"
    RBRACE = r"\}"

    LBRACKET = r"\["
    RBRACKET = r"\]"

    SEMI = r";"
    COMMA = r","

    ELLIPSE = r"\.\.\."

    # INT, FLOAT
    FNUMBER = r"[0-9]+\.[0-9]+"
    INUMBER = r"[0-9]+"

    # IDENTIFICADOR
    ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
    CHARACTER = r"\'.\'"

    # Casos espaciales palabra Reservadas
    ID["static"] = STATIC  # aqui van todas las palabras reservadas del lenguaje
    ID["extern"] = EXTERN
    ID["int"] = INT
    ID["float"] = FLOAT
    ID["char"] = CHAR
    ID["const"] = CONST
    ID["return"] = RETURN
    ID["break"] = BREAK
    ID["continue"] = CONTINUE
    ID["if"] = IF
    ID["else"] = ELSE
    ID["while"] = WHILE
    ID["true"] = TRUE
    ID["FALSE"] = FALSE
    ID["for"] = FOR

    def error(self, t):
        self.index += 1
        print(f"Line {self.lineno}: Caracter '{t.value[0]}' es ilegal")
