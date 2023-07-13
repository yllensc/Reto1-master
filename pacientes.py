import os
import json
import core
PatientsInfo= {"Pacientes":[]}
def LoadInfoPatients():
    global PatientsInfo
    if (core.CheckFile("pacientes.json")):
        infoPacientes = core.LoadInfo("pacientes.json")
    else:
        core.AddInfo("pacientes.json",infoPacientes)
def PatientsMenu():
    animal={"PERRO":["ROTTWEILER","DOBERMAN","PASTOR ALEMAN","PITBULL"],
          "GATO":["PERSA","AZUL RUSO","SIAMES","SIBERIANO"],
          "REPTIL":["CAMALEON","TORTUGAS","IGUANAS","ARAÑAS"],
          "AVE":["GALLINA","PAVO","GANSO","CODORNIZ"]
          }
    opcion=None
    passive=True
    while(passive):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^14}{}{:^23}|".format(' ','GESTION DE PACIENTES',' '))
        print('+','-'*55,'+')
        print("1. Agregar Paciente.")
        print("2. Buscar Paciente.")
        print("3. Motrar Informacion de un Paciente.")
        print("4. Volver al Menu Principal.")
        opcion=int(input("Digite la Opcion: "))
        if(opcion==1):
            Continue=True
            while(Continue):
                print('+','-'*49,'+')
                print("|{:^16}{}{:^15}|".format(' ','AGREGAR PACIENTE',' '))
                print('+','-'*49,'+')
                Id=core.RandomId(),
                patientName=input("Digite el Nombre del Paciente: ")
                Pause=True
                while(Pause):
                    print("---TIPOS DE ANIMALES---\n-PERRO.\n-GATO.\n-REPTIL.\n-AVE.")    
                    tipo=input("Digite Tipo de Animal del Paciente: ").upper()
                    Stop=True
                    while(animal.get(tipo)):
                        print("---TIPOS DE RAZAS---")
                        for i in animal[tipo]:
                            print(f"-{i}.")
                        raza=input("Digite la Raza del Animal: ").upper()
                        for i in animal[tipo]:
                            if(raza==i):
                                raza=i
                                Pause=False
                            else:
                                print("El Tipo de Raza del Animal no esta en la Lista")
                    while(Stop):
                        print("El Tipo de Animal Seleccionado no esta en la Lista")
                        Stop=False
                    edad=""
                    while(type(edad)==str):
                        try:
                            edad=int(input("Digite la Edad del Paciente: "))
                        except ValueError:
                            print("El Digito no es un Numero Entero")
                    ownerName=input("Digite el Nombre del Propietario: ")
                    patient={
                        "Id":Id,
                        "Nombre-Paciente":patientName,
                        "Tipo-Paciente":tipo,
                        "Raza-Paciente":raza,
                        "Edad-Paciente":edad,        
                    }  
                
                PatientsInfo["Pacientes"].append(patient)
                core.AddInfo("pacientes.json",patient)
                Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar un Camper o Presione Enter para Salir al Menu Principal --> "))
        elif(opcion==2):
            pass
        elif(opcion==3):
            pass
        elif(opcion==4):
            passive=False

#def AddPatient():
    