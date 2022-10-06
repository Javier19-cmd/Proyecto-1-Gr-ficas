"""
Referencias: 
 1. Acceder a una variable de una clase: https://www.codigopiton.com/variables-de-clase-y-de-instancia-en-python/#:~:text=Como%20puedes%20ver%2C%20para%20acceder,código%20definido%20en%20la%20clase.
 2. Acceder a un método de una clase: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#:~:text=Para%20crear%20un%20objeto%20de,se%20llamara%20a%20una%20función).&text=El%20código%20anterior%20crea%20una,objeto%20a%20la%20variable%20obj%20.
 3. Inicializar una clase: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=44&codigo=44&inicio=30
 4. Clases en Python: https://tutorial.recursospython.com/clases/#:~:text=Para%20crear%20una%20clase%20vamos,mayúscula%2C%20y%20sin%20guiones%20bajos.
"""
#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from textures import * #Importando los métodos del archivo textures.py.

def main():
    glCreateWindow(1024, 1024) #Creando la ventana.
    glClearColor(1, 1, 1) #Color del fondo.
    glClear() #Limpiando el framebuffer con el color creado en glClearColor.
    glColor(0.5, 0.5, 0.5) #Color del punto.
    
    glViewPort(150, 500, 600, 600) #Asignando el viewport.

    col1 = (0.6, 0.1, 0.9) #Otro color.

    #Probando el lookat.
    # El medium shot se hizo con estas medidas: V3(25, 0, 10), V3(0, 1, 0), V3(0, 1, 0).
    # El low angle se hizo con estas medidas: V3(10, -4.5, 0), V3(1, 0, 0), V3(0, 1, 0).
    # El high agnle se hizo con estas medidas: V3(10, 12, 0), V3(1, 0, 0), V3(0, 1, 0) y las medidas 
    # del viewport fueron glViewPort(900, 500, 300, 300).
    # El dutch angle se hizo con estas medidas: scale = (0.75, 0.75, 1), translate = (1, 0.2, 0)
    # rotacion = (0, 0, pi/2), glViewPort(700, 800, 300, 300) y lookAt(V3(0, 0, 10), V3(0, 1, 0), V3(0, 1, 0)). 
    lookAt(V3(25, 0, 10), V3(0, 1, 0), V3(0, 1, 0))

    scale = (0.5, 0.5, 0.5) #Escala para las cajas.
    translate = (0, 0, 0) #Traslación para las cajas.
    
    rotacion = (0, pi/6, 0) #Rotación para las cajas.

    print("Rotación: ", rotacion)
    
    #Esta llamada puede no estar acá.
    loadModelMatrix(translate, scale, rotacion) #Se carga la matriz de transformación del modelo. Acá se recibe la traslación, la escala y la rotación.

    #Esta función ahora recibe primero el path del obj, luego el path del bmp, el color.
    modelo("./model.obj", "./model.bmp", col1)

    #dibujar("triangle") #Dibujando la imagen.
    #dibujar("square") #Dibujando la imagen.
    
    drawModel() #Dibujando los triángulos del modelo.
    # draw_square() #Dibujando la imagen.

    #drawModel() #Dibujando el modelo.

    #triangle() #Dibujando un triángulo nada más.

    glFinish() #Escribiendo el framebuffer en la imagen y guardándola en un archivo.

main()