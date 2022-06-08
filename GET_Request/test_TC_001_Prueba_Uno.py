import pytest
# Test case code must be written inside a method
# method name must be started with test
# si los ejecuto con -v nos muestra el resultado de cada uno ex: pytest -v GET_Request/test_TC_001_Prueba_Uno.py
# ejecutar como ->  pytest -v GET_Request -mismo efecto que el file pero lo hace con todos los que estan dentro del folder
# -s print statement output en este caso "this is...."

#using decorator
@pytest.mark.skip('skipping as this functionality is not marking, developer will fix it new build')
def test_tc_001_get_users():
    #put test case code over there
    #method with test name
    print('This is out test case code')
    print('This is end of my test case')

def test_tc_003_deposit_account():
    print('prueba ejecucion test case')
    print('another test')
