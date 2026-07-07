def es_ip_valida(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or (len(parte) > 1 and parte.startswith('0')):
            return False
        if int(parte) > 255 or int(parte) < 0:
            return False
    return True
    