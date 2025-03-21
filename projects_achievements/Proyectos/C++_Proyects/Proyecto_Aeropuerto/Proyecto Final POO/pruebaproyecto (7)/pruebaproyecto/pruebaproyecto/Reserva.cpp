#include "Reserva.h"

Reserva::Reserva() {}

void Reserva::setIDReserva(const string& ID) {
    IDReserva = ID;
}

string Reserva::getIDReserva() const {
    return IDReserva;
}

void Reserva::setVuelo(Vuelo* vuelo) {
    this->vuelo = vuelo;
}

Vuelo* Reserva::getVuelo() const {
    return vuelo;
}

void Reserva::setPasajero(Pasajero* pasajero) {
    this->pasajero = pasajero;
}

Pasajero* Reserva::getPasajero() const {
    return pasajero;
}

void Reserva::setFechaReserva(const string& fecha) {
    fechaReserva = fecha;
}

string Reserva::getFechaReserva() const {
    return fechaReserva;
}

void Reserva::setEstatus(const string& estatus) {
    this->estatus = estatus;
}

string Reserva::getEstatus() const {
    return estatus;
}

void Reserva::reservarVuelo(Vuelo* vuelo, Pasajero* pasajero) {
    if (vuelo->obtenerAsientosDisponibles() > 0) {
        vuelo->reservarAsiento();
        this->vuelo = vuelo;
        this->pasajero = pasajero;
    } else {
        throw std::runtime_error("No hay asientos disponibles en el vuelo seleccionado.");
    }
}
// Método para cancelar una reserva existente
void Reserva::cancelarReserva() {
    if (vuelo != nullptr) {
        vuelo->cancelarReserva();
        vuelo = nullptr;
        pasajero = nullptr;
    } else {
        throw std::runtime_error("No hay reserva existente para cancelar.");
    }
}
void Reserva::cambiarVuelo(Vuelo* nuevoVuelo) {
    if (vuelo != nullptr && nuevoVuelo->obtenerAsientosDisponibles() > 0) {
        vuelo->cancelarReserva();
        vuelo = nuevoVuelo;
        vuelo->reservarAsiento();
    } else {
        throw std::runtime_error("No se puede cambiar la reserva a un vuelo inválido o sin asientos disponibles.");
    }
}

// Método para validar una reserva
bool Reserva::validarReserva() const {
    return vuelo != nullptr && pasajero != nullptr;
}

void Reserva::imprimirInformacion()
{

    cout << "Informacion del vuelo:" << endl;
    cout << "Numero de vuelo: " << vuelo->getNumeroVuelo() << endl;
    cout << "Origen: " << vuelo->getOrigen() << endl;
    cout << "Destino: " << vuelo->getDestino() << endl;
    cout << "Hora de salida: " << vuelo->getHoraSalida() << endl;
    cout << "Hora de llegada: " << vuelo->getHoraLlegada() << endl;
    cout << "Asientos disponibles: " << vuelo->getAsientos() <<endl;
    cout << "Asientos disponibles: " << vuelo->getAsientos()-1 << endl;
    cout << "Informacion de la reserva" << endl;
    cout << "ID de reserva: " << getIDReserva() << endl;
    cout << "Fecha de reserva: " << getFechaReserva() << endl;
    cout << "Estatus: " <<getEstatus() << endl;
}
