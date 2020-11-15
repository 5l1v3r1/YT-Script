import os, pafy
from colorama import Fore, Back, Style, init

init(autoreset=True)

Si = "Si"
SI = "SI"
sI = "sI"
No = "No"
NO = "NO"
nO = "nO"
s = "s"
n = "n"
si = "si"
no = "no"
a = "a"
b = "b"
A = "A"
B = "B"

def pantalla(): 
    if os.name == "posix":
         os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
         os.system ("cls")

def yt_script():
    print("")
    print(Fore.YELLOW +" __   _______   ____            _       _   ")
    print(Fore.YELLOW +" \ \ / /_   _| / ___|  ___ _ __(_)_ __ | |_ ")
    print(Fore.YELLOW +"  \ V /  | |   \___ \ / __| '__| | '_ \| __|")
    print(Fore.YELLOW +"   | |   | |    ___) | (__| |  | | |_) | |_ ")
    print(Fore.YELLOW +"   |_|   |_|   |____/ \___|_|  |_| .__/ \__|")
    print(Fore.YELLOW +"                                 |_|        ", end="")
    print("")
    print("")
    print(Fore.YELLOW +"   [", end="")
    print(Fore.GREEN +"*", end="")
    print(Fore.YELLOW +"]", end="")
    print(Fore.GREEN +" Hecho por wrrulos")
    print(Fore.YELLOW +"   [", end="")
    print(Fore.GREEN +"*", end="")
    print(Fore.YELLOW +"]", end="")
    print(Fore.GREEN +" www.github.com/wrrulos")
    print("")
    print("")
    print(Fore.YELLOW +" [", end="")
    print(Fore.GREEN +"*", end="")
    print(Fore.YELLOW +"]", end="")     
    url = (input(Fore.GREEN +" Ingresa la URL del video: ")) 
    video = pafy.new(url)  
    print("")  
    print(Fore.YELLOW +" [", end="")
    print(Fore.GREEN +"*", end="")
    print(Fore.YELLOW +"]", end="")     
    print(Fore.GREEN +" El nombre del video es: ", video.title, end="")
    print("") 
    pregunta = str(input(Fore.GREEN +" [*] ¿Es correcto? si/no: "))

    if pregunta == s or pregunta == si or pregunta == SI or pregunta == Si or pregunta == sI:
        print("")
        print(Fore.YELLOW +" [", end="")
        print(Fore.GREEN +"*", end="")
        print(Fore.YELLOW +"]", end="")    
        print(Fore.GREEN +" Selecciona el formato:")
        print("")
        print(Fore.GREEN +" [A] MP4 (Video y audio)")
        print(Fore.GREEN +" [B] MP3 (Solo audio)")
        print("")
        print(Fore.YELLOW +" [", end="")
        print(Fore.GREEN +"*", end="")
        print(Fore.YELLOW +"]", end="")   
        formato = str(input(Fore.GREEN +" Elije una opcion: "))

        if formato == A or formato == a:
            print("")  
            print(Fore.YELLOW +" [", end="")
            print(Fore.GREEN +"*", end="")
            print(Fore.YELLOW +"]", end="")   
            nombre = str(input(Fore.GREEN +" Nombre del archivo: "))
            print("")
            archivo = video.getbest()
            archivomp4 = archivo.download(filepath=nombre + ".mp4")  
            print("")
            print(Fore.YELLOW +" [", end="")
            print(Fore.GREEN +"*", end="")
            print(Fore.YELLOW +"] ", end="")               
            print(Fore.GREEN + nombre, end="")  
            print(Fore.GREEN + ".mp4 se guardo en la carpeta del script")
            print("")
        if formato == B or formato == b:
            print("")  
            print(Fore.YELLOW +" [", end="")
            print(Fore.GREEN +"*", end="")
            print(Fore.YELLOW +"]", end="")   
            nombre = str(input(Fore.GREEN +" Nombre del archivo: "))
            print("")
            archivo = video.getbest()
            archivomp4 = archivo.download(filepath=nombre + ".mp3")  
            print("")
            print(Fore.YELLOW +" [", end="")
            print(Fore.GREEN +"*", end="")
            print(Fore.YELLOW +"] ", end="")               
            print(Fore.GREEN + nombre, end="")  
            print(Fore.GREEN + ".mp3 se guardo en la carpeta del script")
            print("")
 
    if pregunta == n or pregunta == no or pregunta == nO or pregunta == NO or pregunta == No:
         pantalla()
         yt_script()            

pantalla()
yt_script()
