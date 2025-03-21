#include "Empleado.h"

Empleado::Empleado(){
    ID="";
    puesto="";

}

Empleado::Empleado(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& ID_a, const string& puesto_a):Persona(nombre_r,direccion_r,fechaNacimiento_r), ID(ID_a), puesto(puesto_a)
{
    this->ID=ID_a;
    this->puesto=puesto_a;
}

void Empleado::set_ID(const string& ID_a){
    this->ID=ID_a;

}

string Empleado::getIDEmpleado(){
    return ID;

}
void Empleado::set_puesto(const string& puesta_a){
    this->puesto=puesta_a;

}

string Empleado::getpuesto(){
    return puesto;

}

void Empleado::imprimirInformacion(){
    Persona::imprimirInformacion();
    cout<<"El nombre del empleado: "<<getIDEmpleado()<<endl;
    cout<<"La fecha actual: "<<getpuesto()<<endl;

}
