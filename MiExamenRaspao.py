#Crear una clase bateria que me permita instanciar una bateria y demostrar el uso de copy y deecopy 
# modificando la copia sin afectar la original crear nodo bateria y lista bateria con un unico puntero 
# cabeza implementar los metodos insertar al incio y purgar agotadas el cual debe recorrer la lista y 
# reconectar los punteros y elimine la bateria con menos de 3v

import copy

class Bateria:
    def __init__(self, id_bateria: str, voltaje: float) -> None:
            self.id_lectura: str = id_bateria
            self.voltaje: float = voltaje

class NodoBateria:

    def __init__(self, id_bateria: str, voltaje: float) -> None:
            self.id_lectura: str = id_bateria
            self.voltaje: float = voltaje
            
class ListaBateria:
        def __init__(self):
            self.cabeza: NodoBateria | None = None
            
        def insertar_inicio(self, id_bateria: str, voltaje: float) -> None:
            nuevo_nodo = Bateria(id_bateria, voltaje)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        def purgar_agotadas(self) -> None:
             while self.cabeza and self.cabeza.voltaje < 3.0:
                self.cabeza = self.cabeza.siguiente
                act = self.cabeza
             while act and act.siguiente:
              if act.siguiente.voltaje < 3.0:
                 act.siguiente = act.siguiente.siguiente
              else:
                act = act.siguiente
                print(f"-> purga de baterias con voltaje menor a 3.0V... {act.id_lectura} ({act.voltaje}V) ")

if __name__ == "__main__":
    print("=== INICIO DE PRUEBAS DEL SISTEMA ==\n")
    
    Bateria1 = Bateria("Bateria_01", 1.5 )
    Bateria2 = Bateria("Bateria_02", 4.2 ) 
    Bateria3 = Bateria("Bateria_03", 2.8 )
    Bateria4 = Bateria("Bateria_04", 1.9 )
    print(f"bateria original: {Bateria1.id_lectura} | voltaje: {Bateria1.voltaje}V")
    print(f"bateria original: {Bateria2.id_lectura} | voltaje: {Bateria2.voltaje}V")
    print(f"bateria original: {Bateria3.id_lectura} | voltaje: {Bateria3.voltaje}V")    
    print(f"bateria original: {Bateria4.id_lectura} | voltaje: {Bateria4.voltaje}V")
    print("\n")        
    

    Bateria_copia_superficial = Bateria1
    Bateria_copia_profunda = copy.deepcopy(Bateria1)
    print(f"ID original: {id(Bateria1)} | ID deepcopy: {id(Bateria_copia_profunda)}")
    print("\n")

    print("=== 2. LISTA ENLAZADA Y PURGA DE BATERÍAS (< 3.0V) ===\n")
    agotadas = ListaBateria()
