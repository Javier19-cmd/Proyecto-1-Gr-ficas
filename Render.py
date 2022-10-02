from utilidades import * #Archivo de utilidades.

class Render(object):

    #Estas variables son globales y tienen valores por defecto y arbitrarios.
    GRAY = color(0.501, 0.501, 0.501) #Color blanco hecho con las utilidades.
    colorFondo = 0 #Asignando el color blanco al framebuffer.
    #print("Color del fondo: ", colorFondo)
    colorViewPort = GRAY #Asignando el color blanco al viewport. Esto es temporal-
    width = 0 #Ancho de la pantalla. Esto es temporal.
    height = 0 #Alto de la pantalla. Esto es temporal.
    
    widthV = 0 #Ancho del viewport. Esto es temporal.
    heightV = 0 #Alto del viewport. Esto es temporal.

    xV = 0 #Posición en x del viewport.
    yV = 0 #Posición en y del viewport.

    lista = None #Lista para generar el viewport.

    colorP = 0 #Asignando el color blanco al punto. Esto es temporal.

    framebuffer = [] #Framebuffer.

    zBuffer = [] #Zbuffer.

    zBufferE = [] #Copia del zbuffer, que servirá para escribir el archivo del zbuffer.

    colorZ = 0 #Color del zbuffer.

    tpath = None  #Path de las texturas. Aquí se inicializa en none porque aún no se sabe si hay texturas del personaje.

    #Declarando una matriz para el modelo.
    model_np = None #Quitar después.

    model_s = None

    #Declarando una matriz de vista.
    view_np = None #Quitar después.

    view = None

    #Declarando la matriz de proyección.
    Projection = None

    #Creando matrices para el vértice y para el objeto.
    vertex_buffer_obj = [] #Buffer del vérice.

    active_vertex_array = [] #Lista para los vértices.

    #Método que escribe el archivo bmp.
    def write(self): #Escribir un archivo, pero con el zbuffer.
            
            #Se abre el archivo con la forma de bw.
            f = open("Proyecto_1.bmp", "bw")

            #Se escribe el encabezado del archivo.

            #Haciendo el pixel header.
            f.write(char('B'))
            f.write(char('M'))
            #Escribiendo el tamaño del archivo en bytes.
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0)) #Cosa que no se utilizará en este caso.
            f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
            #Lo anterior suma 14 bytes.

            #Información del header.
            f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
            f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
            f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
            #Pixels que no se usarán mucho.
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #Lo anterior suma 40 bytes.

            #print("Framebuffer", framebuffer)
            #Pintando el archivo de color negro.
            for y in range(self.height):
                for x in range(self.width):
                    f.write(self.framebuffer[y][x])

            #print("Archivo escrito")

            f.close() #Cerrando el archivo que se escribió.

    #Método que escribe el archivo bmp.
    def write2(self): #Escribir un archivo, pero con el zbuffer.
            
            #Se abre el archivo con la forma de bw.
            f = open("SR4_2.bmp", "bw")

            #Se escribe el encabezado del archivo.

            #Haciendo el pixel header.
            f.write(char('B'))
            f.write(char('M'))
            #Escribiendo el tamaño del archivo en bytes.
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0)) #Cosa que no se utilizará en este caso.
            f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
            #Lo anterior suma 14 bytes.

            #Información del header.
            f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
            f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
            f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
            #Pixels que no se usarán mucho.
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #Lo anterior suma 40 bytes.

            #print("Framebuffer", framebuffer)
            #Pintando el archivo de color negro.
            for y in range(self.height):
                for x in range(self.width):
                    f.write(self.zBufferE[x][y])

            #print("Archivo escrito")

            f.close() #Cerrando el archivo que se escribió.