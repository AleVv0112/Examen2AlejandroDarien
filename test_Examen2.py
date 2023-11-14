from Examen2 import MiClase

#Se tuvo que crear el archivo test_Examen2.py para poder realizar las pruebas unitarias porque si no daba error y n oencontraba pruebas en el archivo Examen2.py

def test_ObtieneValencia_con_impares():
    obj = MiClase(None, None, None, None, None)
    assert obj.ObtieneValencia(13579) == 5 

def test_ObtieneValencia_sin_impares():
    obj = MiClase(None, None, None, None, None)
    assert obj.ObtieneValencia(2468) == 0  

def test_DivisibleTempo_numero_primo():
    obj = MiClase(None, None, None, None, None)
    assert obj.DivisibleTempo(7) == [1, 7]  

def test_DivisibleTempo_numero_no_primo():
    obj = MiClase(None, None, None, None, None)
    assert obj.DivisibleTempo(10) == [1, 2, 5, 10]