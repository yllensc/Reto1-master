import os
import pacientes
import veterinarios
import citasMedicas
Activate=True
opcion=None
if __name__ == "__main__":
    DataPatients={"Pacientes":[]}
    DataVets={"Veterinarios":[]}
    DataMedicalAppointments={"Citas-Medicas":[]}
    while(Activate):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^8}{}{:^13}|".format(' ','ADMINISTRACON DEL CENTRO VETERINARIO',' '))
        print('+','-'*55,'+')
        print("1. Gestion de Pacientes.")
        print("2. Gestion de Veterinarios.")
        print("3. Gestion de Citas Medicas.")
        print("4. Salir.")
        opcion=int(input("Digite la Opcion: "))
        if(opcion==1):
            pacientes.PatientsMenu()
        elif(opcion==2):
            veterinarios.VetMenu()
        elif(opcion==3):
            citasMedicas.MedicalAppointments()
        elif(opcion==4):
            print("CERRANDO PROGRAMA")
            input("Presione una tecla para continuar...")
            Activate=False
