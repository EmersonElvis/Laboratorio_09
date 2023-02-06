class Nodo: #Crear una clase de nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
 
class ListaCircularEnlazada: #Crear una clase que cree una lista circular vinculada
    def __init__(self): #Dedinir los punteros
        self.primero = None
        self.ultimo = None
 
    def vacia(self):#Determina si la lista circular está vacía
        return self.primero == None #Esta linea indica que me duevuelve un dato de tipo boolean (Si o No) 

    def agregar_inicio(self, dato):#Agregar un nodo al inicio
        if self.vacia(): #Si la lista esta vacia
            self.primero = self.ultimo = Nodo(dato) #el puntero primero y ultimo apuntaran al nuevo dato
            self.ultimo.siguiente = self.primero #Puntero ultimo siguiente apuntara al nodo primero
        else: #Caso contrario
            aux = Nodo(dato) #Crea un auxiliar
            aux.siguiente = self.primero #auxiliar siguiente apuntara al primer nodo antiguo
            self.primero = aux #puntero primero apuntara al nuevo nodo
            self.ultimo.siguiente = self.primero #puntero ultimo siguiente apuntara al nuevo nodo

    def eliminar_inicio(self):#Eliminar un nodo al inicio
        if self.vacia():#Si la lista esta vacia
            print("Lista vacia")#Imprime
        elif self.primero == self.ultimo:#Si el puntero primero es igual al ultimo
            self.primero = self.ultimo = None #puntero primero y ultimo apuntaran al vacia
        else:#Caso contrario
            self.primero = self.primero.siguiente #el puntero primero apuntara a la siguiente nodo
            self.ultimo.siguiente = self.primero #el puntero ultimo apuntara al nuevo nodo primero 
        
    def agregar_final(self, dato):#Agregar un nodo al final
        if self.vacia():#Si la lista esta vacia
            self.primero = self.ultimo = Nodo(dato) #Primero y ultimo puntero apuntaran al nuevo nodo
            self.ultimo.siguiente = self.primero #puntero ultimo siguiente apuntara al nuevo nodo
        else:#Caso contrario
            aux = self.ultimo #Auxiliar sera el ultimo nodo
            self.ultimo = aux.siguiente = Nodo(dato) #el ultimo puntero apuntara al ultimo nodo ingresado
            self.ultimo.siguiente = self.primero #Puntero ultimo siguiente ingresado apuntara al primer nodo
    
    def eliminar_final(self):#Eliminar nodo final
        if self.vacia():#Si la lista esta vacia
            print("Lista vacia") #Imprime
        elif self.primero == self.ultimo: #si el primer u ultimo puntero son iguales
            self.primero = self.ultimo = None #tanto y el primero y ultimo puntero apuntaran al vacio
        else:#Caso contrario
            aux = self.primero #Aulixiar estaria en el primer nodo
            while aux.siguiente != self.ultimo: #MIentras que el auxiliar siguiente sea diferente del puntero ultimo
                aux = aux.siguiente #Avanza el auxiliar a la siguiente nodo
            aux.siguiente = self.primero #Auxiliar penultimo apuntara a primer nodo
            self.ultimo = aux #Puntero ultimo seria el ultimo nodo
 
    def mostrar(self):
        aux = self.primero #Asignando a la variable aux el valor del primer nodo
        while aux: #Mientras que sea verdadera
            print(aux.dato) #Imprime dato del nodo actual, almacenando en la variable aux
            aux = aux.siguiente #Asiganamos a la varibale aux el nodo siguiente 
            if aux == self.primero: #Si el auxiliar es igual al puntero primero
                break #se rompe el bucle
 
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircularEnlazada() 
        while opcion != 7:
            print("""\n\tLISTA CIRCULAR ENLAZADA:\n
        1. Agregar Inicio
        2. Eliminar Inicio
        3. Agregar Final
        4. Eliminar Final
        5. Mostrar 
        6. Lista vacia?
        7. Salir""")
            opcion = int(input("Ingrese su opcion: "))
            
            if opcion == 1:
                dato = input("Ingrese un Dato ")
                lista.agregar_inicio(dato)
            elif opcion == 2:
                lista.eliminar_inicio()
            elif opcion == 3:
                dato = input("Ingrese un Dato ")
                lista.agregar_final(dato)
            elif opcion == 4:
                lista.eliminar_final()
            elif opcion == 5:
                lista.mostrar()
            elif opcion == 6:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 7:
                print("Fin")
            else:
                print("Ingrese una de las opciones de la lista: ") 
except Exception as e:
    print(e)    
              
