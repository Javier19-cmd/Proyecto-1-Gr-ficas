"""
#Nombre: Javier Valle
#Carnet: 20159

Referencias: 

1. Instanciar un archivo de Python: https://www.youtube.com/watch?v=rYcluou5gEo&ab_channel=LuisCabreraBenito
2. Saber si un número es múltiplo de otro: https://www.youtube.com/watch?v=jOCh6ZpkE1k&ab_channel=JohnOrtizOrdoñez
3. Hacer un return de múltiples variables: https://www.youtube.com/watch?v=QOQTYuynU3w&ab_channel=ProgramaResuelto
4. Formato de archivo BMP: https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20BMP%20file%20format%2C%20also,and%20OS%2F2%20operating%20systems. 
5. Acceder a una variable de otra clase: https://programmerclick.com/article/14131486210/
6. Algoritmo de Lineas Bresenham: https://es.wikipedia.org/wiki/Algoritmo_de_Bresenham#:~:text=El%20Algoritmo%20de%20Bresenham%20es,solo%20realiza%20cálculos%20con%20enteros.
7. Algoritmo de Bresenham: https://www.youtube.com/watch?v=yaovJmM-0OM&ab_channel=CodesVille
8. Simular un do-while: https://www.freecodecamp.org/espanol/news/python-bucle-do-while-ejemplos-de-bucles/#:~:text=Para%20crear%20un%20bucle%20do%20while%20en%20Python%2C%20necesitas%20modificar,verdadero%20se%20ejecutará%20otra%20vez.
"""


"""
SR4:

1. Coordenadas baricéntricas (Ejemplo 9): 
    https://www.programcreek.com/python/?CodeExample=get+bounding+box

2. Evitando la división entre cero: 
    https://www.yawintutor.com/zerodivisionerror-division-by-zero/
"""

from Render import * #Importando la clase Render.
from utilidades import *
from vector import *
from Obj import *
from textures import *
from math import *
#Importando la clase de matriz.
from Matrixes import *

#Importando numpy de manera temoral.
#from numpy import *

c1 = Render() #Inicializando la clase Render.
c2 = Texture() #Inicializando las texturas.
#c3 = Matriz() #Inicializando la clase de matrices.

#Pregunar si está bien implementada esta función.
def glInit(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.
    pass

def glCreateWindow(width, height): #Preguntar de esta función.
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)

    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Creando las dimensiones de la pantalla.

            c1.width = width #Ancho de la pantalla.
            c1.height = height #Alto de la pantalla.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.

    #colorV = color(0.4, 0.8, 0.08) #Creando el color del viewport.

    #Verificando que las dimensiones del viewport sean múltiplos de 4.

    loadViewPortMatrix(x, y, width, height)

        


#Preguntar si esta función lo que hace es llenar por primera vez el color de la pantalla.
def glClear(): #Se usará para que llene el mapa de bits con un solo color.   
    

    #print("Colores en glClear ", color(rP, gP, bP)) #Imprimiendo el color que se le pasa.
    
    # if rP < 0 or gP < 0 or bP < 0: #Si los colores son menores a 0, entonces se imprime un error.
    #     print("Error")
    # elif rP > 1 or gP > 1 or bP > 1:
    #     print("Error")
    # else: #Si todo está bien, entonces se llena el mapa de bits con el color que se le pasa.
    #     #print(color(rP, gP, bP))
    
    #c1.Framebuffer() #Llenando el framebuffer con el color que se le pasó en glClearColor.

    c1.framebuffer = [
                    [c1.colorFondo for x in range(c1.width)] #Llenando el framebuffer con el color que se le pasó en glClearColor.
                      for y in range(c1.height)
                    ] #Llenando el framebuffer con el color que se le pasó en glClearColor.

    c1.zBuffer = [
                    [-9999 for x in range(c1.width)] #Llenando el zBuffer con un valor muy pequeño.
                    for y in range(c1.height)
                ] #Llenando el zBuffer con un valor muy pequeño.
    
    #print("zBufferE ", c1.zBufferE) #Imprimiendo el zBufferE.

    #print("zBufferE: ", c1.zBufferE) #Imprimiendo el zBufferE.

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
        
    #Verificando que los códigos de los colores no sean negativos.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1: #Verificando que los códigos de los colores no sean mayores a 255.
        print("Error")
    else: #Si todo está bien, entonces se crea el framebuffer con el color que se le pasa.
        
        #print("Color de fondo antes: ", c1.colorFondo) #Antes de cambiar el color, se imprime el color de fondo.
        
        colorPantalla = color(r, g, b) #Creando el color de la pantalla.
        
        c1.colorFondo = colorPantalla #Se manda a hacer el color de la pantalla.

        #print("Color de fondo: ", c1.colorFondo) #Imprimiendo el color de la pantalla.

        #color(rP, gP, bP) #Color inicial de la pantalla.
       
        #Rend2.recibirColor(color(rP, gP, bP))

        #print("Color en glClearColor: ", color(rP, gP, bP)) #Debuggeo.

def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    
    #Convertir el valor de 0 a 1 de 0 a 255 y luego llamar al color.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1:
        print("Error")
    else:
        
        Color = color(r, g, b) #Se manda a hacer el color con las utilidades y se setea el color.
        #print("Color en gl: ", Color)
        c1.colorP = Color #Se setea el color del punto.

def loadModelMatrix(translate=(0,0,0), scale=(1,1,1), rotate=(0,0,0)): #Función para cargar la matriz de transformación.

    #Convirtiendo los parámetros a V3 por el momento.
    translate = V3(translate[0], translate[1], translate[2])
    scale =     V3(scale[0],         scale[1],     scale[2])
    rotate =    V3(rotate[0],       rotate[1],    rotate[2])

    # #Definiendo la matriz de transformación esto es con numpy.
    # traslation_matrix_np = matrix([
    #     [1, 0, 0, translate.x],
    #     [0, 1, 0, translate.y],
    #     [0, 0, 1, translate.z],
    #     [0, 0, 0,           1]
    # ])

    # #Definiendo la matriz de escala.
    # scale_matrix_np = matrix([
    #     [scale.x, 0, 0, 0],
    #     [0, scale.y, 0, 0],
    #     [0, 0, 1, scale.z],
    #     [0, 0, 0,       1]
    # ])

    # #Definiendo la matriz de rotación.

    # #Rotación en x.
    # a = rotate.x
    # rotation_matrix_x_np = matrix([
    #     [1,    0,        0,  0],
    #     [0, cos(a), -sin(a), 0],
    #     [0, sin(a),  cos(a), 0],
    #     [0,      0,       0, 1]
    # ])

    # #Rotación en y.
    # b = rotate.y
    # rotation_matrix_y_np = matrix([
    #     [cos(b), 0, sin(b),  0],
    #     [0,      1,      0,  0],
    #     [-sin(b), 0, cos(b), 0],
    #     [0, 0, 0, 1]
    # ])

    # #Rotación en z.
    # c = rotate.z
    # rotation_matrix_z_np = matrix([
    #     [cos(c), -sin(c), 0,  0],
    #     [sin(c),  cos(c), 0,  0],
    #     [0,            0, 1,  0],
    #     [0,            0, 0,  1]
    # ])

    ######################################################################################################################################################################

    #Definiendo la matriz de transformación esto es sin numpy.
    traslation_matrix = Matriz([
        [1, 0, 0, translate.x],
        [0, 1, 0, translate.y],
        [0, 0, 1, translate.z],
        [0, 0, 0,           1]
    ])

    #Definiendo la matriz de escala.
    scale_matrix = Matriz([
        [scale.x, 0, 0, 0],
        [0, scale.y, 0, 0],
        [0, 0, 1, scale.z],
        [0, 0, 0,       1]
    ])

    #Definiendo la matriz de rotación.

    #Rotación en x.
    a = rotate.x
    rotation_matrix_x = Matriz([
        [1,    0,        0,  0],
        [0, cos(a), -sin(a), 0],
        [0, sin(a),  cos(a), 0],
        [0,      0,       0, 1]
    ])

    #Rotación en y.
    b = rotate.y
    rotation_matrix_y = Matriz([
        [cos(b),  0, sin(b),  0],
        [0,       1,      0,  0],
        [-sin(b), 0, cos(b),  0],
        [      0, 0,      0,  1]
    ])

    #Rotación en z.
    c = rotate.z
    rotation_matrix_z = Matriz([
        [cos(c), -sin(c), 0,  0],
        [sin(c),  cos(c), 0,  0],
        [0,            0, 1,  0],
        [0,            0, 0,  1]
    ])

    # #Multiplicando las matrices. Estos resultados se deben a numpy.

    #rotation_matrix_np = rotation_matrix_x_np @ rotation_matrix_y_np @ rotation_matrix_z_np #Esto es con numpy.


    #c1.matrix_np = traslation_matrix_np @ scale_matrix_np @ rotation_matrix_np #Esto es con numpy.

    #print("Matriz de rotación: ", rotation_matrix_np) #Debuggeo.
    #print("Matriz de transformación: ", c1.model_s) #Debuggeo.



    #print("Matriz del modelo: ", c1.matrix_np)
    
    #Multiplicación de las matrices. Esto es sin numpy.
    #rotation_matrix = c3.multiplicar(c3.multiplicar(rotation_matrix_x, rotation_matrix_y), rotation_matrix_z) #Esto es sin numpy.
    rotation_matrix = rotation_matrix_x * rotation_matrix_y * rotation_matrix_z #Esto es sin numpy.
    
    #c1.matrix = traslation_matrix @ scale_matrix @ rotation_matrix #Esto es sin numpy.
    #c1.model_s = c3.multiplicar(c3.multiplicar(traslation_matrix, rotation_matrix), scale_matrix) #Esto es sin numpy.
    c1.model_s = traslation_matrix * rotation_matrix * scale_matrix #Esto es sin numpy.

    # print("---------------------------------------------------")
    # print("Matriz de rotación: ")
    # #Imprimiendo fila por fila el cada matriz.
    # for i in range(len(rotation_matrix)):
    #     print(rotation_matrix[i])
    
    # print("Matriz del modelo:")
    # print("---------------------------------------------------")
    # for i in range(len(c1.matrix)):
    #     print(c1.matrix[i])

def loadViewMatrix(x, y, z, center):

    # #Definiendo la matriz de vista. (con numpy)
    # Minv = matrix([
        
    #     [x.x, x.y, x.z, 0],
    #     [y.x, y.y, y.z, 0],
    #     [z.x, z.y, z.z, 0],
    #     [0,     0,   0, 1]
    #     ])

    # Op = matrix([
    #     [1, 0, 0, -center.x],
    #     [0, 1, 0, -center.y],
    #     [0, 0, 1, -center.z],
    #     [0, 0, 0,          1]
    # ])

    #c1.view = Minv @ Op #Multiplicando las matrices.
    #print("Multiplicación con numpy: ", c1.view) #Debuggeo.
        


    #Definiendo la matriz de vista (sin numpy)
    Mi = Matriz([
        [x.x, x.y, x.z, 0],
        [y.x, y.y, y.z, 0],
        [z.x, z.y, z.z, 0],
        [0,     0,   0, 1]
    ]) #Matriz inversa.

    Op2 = Matriz([
        [1, 0, 0, -center.x],
        [0, 1, 0, -center.y],
        [0, 0, 1, -center.z],
        [0, 0, 0,         1]
    ]) # Matriz de traslación.

    #c1.view = c3.multiplicar(Mi, Op2) #Multiplicando las matrices.

    c1.view = Mi * Op2 #Multiplicando las matrices.

    #print("Matriz de vista sin numpy: ", c1.view)

def loadProjectionMatrix(eye, center): #Calculando la proyección de la cámara.

    coeff = -1 /(eye.len() - center.len()) #Calculando el coeficiente de alejamiento.
   
    #Definiendo la matriz de vista (sin numpy)
    c1.Projection = Matriz([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, coeff, 1]
    ])

def loadViewPortMatrix(x, y, w, h): #Calculando la proyección de la cámara.
    
    c1.lista = Matriz([
        [w, 0, 0, x + w],
        [0, h, 0, y + h],
        [0, 0, 128, 128],
        [0, 0, 0, 1]
    ])



def lookAt(eye, center, up): #Recibe donde está la cámara, el centro y que es arriba.
    #Esto da la base del espacio vectorial.

    z = (eye-center).normalice() # Zeta de la cámara.
    x = cross(up, z).normalice() # Equis de la cámara.
    y = cross(z, x).normalice()  # Y de la cámara.

    loadViewMatrix(x, y, z, center) #Cargando la matriz de vista.
    loadProjectionMatrix(eye, center) #Cargando la matriz de proyección.

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda

    if 0 < x < c1.width and 0 < y < c1.height: #Verificando que las coordenadas estén dentro del viewport.
        #Escribiendo el punto directamente en el framebuffer.
        #print("Punto: ", x, y)
        c1.framebuffer[y][x] = c1.colorP #Escribiendo el color el punto en el framebuffer.
        #c1.Vertex(x, y) #Se manda a hacer el punto.

#Función que crea una línea entre dos puntos. Esta tiene que estar en el rango de 0 a 1.
def glLine(v1, v2):
    
    #Redondeo para que no haya problemas con los decimales.
    x0 = round(v1.x)
    y0 = round(v1.y)
    x1 = round(v2.x)
    y1 = round(v2.y)

    #Verifiando las propiedades del viewport.
    #print(ancho, alto, equis, ye)
    
    #Moviendo el punto a la posición deseada.
    # dy = abs(y1 - y0)
    # dx = abs(x1 - x0)

    #print("Posiciones: ", x0, y0, x1, y1)

    #Prueba.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    #Debuggeo.
    #print("Cambio en y y cambio en x ", dy, dx)
    #print("Cambio en x y cambio en y ", dx1, dy1)


    steep = dy > dx #Verificando si la línea es vertical o horizontal.

    if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    
    if x0 > x1: #Si el punto 1 está a la derecha del punto 2, entonces se cambia el orden de los puntos.
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Calculando los nuevos cambios.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    offset = 0 #Offset de la línea.
    threshold = dx #Umbral de la línea.	
    y = y0 #Coordenada y de la línea.

    #Verificando las variables.
    #print("Offset, threshold, y ",offset, threshold, y)

    #Dibujando la línea.
    for x in range(x0, x1 + 1):
        
        offset += dy * 2 #Cambiando el offset.
        if offset >= threshold: #Si el offset es mayor o igual al umbral, entonces se cambia la coordenada y.
            y += 1 if y0 < y1 else -1
            threshold += 2 * dx

            #print("Punto inicial: ", movx1, movy1)
            #print("Punto final: ", movx2, movy2)


        if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
            #print("Coordenadas: ", x, y)
            glVertex(y, x)
            #print(y, x)
        
        else: #Si la línea es horizontal, entonces se cambia el orden de los puntos.
            #print("Puntos dados en decimales ", x0, y0, x1, y1)
            #print("Coordenadas: ", x, y)
            glVertex(x, y)
            #print(x, y)

#Este método recibe ahora dos paths. Uno es para el obj y el otro es para el bmp.
def modelo(path1, path2): #Método para cargar un modelo 3D.
    r = Object(path1) #Llamando al método Object del archivo Obj.py.

    if path2: 
        #Método para hacer el ejemplo de Dennis.
        c2.lectura(path2) #Abriendo el bmp de la textura y procesando sus pixeles.

        c1.tpath = path2 #Se setea la textura.

        #print("Path de la textura: ", c1.tpath) #Debuggeo.

    #print("Textura: ", c1.tpath) #Debuggeo.

    #Recorriendo las caras del objeto y dibujando las líneas en el framebuffer.
    for face in r.faces: 
       
        #print(face) #Debuggeo.
        if c1.tpath: #Si hay una textura, entonces se dibuja la cara con textura.
            if len(face) == 4: #Validando que la cara tenga 4 vértices.
                #El array de caras es bidimensional en este código.
                f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                f2 = face[1][0] - 1 #Agarrando el índice 0.
                f3 = face[2][0] - 1 #Agarrando el índice 1.
                f4 = face[3][0] - 1 #Agarrando el índice 2.

                #Transformando los vértices.
                v1 = transform_vertex(r.vertices[f1]) 
                v2 = transform_vertex(r.vertices[f2])
                v3 = transform_vertex(r.vertices[f3])
                v4 = transform_vertex(r.vertices[f4])

                if c1.tpath: #Si hay una textura, entonces se dibuja la cara con textura.
                    
                    ft1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                    ft2 = face[1][1] - 1 #Agarrando el índice 0.
                    ft3 = face[2][1] - 1 #Agarrando el índice 1.
                    ft4 = face[3][1] - 1 #Agarrando el índice 2.

                    #Transformando los vértices.
                    vt1 = V3(*r.vts[ft1])
                    vt2 = V3(*r.vts[ft2])
                    vt3 = V3(*r.vts[ft3])
                    vt4 = V3(*r.vts[ft4])

                    if r.normal:
                        #Verificando si el modelo tiene normales.
                        #Jalando las normales de los vértices.
                        fn1 = face[0][2] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                        fn2 = face[1][2] - 1 #Agarrando el índice 0.
                        fn3 = face[2][2] - 1 #Agarrando el índice 1.
                        fn4 = face[3][2] - 1 #Agarrando el índice 2.

                        #Transformando los vértices.
                        vn1 = V3(*r.normal[fn1])
                        vn2 = V3(*r.normal[fn2])
                        vn3 = V3(*r.normal[fn3])
                        vn4 = V3(*r.normal[fn4])

                #Ahora se generan los triángulos.
                
                #Guardando el primer triángulo.

                #Vértices del triángulo.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v2)
                c1.vertex_buffer_obj.append(v3)

                #Texturas del triángulo.
                c1.vertex_buffer_obj.append(vt1)
                c1.vertex_buffer_obj.append(vt2)
                c1.vertex_buffer_obj.append(vt3)

                #Normales del triángulo.
                c1.vertex_buffer_obj.append(vn1)
                c1.vertex_buffer_obj.append(vn2)
                c1.vertex_buffer_obj.append(vn3)

                #Guardando el segundo triángulo.

                #Vértices del triángulo.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v3)
                c1.vertex_buffer_obj.append(v4)

                #Texturas del triángulo.
                c1.vertex_buffer_obj.append(vt1)
                c1.vertex_buffer_obj.append(vt3)
                c1.vertex_buffer_obj.append(vt4)

                #Normales del triángulo.
                c1.vertex_buffer_obj.append(vn1)
                c1.vertex_buffer_obj.append(vn3)
                c1.vertex_buffer_obj.append(vn4)
                        
            
            elif len(face) == 3: #Validando que la cara tenga 3 vértices.
                #El array de caras es bidimensional en este código.
                f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                f2 = face[1][0] - 1 #Agarrando el índice 0.
                f3 = face[2][0] - 1 #Agarrando el índice 1.
                #f4 = face[3][0] - 1 #Agarrando el índice 2.

                #Transformando los vértices.
                v1 = transform_vertex(r.vertices[f1]) 
                v2 = transform_vertex(r.vertices[f2])
                v3 = transform_vertex(r.vertices[f3])
                #v4 = transform_vertex(r.vertices[f4])

                #Guardando los vértices en una lista.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v2)
                c1.vertex_buffer_obj.append(v3)

                if c1.tpath: #Si hay una textura, entonces se dibuja la cara con textura.
                    
                    ft1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                    ft2 = face[1][1] - 1 #Agarrando el índice 0.
                    ft3 = face[2][1] - 1 #Agarrando el índice 1.
                    #ft4 = face[3][1] - 1 #Agarrando el índice 2.

                    #Transformando los vértices.
                    vt1 = V3(*r.vts[ft1])
                    vt2 = V3(*r.vts[ft2])
                    vt3 = V3(*r.vts[ft3])
                    #vt4 = V3(*r.vts[ft4])

                    #Guardando los vértices en una lista.
                    c1.vertex_buffer_obj.append(vt1)
                    c1.vertex_buffer_obj.append(vt2)
                    c1.vertex_buffer_obj.append(vt3)

                    if r.normal:                        
                    #Verificando si el modelo tiene normales.
                        #Jalando las normales de los vértices.
                        fn1 = face[0][2] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                        fn2 = face[1][2] - 1 #Agarrando el índice 0.
                        fn3 = face[2][2] - 1 #Agarrando el índice 1.
                        #fn4 = face[3][2] - 1 #Agarrando el índice 2.

                        #Transformando los vértices.
                        vn1 = V3(*r.normal[fn1])
                        vn2 = V3(*r.normal[fn2])
                        vn3 = V3(*r.normal[fn3])
                        #vn4 = V3(*r.normal[fn4])

                        #Guardando los vértices en una lista.
                        c1.vertex_buffer_obj.append(vn1)
                        c1.vertex_buffer_obj.append(vn2)
                        c1.vertex_buffer_obj.append(vn3)

                        c1.normales = True #Activando las normales.

def dibujar(poligono): #Función para dibujar los polígonos.
    c1.active_vertex_array = iter(c1.vertex_buffer_obj) #Iterando el vertex buffer object.
    
    #Dibujando los polígonos.
    if poligono == 'triangle': #Dibujando triángulos.
        try:
            while True: #Dibujando los triángulos.
                triangle() #Dibujando el triángulo.
                #triangle_wire() #Dibujando los triángulos.
                #drawModel() #Dibujando los triángulos.
        except StopIteration:
            print('Dibujando triángulos...')

    elif poligono == 'square': #Dibujando cuadrados.
        try:
            while True:
                #triangle_wire() #Dibujando los triángulos.
                square_wire() #Dibujando los cuadrados.
        except StopIteration:
            print('Dibujando cuadrados...')

#Función para dibujar los triángulos.
def drawModel():
    c1.active_vertex_array = iter(c1.vertex_buffer_obj) #Iterando el vertex buffer object.

    try:
        while True:
            #Dibujando los triángulos.
            triangle()
    except StopIteration:
            print('Dibujando triángulos...')

#Función para dibujar los cuadrados.
def draw_square():
    try:
        while True:
            #Dibujando los cuadrados.
            square()
    except StopIteration:
            print('Dibujando cuadrados...')

def square():
    #Dibujando los cuadrados.
    A = next(c1.active_vertex_array)
    B = next(c1.active_vertex_array)
    C = next(c1.active_vertex_array)
    D = next(c1.active_vertex_array)

    #Dibujando los cuadrados.
    triangle(A, B, C)
    triangle(A, C, D)

def triangle_wire(): #Función para dibujar los triángulos en wireframe.
    #Dibujando los triángulos.
    A = next(c1.active_vertex_array)
    B = next(c1.active_vertex_array)
    C = next(c1.active_vertex_array)

    if c1.tpath: #Verificando que sí haya una textura.
        tA = next(c1.active_vertex_array)
        tB = next(c1.active_vertex_array)
        tC = next(c1.active_vertex_array)

    # if c1.normales: #Verificando que sí haya normales.
    #     nA = next(c1.active_vertex_array)
    #     nB = next(c1.active_vertex_array)
    #     nC = next(c1.active_vertex_array)
        
    # else: #Si no hay textura, entonces se dibuja el wireframe.
        #Dibujando los triángulos.
    glLine(A, B)
    glLine(B, C)
    glLine(C, A)

def square_wire(): #Función para dibujar los cuadrados en wireframe.
    #Dibujando los cuadrados.
    A = next(c1.active_vertex_array)
    B = next(c1.active_vertex_array)
    C = next(c1.active_vertex_array)
    D = next(c1.active_vertex_array)

    if c1.tpath: #Si hay textura.
        tA = next(c1.active_vertex_array)
        tB = next(c1.active_vertex_array)
        tC = next(c1.active_vertex_array)
        tD = next(c1.active_vertex_array)
        #print(c1.active_tvertex_array)

    # if c1.normales: #Si hay normales.
    #     nA = next(c1.active_vertex_array)
    #     nB = next(c1.active_vertex_array)
    #     nC = next(c1.active_vertex_array)
    #     nD = next(c1.active_vertex_array)
       
    #Dibujando los triángulos.
    #Dibujando el primer triángulo.
    glLine(A, B)
    glLine(B, C)
    glLine(C, A)

    #Dibujando el segundo triángulo.
    glLine(A, C)
    glLine(C, D)
    glLine(D, A)


#Método para dibujar los triángulos.

def triangle(): #Función que dibuja un triángulo.

    #c1.active_vertex_array = iter(c1.vertex_buffer_obj) #Iterando el vertex buffer object.
    # c1.active_tvertex_array = iter(c1.tvertex_buffer_obj) #Iterando el vertex buffer object.
    # c1.active_nvertex_array = iter(c1.nvertex_buffer_obj) #Iterando el vertex buffer object.

    #Recibiendo los valores de cada vértice.
    A = next(c1.active_vertex_array)
    B = next(c1.active_vertex_array)
    C = next(c1.active_vertex_array)

    if c1.tpath: #Si el path2 no está vacío, entonces se dibuja el triángulo con textura.
        #Texturas.
        tA = next(c1.active_vertex_array)
        tB = next(c1.active_vertex_array)
        tC = next(c1.active_vertex_array)

       # print(tA, tB, tC)

    #Normales.
    nA = next(c1.active_vertex_array)
    nB = next(c1.active_vertex_array)
    nC = next(c1.active_vertex_array)


    #print(col[0], col[1], col[2])

    #print(A, B, C) #Se imprimen las coordenadas.

    L = V3(0, 1, 1) #Vector de la luz.

    #print("Intensidad: ", i) #Se imprime la intensidad.

    #print("Color: ", c1.colorP)

    #c1.colorP = col #Se setea el color del punto. (En este caso gris)


    #Calculando los mínimos y máximos de los puntos.
    min, max = bounding_box(A, B, C) #Se calculan los mínimos y máximos de los puntos.

    #print("Mínimos: ", min.x, min.y)
    #print("Máximos: ", max.x, max.y)

    #Redondeando los mínimos y máximos para poderlos meter a los for-loops.
    min.round()
    max.round()


    for x in range(min.x, max.x + 1):
        for y in range(min.y, max.y + 1):
            w, u, v = baricentrico(A, B, C, V3(x, y)) #Se calcula el baricéntrico.

            if u < 0 or v < 0 or w < 0: #Si el baricéntrico es mayor o igual a 0, entonces se dibuja el punto.
                #print("Punto: ", x, y)
                continue
            
            #print("Color del fondo: ", c1.colorFondo)
            #print("Color del punto", c1.colorP)

            z = A.z * w + B.z * v + C.z * u #Se calcula la z.

            if (
                c1.zBuffer[x][y] < z
                ): #Si el zBuffer es menor a z, entonces se dibuja el punto.
                c1.zBuffer[x][y] = z #Se setea la z.
                
                #print("Color del punto: ", active_shader)
                
                c1.colorP = shader(
                    c1, 
                    bar=(w, u, v),
                    texture_coords=(tA, tB, tC),
                    normales=(nA, nB, nC),
                    vertices=(A, B, C),
                    light = L
                    ) #Creando los shaders con la función shader.

                glVertex(x, y) #Se dibuja el punto.

            #glVertex(x, y) #Se dibuja el punto.


def shader(render, **kwargs): #Función hace los shaders.
   w, u, v = kwargs['bar'] #Se obtienen los valores de u, v y w.
   tA, tB, tC = kwargs['texture_coords'] #Se obtienen los vértices de textura.
   nA, nB, nC = kwargs['normales'] #Se obtienen los vértices de normales.
   A, B, C = kwargs['vertices'] #Se obtienen los vértices.
   L = kwargs['light'] #Se obtiene el vector de la luz.


   iA = nA.normalice() @ L.normalice() #Se calcula la intensidad del punto A.
   iB = nB.normalice() @ L.normalice() #Se calcula la intensidad del punto B.
   iC = nC.normalice() @ L.normalice() #Se calcula la intensidad del punto C.

   i = abs(iA * v + iB * w + iC * u) #Se calcula la intensidad del punto P. Este se devuelve en valor absoluto para que no haya valores negativos.

   #print("Textura: ", tA, tB, tC) #Se imprimen los vértices de textura.
   #print("Intensidad: ", i) #Se imprime la intensidad.

   #return color(0.7, 0.5, 0.1) #Se setea el color del punto con textura.

   if render.tpath: #Si el path2 no está vacío, entonces se dibuja el triángulo con textura.
        tx = tA.x * v + tB.x * w + tC.x * u #Se calcula la x de la textura.
        ty = tA.y * v + tB.y * w + tC.y * u #Se calcula la y de la textura.

        #print("Textura: ", abs(tx), abs(ty)) #Se imprimen los vértices de textura.

        #b1, g1, r1 = c2.get_color_with_intensity(tx, ty, i)

        b, g, r = c2.get_color_with_intensity(tx, ty, i) #Se obtiene el color de la textura con la intensidad.

        col = color(r/255, g/255, b/255) #Se crea el color.

        return col #Se setea el color del punto con textura.

    #print("Y: ", y)
    #return color(1, 0, 0)

def fondo(path):
    c2.load(path) #Se lee la imagen.

    #print("Colores: ", c2.pixels) #Se imprimen los colores.

    c1.framebuffer = c2.pixels #Se setea el framebuffer con los colores de la imagen.

#Función que transforma los vértices de la estructura de la imagen.
def transform_vertex(vertex):
    
    #print(vertex)
    #print(scale)

    aumented_vertex = Matriz([
        [vertex[0]], 
        [vertex[1]], 
        [vertex[2]], 
                [1]
        ]) #Se aumenta el vértice a 4 dimensiones.


    #Debuggeo.
    #print("Model matrix: ", model_matrix)
    #print("Aumented vertex: ", aumented_vertex)

    #transformed_vertex = c3.multiplicar(c1.lista, c3.multiplicar(c1.Projection, c3.multiplicar(c3.multiplicar(c1.view, c1.model_s), aumented_vertex))) #Se multiplica el vértice aumentado por la matriz de transformación. Luego se tiene que cambiar a @, porque * es para multiplicar con numpy.
    
    transformed_vertex = c1.lista * c1.Projection * c1.view * c1.model_s * aumented_vertex #Se multiplica el vértice aumentado por la matriz de transformación. Luego se tiene que cambiar a @, porque * es para multiplicar con numpy.

    #Imprimiendo el vértice transformado.
    #print("Transformed vertex: ", transformed_vertex)

    #Imprimiendo cada componente del vértice transformado.
    #print("Transformed vertex x: ", transformed_vertex[0])
    
    #print("Transformed vertex y: ", transformed_vertex[1][0])

    #Recibir la matriz del vector.
    return V3(
        transformed_vertex[0][0]/transformed_vertex[3][0], 
        transformed_vertex[1][0]/transformed_vertex[3][0],
        transformed_vertex[2][0]/transformed_vertex[3][0]
        ) #Se regresa el vértice transformado en términos de vector 3D.



def cross(V1, V2): #Producto cruz entre dos vectores, pero con return de V3.

    return V3(
        V1.y * V2.z - V1.z * V2.y,
        V1.z * V2.x - V1.x * V2.z,
        V1.x * V2.y - V1.y * V2.x
    )

def bounding_box(A, B, C): #Función que calcula el bounding box de un triángulo.

    coords = [(A.x, A.y), (B.x, B.y), (C.x, C.y)] #Se guardan las coordenadas de los puntos.

    #Se calculan las coordenadas mínimas y máximas.
    xmin = 99999
    xmax = -99999
    ymin = 99999
    ymax = -99999


    for (x, y) in coords: #Se recorren las coordenadas.

        if x < xmin: #Si la coordenada x es menor que la mínima, se setea la mínima.
            xmin = x
        if x > xmax: #Si la coordenada x es mayor que la máxima, se setea la máxima.
            xmax = x
        if y < ymin: #Si la coordenada y es menor que la mínima, se setea la mínima.
            ymin = y
        if y > ymax: #Si la coordenada y es mayor que la máxima, se setea la máxima.
            ymax = y

    #print("Coordenadas: ", x, y)

    return V3(xmin, ymin), V3(xmax, ymax) #Se retornan las coordenadas mínimas y máximas.


    #return V3(xmin, xmax), V3(ymin, ymax) #Retornando los valores mínimos y máximos de x y y.

def baricentrico(A, B, C, P):

    cx, cy, cz = V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y)
                    

    #print("¨Producto cruz: ", V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y))

    #print("Valor de cz: ", cz)

    if cz == 0: #Si el valor de cz es 0, entonces el punto no está en el plano.
        u, v = -1, -1
        w = -1

        return (u, v, w)
    else: #Si el valor de cz es diferente de 0, entonces el punto está en el plano.

        u = cx/cz
        v = cy/cz
        w = 1 - (u + v)

        return (u, v, w)


def zBuffer(): 
    
    #Copiar el zBuffer al zBufferE.
    c1.zBufferE = c1.zBuffer.copy() #Copiar el zBuffer al zBufferE.

    #Recorriendo el zBufferE. Si hay un -9999, entonces se cambia por un 0.
    for i in range(c1.height):
        for j in range(c1.width):
            if c1.zBufferE[i][j] == -9999: #Si el zBufferE tiene un -9999, entonces se cambia por un 0.
                c1.zBufferE[i][j] = color(0, 0, 0)
            elif c1.zBufferE[i][j] < 0: #Si el zBufferE tiene un valor menor a 0, entonces se cambia por un 0.
                c1.zBufferE[i][j] = color(0, 0, 0)
            elif c1.zBufferE[i][j] > 1 and c1.zBufferE[i][j] < 255: #Si el zBufferE tiene un valor mayor a 1, pero menor a 255, entonces dividir el número entre 255.
                c1.zBufferE[i][j] = color(int(c1.zBufferE[i][j] / 255), int(c1.zBufferE[i][j] / 255), int(c1.zBufferE[i][j] / 255))
                #print(c1.zBufferE[i][j])
            elif c1.zBufferE[i][j] > 255: #Si hay un valor mayor a 255, entonces se cambia por un 1.
                c1.zBufferE[i][j] = color(1, 1, 1)
            else: #Si hay algún color sesgado entre 0 y 1, entonces se pintan.
                c1.zBufferE[i][j] = color(int(c1.zBufferE[i][j]), int(c1.zBufferE[i][j]), int(c1.zBufferE[i][j]))


def texturas(path1, path2, col): #Método para dibujar las texturas.

    
    r = Object(path1) #Llamando al método Object del archivo Obj.py.

    #Método para hacer el ejemplo de Dennis.
    c2.lectura(path2) #Abriendo el bmp de la textura y procesando sus pixeles.

    c1.framebuffer = c2.pixels #Se setea el framebuffer con la textura.

    print(c1.colorFondo)

    #Recorriendo las caras del objeto y dibujando las líneas en el framebuffer.
    for face in r.faces: 
        #print(face) #Debuggeo.
        
        if len(face) == 4: #Validando que la cara tenga 4 vértices.
            #El array de caras es bidimensional en este código.
            f1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][1] - 1 #Agarrando el índice 0.
            f3 = face[2][1] - 1 #Agarrando el índice 1.
            f4 = face[3][1] - 1 #Agarrando el índice 2.

            #Transformando los vértices.
            vt1 = V3(
                r.vts[f1][0] * c2.width,
                r.vts[f1][1] * c2.height
            )

            vt2 = V3(
                r.vts[f2][0] * c2.width,
                r.vts[f2][1] * c2.height
            )

            vt3 = V3(
                r.vts[f3][0] * c2.width,
                r.vts[f3][1] * c2.height
            )

            vt4 = V3(
                r.vts[f4][0] * c2.width,
                r.vts[f4][1] * c2.height
            )

            #print("Cara: ", f1, f2, f3, f4)

            # #Dibujando los triangulos.
            # triangle(vt1, vt2, vt4)
            # triangle(vt2, vt3, vt4)

            # #Dibujando triángulos con líneas por el momento.
            glLine(vt1, vt2)
            glLine(vt2, vt3)
            glLine(vt3, vt1)
            
            # #Dibujar triángulos con líneas y el vértice 4.
            glLine(vt2, vt3)
            glLine(vt3, vt4)
            glLine(vt4, vt2)


        elif len(face) == 3: #Validando que la cara tenga 3 vértices.
            
            f1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][1] - 1 #Agarrando el índice 0.
            f3 = face[2][1] - 1 #Agarrando el índice 1.
            #f4 = face[3][0] - 1 #Agarrando el índice 2.

            #print(r.vts[f1]) #Debuggeo.

            #print(r.vertices[f1], scale, translate)

            #Transformando los vértices.
            #Obteniendo los vértices del tamaño de la escala y la translación.
            vt1 = V3(
                r.vts[f1][0] * c2.width,
                r.vts[f1][1] * c2.height
            )

            vt2 = V3(
                r.vts[f2][0] * c2.width,
                r.vts[f2][1] * c2.height
            )

            vt3 = V3(
                r.vts[f3][0] * c2.width,
                r.vts[f3][1] * c2.height
            )
            
            #print("Cara: ", f1, f2, f3)

            #print("Vértices: ", vt1, vt2, vt3)

            #colr = color(1, 0, 0) #Color para el triángulo.

            # #Pintando un triángulo por ahora.
            glLine(vt1, vt2)
            glLine(vt2, vt3)
            glLine(vt3, vt1)
            

            #triangle(vt1, vt2, vt3, col1) #Llamando al método triangle para dibujar un triángulo.

def glFinish(): #Función que escribe el archivo de imagen resultante.

   c1.write() #Escribiendo el archivo.
   #c1.write2() #Escribiendo el archivo con el zBuffer.


