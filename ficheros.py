import os

class ficheros:
    
    ruta = ""
    
    ext_imagenes = ['.jpg', '.jpge', '.png', '.webp', '.gif', '.ico']
    ext_documents = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt']
    ext_videos = ['.mp4', '.avi', '.mkv', '.mov', '.flv']
    ext_audio = ['.mp3', '.ogg', '.wav']
    
    imagenes = []
    documentos = []
    videos = []
    audios = []
    otros = []
    
    def __init__(self, ruta):
        self.ruta = ruta
        self.crearDirectorios("Imagenes")
        self.crearDirectorios("Documentos")
        self.crearDirectorios("Videos")
        self.crearDirectorios("Audios")
        self.crearDirectorios("Otros")
        self.listarDirectorio()
        self.ordenar()
        
    def crearDirectorios(self, nombreDirectorio):
        try:
            os.mkdir(self.ruta + "/" + nombreDirectorio)
        except OSError:
            print("")
        else:
            print("Se ha creado el directorio")
    
    def ordenar(self):
        for imagen in self.imagenes:
            try:
                os.rename(self.ruta + "/" + imagen, self.ruta + "/Imagenes/" + imagen)
            except FileNotFoundError:
                print("")
        
        for documento in self.documentos:
            try:
                os.rename(self.ruta + "/" + documento, self.ruta + "/Documentos/" + documento)
            except FileNotFoundError:
                print("")
            
        for video in self.videos:
            try:
                os.rename(self.ruta + "/" + video, self.ruta + "/Videos/" + video)
            except FileNotFoundError:
                print("")
            
        for audio in self.audios:
            try:
                os.rename(self.ruta + "/" + audio, self.ruta + "/Audios/" + audio)
            except FileNotFoundError:
                print("")
        
        for otro in self.otros:
            try:
                os.rename(self.ruta + "/" + otro, self.ruta + "/Otros/" + otro)
            except FileNotFoundError:
                print("")
    
    def guardarFicheros(self, fichero, ext_list, tipo):
        for ext in ext_list:
            if fichero.endswith(ext):
                tipo.append(fichero)
                return True
    
    def listarDirectorio(self):
        with os.scandir(self.ruta) as ficheros:
            for fichero in ficheros:
                if fichero.is_file():
                    if self.guardarFicheros(fichero.name, self.ext_imagenes, self.imagenes) or self.guardarFicheros(fichero.name, self.ext_documents, self.documentos) or self.guardarFicheros(fichero.name, self.ext_videos, self.videos) or self.guardarFicheros(fichero.name, self.ext_audio, self.audios):
                        print("")
                    else:
                        self.otros.append(fichero.name)
                    
