#ifndef RESERVA_H_INCLUDED
#define RESERVA_H_INCLUDED

#include <string>
#include "Vuelo.h"
#include "Pasajero.h"

using namespace std;
class Reserva: virtual public Persona{
private:
    string IDReserva;
    Vuelo* vuelo;
    Pasajero* pasajero;
    string fechaReserva;
    string estatus;

public:
    // Constructor
    Reserva();

    // Métodos para establecer y obtener la información de la reserva
    void setIDReserva(const string& ID);
    string getIDReserva() const;
    void setVuelo(Vuelo* vuelo);
    Vuelo* getVuelo() const;
    void setPasajero(Pasajero* pasajero);
    Pasajero* getPasajero() const;
    void setFechaReserva(const string& fecha);
    string getFechaReserva() const;
    void setEstatus(const string& estatus);
    string getEstatus() const;
    void reservarVuelo(Vuelo* vuelo, Pasajero* pasajero);
    void cancelarReserva();
    void cambiarVuelo(Vuelo* nuevoVuelo);
    bool validarReserva() const;
    void imprimirInformacion() override;
};

#endif // RESERVA_H_INCLUDED
