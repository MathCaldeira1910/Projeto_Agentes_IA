def calculator(expression: str):
    try:
        return str(eval(expression))
    except Exception:
        return "Erro no cálculo"
