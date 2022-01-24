class NodoFama:

    def __init__(self, usuario, padre=None):
        # No modificar
        self.usuario = usuario
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBinario:

    def __init__(self):
        # No modificar
        self.raiz = None

    def crear_arbol(self, nodos_fama):
        # No modificar
        for nodo in nodos_fama:
            self.insertar_nodo(nodo, self.raiz)

    def insertar_nodo(self, nuevo_nodo, padre=None):
        # Completar
        if nuevo_nodo.padre is None:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.usuario.fama > padre.usuario.fama:
            if padre.hijo_derecho is None:
                padre.hijo_derecho = nuevo_nodo
            else:
                self.insertar_nodo(nuevo_nodo, padre.hijo_derecho)
        elif nuevo_nodo.usuario.fama < padre.usuario.fama:
            if padre.hijo_izquierdo is None:
                padre.hijo_izquierdo = nuevo_nodo
            else:
                self.insertar_nodo(nuevo_nodo, padre.hijo_izquierdo)

    def buscar_nodo(self, fama, padre=None):
        # Completar
        if padre is not None:
            if fama == padre.usuario.fama:
                return padre
            elif fama > padre.usuario.fama:
                return self.buscar_nodo(fama, padre.hijo_derecho)
            elif fama < padre.usuario.fama:
                return self.buscar_nodo(fama, padre.hijo_izquierdo)
                
        if fama == self.raiz.usuario.fama:
            return self.raiz
        elif fama > self.raiz.usuario.fama:
            return self.buscar_nodo(fama, self.raiz.hijo_derecho)
        elif fama < self.raiz.usuario.fama:
            return self.buscar_nodo(fama, self.raiz.hijo_izquierdo)
        
        return None
        
        
        

    def print_arbol(self, nodo=None, nivel_indentacion=0):
        # No modificar
        indentacion = "|   " * nivel_indentacion
        if nodo is None:
            print("** DCCelebrity Arbol Binario**")
            self.print_arbol(self.raiz)
        else:
            print(f"{indentacion}{nodo.usuario.nombre}: "
                  f"{nodo.usuario.correo}")
            if nodo.hijo_izquierdo:
                self.print_arbol(nodo.hijo_izquierdo,
                                 nivel_indentacion + 1)
            if nodo.hijo_derecho:
                self.print_arbol(nodo.hijo_derecho,
                                 nivel_indentacion + 1)
