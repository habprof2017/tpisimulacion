import random

# random.uniform(a, b) devuelve un numero flotante entre a y b


def generador(lote):
    minLote = min(lote)
    maxLote = max(lote)
    r = round(random.random(), 6)

    valor = round(round(maxLote - minLote, 6) * r + minLote, 6)

    return valor

