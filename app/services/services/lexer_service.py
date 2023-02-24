from fastapi import HTTPException

from app.utils.Lexer import LexerMiniC  # Falta Dependency injection


def check_sintaxis(code: str):
    """Check the sintaxis from code

    Args:
        code (str): the code to analyze

    Raises:
        HTTPException: if there is an error tokenizing

    Returns:
        list: list of tokens
    """
    lexer = LexerMiniC()
    try:
        tokens = lexer.tokenize(code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

    # for tok in tokens:
    #     print('type=%r, value=%r line=%r' % (tok.type, tok.value, tok.lineno))

    data_response = [
        {"num_token": num + 1, "type": tok.type, "value": tok.value, "line": tok.lineno}
        for num, tok in enumerate(tokens)
    ]
    return data_response
