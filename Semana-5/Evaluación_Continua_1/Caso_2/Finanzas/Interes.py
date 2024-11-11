def interes_compuesto(p, r, n, t):
    # Fórmula de interés compuesto: A = P * (1 + r / n) ** (n * t)
    monto_total = p * (1 + r / n) ** (n * t)
    return round(monto_total, 2) # Redondear el resultado a 2 decimales para formato de moneda
