#include "Persona.h"
using namespace std;
Persona::Persona()
{
    nombre="";
    direccion="";
    fechaNacimiento="";
}


Persona::Persona(const string& nombre, const string& direccion, const string& fechaNacimiento){

    this->nombre=nombre;
    this->direccion=direccion;
    this->fechaNacimiento=fechaNacimiento;

}

void Persona::setNombre(const string& nombre) {
    this->nombre = nombre;
}

string Persona::getNombre(){
    return nombre;
}

void Persona::setDireccion(const string& direccion) {
    this->direccion = direccion;
}

string Persona::getDireccion(){
    return direccion;
}

void Persona::setFechaNacimiento(const string& fechaNacimiento) {
    this->fechaNacimiento = fechaNacimiento;
}

string Persona::getFechaNacimiento(){
    return fechaNacimiento;
}


 void Persona::imprimirInformacion() {

    cout<<"EL nombre es: "<< getNombre()<<endl;
    cout<<"La direccion es: "<< getDireccion()<<endl;
    cout<<"Fecha de nacimiento: "<< getFechaNacimiento()<<endl;

}



