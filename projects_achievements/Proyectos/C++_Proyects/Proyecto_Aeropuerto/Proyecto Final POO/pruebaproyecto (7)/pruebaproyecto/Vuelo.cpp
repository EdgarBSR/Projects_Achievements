#include "Vuelo.h"
using namespace std;


Vuelo::Vuelo()
{
    numeroVuelo="";
    origen="";
    destino="";
    horaSalida="";
    horaLlegada="";
    asientos=0 ;
    equipaje=nullptr;
    comentario = "";
}

void Vuelo::setNumeroVuelo(const string& numero) {
    numeroVuelo = numero;
}

string Vuelo::getNumeroVuelo() const {
    return numeroVuelo;
}

void Vuelo::setOrigen(const string& origen) {
    this->origen = origen;
}

string Vuelo::getOrigen() const {
    return origen;
}

void Vuelo::setDestino(const string& destino) {
    this->destino = destino;
}

string Vuelo::getDestino() const {
    return destino;
}

void Vuelo::setHoraSalida(const string& hora) {
    horaSalida = hora;
}

string Vuelo::getHoraSalida() const {
    return horaSalida;
}

void Vuelo::setHoraLlegada(const string& hora) {
    horaLlegada = hora;
}

string Vuelo::getHoraLlegada() const {
    return horaLlegada;
}

void Vuelo::setAsientos(int asientos) {
    this->asientos = asientos;
}

int Vuelo::getAsientos() const {
    return asientos;
}

bool Vuelo::hayAsientosDisponibles() const {
    return asientos > 0;
}

void Vuelo::reservarAsiento() {
    if (asientos > 0) {
        asientos--;
        cout << "Asiento reservado. Asientos restantes: " << asientos << endl;
    } else {
        cout << "No hay asientos disponibles." << endl;
    }
}
void Vuelo::cancelarReserva() {
    asientos++;
    cout << "Reserva cancelada. Asientos disponibles: " << asientos << endl;
}

    int Vuelo::obtenerAsientosDisponibles() const {
        return asientos;
}

    bool Vuelo::validarVuelo() const {
        return !numeroVuelo.empty() && !origen.empty() && !destino.empty() && !horaSalida.empty() && !horaLlegada.empty() && asientos > 0;
}

void Vuelo::setEquipaje(Equipaje* equipaje) {
    this->equipaje = equipaje;
}

Equipaje* Vuelo::getEquipaje() {
    return equipaje;
}

void Vuelo::setComentario(const string& comentario) {
    this->comentario = comentario;
}

std::string Vuelo::getComentario() const {
    return comentario;
}


void Vuelo::imprimiInformacion()
{
    cout << "Numero de Vuelo: " << numeroVuelo << endl;
    cout << "Origen: " << origen << endl;
    cout << "Destino: " << destino << endl;
    cout << "Hora de Salida: " << horaSalida << endl;
    cout << "Hora de Llegada: " << horaLlegada << endl;
    cout << "Asientos disponibles: " << asientos << endl;
    if (equipaje != nullptr) {
        cout << "Informacion del Equipaje:" << endl;
        equipaje->imprimirInformacion();
    }
     cout << "Comentario: " << comentario << endl;
}


