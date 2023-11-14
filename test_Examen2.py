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
    
def test_Encuentra_elemento_presente():
    obj = MiClase(None, None, None, None, None)
    assert obj.Encuentra([1, 2, 3, 4, 5], 3) == True 

def test_Encuentra_elemento_ausente():
    obj = MiClase(None, None, None, None, None)
    assert obj.Encuentra([1, 2, 3, 4, 5], 6) == False



def test_ObtieneMasBailable_lista_vacia():
    obj = MiClase(None, None, None, None, None)
    assert obj.ObtieneMasBailable([]) is None  

def test_ObtieneMasBailable_lista_no_vacia():
    obj = MiClase(None, None, None, None, None)
    assert obj.ObtieneMasBailable([1, 2, 3, 4, 5]) == 5 

def test_VerificaListaCanciones_con_None():
    obj = MiClase(None, None, None, None, None)
    assert obj.VerificaListaCanciones(["Canción 1", None, "Canción 3"]) == False 

def test_VerificaListaCanciones_sin_None():
    obj = MiClase(None, None, None, None, None)
    assert obj.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]) == True