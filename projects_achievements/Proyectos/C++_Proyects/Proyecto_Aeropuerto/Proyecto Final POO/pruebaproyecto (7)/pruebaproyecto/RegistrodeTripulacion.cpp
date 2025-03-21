#include "RegistroDeTripulacion.h"

RegistroDeTripulacion::RegistroDeTripulacion() : aeropuerto(nullptr) {}
/*
RegistroDeTripulacion::~RegistroDeTripulacion() {
    delete aeropuerto;
    for (Tripulacion* trip : tripulacion) {
        delete trip;
    }
}
*/

void RegistroDeTripulacion::agregarTripulacion(Tripulacion* tripulacion) {
    if (!aeropuerto) {
        throw AeropuertoNoAsignadoException();
    }
    this->tripulacion.push_back(tripulacion);
}


void RegistroDeTripulacion::setAeropuerto(Aeropuerto* aeropuerto) {
    this->aeropuerto = aeropuerto;
}

Aeropuerto* RegistroDeTripulacion::getAeropuerto() const {
    return aeropuerto;
}


vector<Tripulacion*> RegistroDeTripulacion::getTripulacion() const {
    return tripulacion;
}
