#include "Pasajero.h"
#include <iostream>

Pasajero::Pasajero(){
    ID="";
    email="";
    equipaje=nullptr;
    resena = "";

}

Pasajero::Pasajero(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& ID, const string& email):Persona(nombre_r, direccion_r, fechaNacimiento_r),ID(ID), email(email)
{
    this->ID = ID;
    this->email = email;
    resena = "";

}
void Pasajero::setID(const string& ID) {
    this->ID = ID;
}

string Pasajero::getID() {
    return ID;
}

void Pasajero::setEmail(const string& email) {
    this->email = email;
}

string Pasajero::getEmail(){
    return email;
}

void Pasajero::setEquipaje(Equipaje* equipaje) {
    this->equipaje = equipaje;
}

Equipaje* Pasajero::getEquipaje(){
    return equipaje;
}

void Pasajero::setResena(const string& resena) {
    this->resena = resena;
}

string Pasajero::getResena() const {
    return resena;
}


void Pasajero::imprimirInformacion() {
    cout<<"EL nombre es: "<< nombre<<endl;
    cout<<"La direccion es: "<< direccion<<endl;
    cout<<"Fecha de nacimiento: "<< fechaNacimiento<<endl;
    cout << "ID: " << getID() << endl;
    cout << "Email: " << getEmail() << endl;
    if (equipaje != nullptr) {
        cout << "Informacion del Equipaje:" << endl;
        equipaje->imprimirInformacion();
    }
    cout << "Resena: " << resena << endl;

    }





