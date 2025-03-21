#ifndef REGISTRODETRIPULACION_H_INCLUDED
#define REGISTRODETRIPULACION_H_INCLUDED
#include "Tripulacion.h"
#include "Aeropuerto.h"

#include "Tripulacion.h"
#include "Aeropuerto.h"
#include <vector>

class RegistroDeTripulacion {
private:
    Aeropuerto* aeropuerto;
    vector<Tripulacion*> tripulacion;

public:
    class AeropuertoNoAsignadoException : public exception {
    public:
        const char* what() const noexcept  {
            return "No se ha asignado un aeropuerto al registro de tripulación.";
        }
    };


    RegistroDeTripulacion();
    //~RegistroDeTripulacion();

    void setAeropuerto(Aeropuerto* aeropuerto);
    Aeropuerto* getAeropuerto() const;
    void agregarTripulacion(Tripulacion* tripulacion);
    vector<Tripulacion*> getTripulacion() const;
};


#endif // REGISTRODETRIPULACION_H_INCLUDED
