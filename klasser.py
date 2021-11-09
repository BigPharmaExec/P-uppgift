import tkinter as tk
import random as rnd

class Memory:
    """Klass som skapar memory brädet med storlek 6 x 6"""
    def __init__(self, text_lista):
        self.fönster = tk.Tk()
        self.rad = 6
        self.kolumn = 6
        self.text_lista = text_lista
        self.räknare = 0
        self.knapp_lista = []
        self.namn = "Användare"

        #variabel som sparar texten från senaste knapptryckningen för att jämföra med nuvarande
        #återställs till -1 vartannat tryck
        self.senaste_försöket = -1

        #self.välkommen = tk.Label(text="Välkommen till Memory, Skriv in ditt namn:")

        
        nummer = 0
        for i in range(1, self.rad+1):    
            for j in range(self.kolumn):                
                self.skapa_knapp(i, j, nummer)
                nummer = nummer + 1
        

        self.fönster.mainloop()
        
    
    def skapa_bräde(self):
        pass
        
    
    def skapa_knapp(self, rad, kolumn, nummer):
        knapp = tk.Button(text="---", command=lambda id = nummer:self.knapptryckning(id))
        knapp.grid(row=rad, column=kolumn)
        self.knapp_lista.append(knapp)

    def knapptryckning(self, nummer):
        if nummer == self.senaste_försöket:
            return
        self.räknare = self.räknare + 1
        #print(self.räknare)
        #print(self.knapp_lista[nummer])
        print(self.text_lista[nummer])
        print(nummer)
        self.knapp_lista[nummer].config(text=self.text_lista[nummer])
        '''
        if self.jämför_svar(nummer):
            self.knapp_lista[self.senaste_försöket].config(text=self.text_lista[self.senaste_försöket])
        else:
            self.knapp_lista[nummer].config(text="---")    
    def jämför_svar(self, nummer):
        if self.räknare % 2 == 0:
            if self.text_lista[nummer] == self.text_lista[self.senaste_försöket]:
                self.senaste_försöket = -1
                return True            
        else:
            self.senaste_försöket = nummer
'''

    


def fil_till_lista(antal_ord):
    '''Funktion som konverterar ett visst antal ord från en fil till en lista slumpmässsigt, 
    lägger till dubbletter till varje ord, blandar den listan och returerar den'''
    lista = []
    while True:
    
        fil = open("/Users/alexanderek/Desktop/Python projects/test/memo.txt", 'r')
        for rad in fil:                
            lista.append(rad.strip())

        lista = 2*rnd.sample(lista, antal_ord)
        rnd.shuffle(lista)
        return lista


    

def main():
    text_lista = fil_till_lista(18)
    Memory(text_lista)
    

if __name__ == "__main__":
    main()
