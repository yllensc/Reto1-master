import os
import json
import core
MedicalInfo= {"Citas-Medicas":[]}
def LoadInfoMedical():
    global MedicalInfo
    if (core.CheckFile("citasmedicas.json")):
        infoCitasMedicas = core.LoadInfo("citasmedicas.json")
    else:
        core.AddInfo("citasmedicas.json",infoCitasMedicas)
def MedicalAppointments():
    opcion=None
    passive=True
    while(passive):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^14}{}{:^19}|".format(' ','GESTION DE CITAS MEDICAS',' '))
        print('+','-'*55,'+')
        print("1. Crear Cita.")
        print("2. Cancelar Cita.")
        print("3. Consultar Cita por Fecha.")
        print("4. Consultar Citas por Veterinario.")
        print("5. Volver al Menu Principal.")
        opcion=int(input("Digite la Opcion: "))
        if(opcion==1):
            pass
        elif(opcion==2):
            pass
        elif(opcion==3):
            pass
        elif(opcion==4):
            pass
        elif(opcion==5):
            passive=False

