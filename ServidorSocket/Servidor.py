import datetime as d
import socket as sk
from .Convertidor.Convertidor import Convertidor as C

class Server:
    def ObtenerIndice(self,r):
        try:
            File=open(r,'r')
            Fs=File.readlines()
            ultimo=int(Fs[len(Fs)-1])        
            File.close()
            return ultimo
        except:
            print("Ha fallado la operacion de obtencion del indice")


    def __init__(self,IP,PORT,BUFFER,r):
        try:
            self.MiSocket=sk.socket()
            self.IP=IP
            self.PORT=PORT
            self.BUFFER=BUFFER
            self.MSG=bytes("Conexion Aceptada",'utf-8')
            self.CONEXION=None
            self.DIRECCION=None
            self.PETICION=None
            self.ruta=r
            self.Exten=".jpg"
            self.dir=open(r,'a+')
            if(len(self.dir.readline())==0):
                self.dir.writelines(str(self.ObtenerIndice(r)) + '\n')
                self.dir.close()
                self.COUNT=self.ObtenerIndice(r)
        except:
            print("Fallo en el constructor")

            
    def IniciarServidor(self,INICIAR=False,ruta=""):
        self.MiSocket.bind((self.IP,self.PORT))
        self.MiSocket.listen(5)
        self.dirl2=open(ruta+"/logConx.txt",'a+')
        while INICIAR:
            
                self.CONEXION,self.DIRECCION=self.MiSocket.accept()
                self.ObtenerIndice(self.ruta) 
                self.PETICION = self.CONEXION.recv(self.BUFFER)
                print(("Conexion: ")+str(self.DIRECCION))
                if  self.PETICION!=None:
                    if len(self.PETICION)>5000:
                        self.dir=open(self.ruta,"a")
                        C.BytesAImagen(self,ruta,self.PETICION)
                        self.COUNT+=1
                        self.dir.writelines(str(self.COUNT)+"\n")
                        self.dir.close()
                        self.dirl2.writelines(str(d.datetime.utcnow())+" - ip:"+str(self.DIRECCION)+"Arch:"+str(self.COUNT)+"\n" )
                        self.dirl2.close()
                    else:
                        print(self.PETICION)
                        html='hola'
                        ms=bytes(html,'utf-8')
                        self.CONEXION.send(ms)
                self.CONEXION.close()
