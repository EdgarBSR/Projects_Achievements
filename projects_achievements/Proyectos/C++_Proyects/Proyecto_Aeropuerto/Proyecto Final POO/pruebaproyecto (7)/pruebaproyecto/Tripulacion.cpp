#include "Tripulacion.h"
#include <iostream>

void Tripulacion::setID(const string& ID) {
    this->ID = ID;
}

string Tripulacion::getID() const {
    return ID;
}

void Tripulacion::setPuesto(const string& puesto) {
    this->puesto = puesto;
}

string Tripulacion::getPuesto() const {
    return puesto;
}

void Tripulacion::imprimirInformacion() {
    //std::cout << "Nombre: " << getNombre() const << std::endl;
    cout << "ID: " << getID() << endl;
    cout << "Puesto: " << getPuesto() << endl;
}
