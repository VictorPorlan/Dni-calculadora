from src.tabla_letras import tabla_letras

def test_dni():
    assert 'C' == tabla_letras(45699019).calcular_letra()
    assert 'L' == tabla_letras(26450640).calcular_letra()
    assert 'S' == tabla_letras(18032682).calcular_letra()