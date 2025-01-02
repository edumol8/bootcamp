class Libro: 
  def __init__(self, titulo, autor): 
    self.titulo = titulo 
    self.autor = autor

  def __str__(self):
    return f"Libro: {self.titulo} por {self.autor}"

  def __repr__(self):
    return f"Libro({self.titulo!r}, {self.autor!r})"
  
libro = Libro("Python Avanzado", "Juan Pérez")
print(str(libro))  # Libro: Python Avanzado por Juan Pérez
print(repr(libro))  # Libro('Python Avanzado', 'Juan Pérez')