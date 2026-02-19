def formatar_telefone(numero):
    # Exemplo: "11999998888" → "(11) 99999-8888"
    if len(numero) == 11:
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    return numero

def validar_email(email):
    return "@" in email and "." in email

