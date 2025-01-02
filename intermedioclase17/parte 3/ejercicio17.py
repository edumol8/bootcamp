#Crea una clase LoggerMixin para agregar registro de actividades a otras clases.

class LoggerMixin: 
    def log(self, mensaje): 
        print(f"Log: {mensaje}")

class Usuario(LoggerMixin): 
    def __init__(self, nombre): 
        self.nombre = nombre

    def realizar_actividad(self):
        self.log(f"{self.nombre} realizó una actividad")

usuario = Usuario("Carlos")
usuario.realizar_actividad()  # Log: Carlos realizó una actividad

