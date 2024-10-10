#
# github.com/Bbenrod/DataStructures101
# www.youtube.com/@Bbenrod
#

class My_string:
    def __init__(self, texto) -> None:
        self.texto = list(texto)

    def obtener(self, indice:int =None) -> str:
        if not indice:
            return "".join(self.texto)
        else:
            return self.texto[indice]
        
    def longitud(self) -> int:
        return len(self.texto)
    
    def concatenar (self,texto_nuevo: str) -> None:
        for caracter in texto_nuevo:
            self.texto.append(caracter)
            

if __name__ == "__main__":
    string = My_string("Hola")

    print(string.obtener())
    print(string.obtener(3))
    print(string.longitud())

    string.concatenar(" mundo")
    print(string.obtener())