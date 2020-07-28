import json
import base64
class Convertidor:

    def __init__(self):
        
        pass  

    def ImagenABytes(self,ruta):
        try:
            with open(ruta,'rb') as Imagen:
                Fichero=Imagen.read()
                ArrayBytes=bytearray(Fichero)
                return ArrayBytes
        except :
            print("Algo ha fallado en el metodo 'Imagen a bytes'")

    def BytesAImagen(self,sruta,Obj):
            jsonl=Obj.decode('utf-8').replace("'","'")
            print(jsonl)
            jsonDic=json.loads(jsonl)
            Name = jsonDic[0]
            Type = jsonDic[1]
            Data = base64.b64decode(jsonDic[2])
            f = open(sruta+Name, 'wb')
            f.write(bytearray(Data))
            f.close()

        
