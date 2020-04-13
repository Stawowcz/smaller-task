from parsowanie import ParsowaniePliku
import pytest

@pytest.fixture()
def param():
        test_obiekt = ParsowaniePliku("plik_bez_niepotrzebnych_danych.txt", "plik_obliczeniowy.txt", 360)
        return test_obiekt
        
def test_srednia_temp_test(param):
        param.stworzenie_pliku_bez_niepotrzebnych_danych()
        param.stworzenie_pliku_obliczeniowego1()
        result= param.srednia()      
        assert result == 5.95
        
def test_najwyższa_temp_test(param):
        result = param.dzień_w_którym_zaobserwowano_najwyzsza2()
        assert result == 14.75
        
