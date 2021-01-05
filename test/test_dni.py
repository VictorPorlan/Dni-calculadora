from src.dni import dni

def test_verificar_longitud_corto():
    assert 'Error: dni demasiado largo o corto' == dni('4569901C').verificar_longitud()
    assert 'Error: dni demasiado largo o corto' == dni('').verificar_longitud()
    assert 'Error: dni demasiado largo o corto' == dni('4569901C').verificar_longitud()

def test_verificar_longitud_largo():
    assert 'Error: dni demasiado largo o corto' == dni('456990199C').verificar_longitud()
    assert 'Error: dni demasiado largo o corto' == dni('45699019921454125').verificar_longitud()

def test_verificar_letra_y_dni():
    assert '45699019C' == dni('45699019C').verificar_letra_y_dni()
    assert 'C45699019' == dni('C45699019').verificar_letra_y_dni()
    assert False == dni('45699019N').verificar_letra_y_dni()

def test_creador_dni():
    assert 'Error: dni demasiado largo o corto' == dni('456C').creador_dni()
    assert 'Error: dni demasiado largo o corto' == dni('456').creador_dni()
    assert 'Error: dni demasiado largo o corto' == dni('4561241245125').creador_dni()
    assert 'Error: la letra no es correcta' == dni('45699019N').creador_dni()
    assert '45699019C' == dni('45699019C').creador_dni()
