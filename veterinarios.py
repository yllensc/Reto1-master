import os
import json
import core
VetsInfo= {"Veterinarios":[]}
def LoadInfoVets():
    global VetsInfo
    if (core.CheckFile("veterinarios.json")):
        infoVeterinarios = core.LoadInfo("veterinarios.json")
    else:
        core.AddInfo("veterinarios.json",infoVeterinarios)
def VetMenu():
    opcion=None
    passive=True
    while(passive):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^14}{}{:^20}|".format(' ','GESTION DE VETERINARIOS',' '))
        print('+','-'*55,'+')
        print("1. Agregar Veterinario.")
        print("2. Buscar Veterinario.")
        print("3. Motrar Informacion de un Veterinario.")
        print("4. Volver al Menu Principal.")
        opcion=int(input("Digite la Opcion: "))
        if(opcion==1):
            pass
        elif(opcion==2):
            pass
        elif(opcion==3):
            pass
        elif(opcion==4):
            passive=False
def AddVet():
    vet={
        "Id":input("Digite el Id del Veterinario: "),
        "Nombre":input("Digite el Nombre del Veterinario: "),
        "Titulo-Profesional":input("Digite el Titulo Prpofesional del Veterinario: "),
        "Fecha-Registro":input("Digite la Fecha de Registro del Veterinario: ")
    }

