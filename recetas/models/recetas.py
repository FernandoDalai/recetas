class Receta:
    def __init__(self, id, nombre, dificultad, tiempo, descripcion, costo, calificacion):
        self.id = id
        self.nombre = nombre
        self.dificultad = dificultad
        self.tiempo = tiempo
        self.descripcion = descripcion
        self.costo = costo
        self.calificacion = calificacion
        self.imagen = 'https://www.vvsupremo.com/wp-content/uploads/2015/10/900X570_Enchiladas-Morelia-Style-With-Chorizo-And-Potatoes.jpg'

        self.ingredientes = []
        self.pasos = []

    def agregar_paso(self, paso):
        self.pasos.append(paso)
        return self.pasos

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        return self.ingredientes

    def mostrar_pasos(self):
        return self.pasos

    def mostrar_ingredientes(self):
        return self.ingredientes
