from ServidorSocket import Servidor as Server


if __name__ == "__main__":
    
    PATH="C:/Users/nieva/Desktop/AutoFIT-CONTOR/UPLOADS/"

    IP=''
    PORT=11000
    BUFFER=8024
    R=PATH+"Log.txt"
    SERV=Server.Server(IP,PORT,BUFFER,R)

    SERV.IniciarServidor(True,PATH)


    
