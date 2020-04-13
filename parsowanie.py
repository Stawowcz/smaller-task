class ParsowaniePliku():

    def __init__(self,plik_bez_niepotrzebnych_danych, plik_obliczeniowy, ilosc_dni)
        print("Podaj nazwe pliku, w którym nie bedzie niepotrzebnych danych")
        #self.plik_bez_niepotrzebnych_danych = input()
        self.plik_bez_niepotrzebnych_danych = plik_bez_niepotrzebnych_danych
        print("Podaj nazwe pliku obliczeniowego ")
        self.plik_obliczeniowy = plik_obliczeniowy
        print("Podaj ilosc dni ")
        #self.ilosc_dni = input()
        self.ilosc_dni = ilosc_dni
        self.plik_poczatkowy = r"C:\\Users\\Kuba\\Desktop\\zadanie_dolby\\wroclaw_weather.txt"
        self.sciezka = r"C:\\Users\Kuba\\Desktop\\zadanie_dolby\\"
        self.rok = r"2016"

    def stworzenie_pliku_bez_niepotrzebnych_danych(self):
        with open(self.plik_poczatkowy, "r") as f:        
            contents = f.readlines()
            for line in (contents):
                if line[0:4]==self.rok:
                    with open(self.sciezka + self.plik_bez_niepotrzebnych_danych, "a") as f:
                        f.write(line)
        return self.plik_bez_niepotrzebnych_danych
        print (self.plik_bez_niepotrzebnych_danych)
        
                        
    def stworzenie_pliku_obliczeniowego1(self):
        with open(self.sciezka + self.plik_bez_niepotrzebnych_danych, "r") as f:        
            contents = f.readlines()
            for n, line in enumerate(contents):
                if line[0:4]==self.rok and n<int(self.ilosc_dni):
                    with open(self.sciezka + self.plik_obliczeniowy, "a") as f:
                        f.write(line)
        return self.plik_obliczeniowy 

    def odczyt_pliku_obliczeniowego(self):
        with open(self.sciezka + self.plik_obliczeniowy, "r") as f:
                return f.readlines()          

    def srednia(self):
        suma = 0
        for digit in self.lista_temperatur():
            suma = suma + digit
        print ("Srednia temperatura całosciowo to " +str(((suma)/len(self.lista_temperatur()))))
        return round((suma)/len(self.lista_temperatur()),2)

    def lista_temperatur(self):
        lista = []
        with open(self.plik_obliczeniowy, 'r') as f2:
            contents = f2.readlines()
            for line in contents:
                lista.append(float((line.split(";")[5])))
        return lista
          
    def dzień_w_którym_zaobserwowano_najwyzsza(self):  
        print ("Dzień w którym była najwyższa temperatura: " + str(max(self.lista_temperatur()))  + " to "+ ("-".join(self.otwarcie_pliku()[self.lista_temperatur().index(max(self.lista_temperatur()))].split(";")[0:3])))
        return (max(self.lista_temperatur()))

    def dzień_w_którym_zaobserwowano_najnizsza(self):  
        print ("Dzień w którym była najniższa temperatura: " + str(min(self.lista_temperatur()))  + " to "+ ("-".join(self.otwarcie_pliku()[self.lista_temperatur().index(min(self.lista_temperatur()))].split(";")[0:3])))

    def indexy_min(self):
        indexies = [i for i, x in enumerate(self.lista_temperatur()) if x == min(self.lista_temperatur())]
        return (indexies)

    def indexy_max(self):
        indexies = [i for i, x in enumerate(self.lista_temperatur()) if x == max(self.lista_temperatur())]
        return (indexies)
        
    def dzień_w_którym_zaobserwowano_najwyzsza2(self):    
        for i in self.indexy_max():
            print ("Dzień w którym była najwyższa temperatura: " + str(max(self.lista_temperatur()))  + " to "+ ("-".join(self.odczyt_pliku_obliczeniowego()[int(i)].split(";")[0:3])))
        return max(self.lista_temperatur())
    
    def dzień_w_którym_zaobserwowano_najnizsza2(self):
        for i in self.indexy_min():
              print ("Dzień w którym była najniższa temperatura: " + str(min(self.lista_temperatur()))  + " to "+ ("-".join(self.odczyt_pliku_obliczeniowego()[int(i)].split(";")[0:3])))
        return min(self.lista_temperatur())
        
    def kawałki_temp(self):
        return [self.lista_temperatur()[i:i + 24] for i in range(0, len(self.lista_temperatur()), 24)]
    
    def srednia_dla_poszczegolnych_dni(self):
        lista = []
        for i in self.kawałki_temp():
            lista.append(sum(i)/24)
        return lista

    def indexy_min_poszczególne_dni(self):
        indexies = [i for i, x in enumerate(self.srednia_dla_poszczegolnych_dni()) if x == min(self.srednia_dla_poszczegolnych_dni())]
        return (indexies)

    def indexy_max_poszczególne_dni(self):
        indexies = [i for i, x in enumerate(self.srednia_dla_poszczegolnych_dni()) if x == max(self.srednia_dla_poszczegolnych_dni())]
        return (indexies)
        
    def kawałki_plik_obli(self):
        return [self.odczyt_pliku_obliczeniowego()[i:i + 24] for i in range(0, len(self.odczyt_pliku_obliczeniowego()), 24)]

    def najwyzsza_srednia(self): 
        for i in self.indexy_max_poszczególne_dni():
            print ("Dzień w którym była najwyższa srednia temperatura: " + str(max(self.srednia_dla_poszczegolnych_dni()))  + " to "+ ("-".join(self.kawałki_plik_obli()[int(i)][0].split(";")[0:3])))

    def najniższa_srednia(self):
        for i in self.indexy_min_poszczególne_dni():
              print ("Dzień w którym była najniższa srednia temperatura: " + str(min(self.srednia_dla_poszczegolnych_dni()))  + " to "+ ("-".join(self.kawałki_plik_obli()[int(i)][0].split(";")[0:3])))
        
        




