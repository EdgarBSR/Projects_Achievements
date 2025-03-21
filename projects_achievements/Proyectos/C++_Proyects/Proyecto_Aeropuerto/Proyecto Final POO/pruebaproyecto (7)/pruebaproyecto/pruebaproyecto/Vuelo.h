#ifndef VUELO_H_INCLUDED
#define VUELO_H_INCLUDED

#include <string>
#include <iostream>
#include "Equipaje.h"


using namespace std;

class Vuelo{
private:
    string numeroVuelo;
    string origen;
    string destino;
    string horaSalida;
    string horaLlegada;
    int asientos;
    Equipaje* equipaje; // Asociación con la clase Equipaje
    string comentario;



public:
    Vuelo();

    void setNumeroVuelo(const string& numero);
    string getNumeroVuelo() const;
    void setOrigen(const string& origen);
    string getOrigen() const;
    void setDestino(const string& destino);
    string getDestino() const;
    void setHoraSalida(const string& hora);
    string getHoraSalida() const;
    void setHoraLlegada(const string& hora);
    string getHoraLlegada() const;
    void setAsientos(int asientos);
    int getAsientos() const;

    // Otros métodos para gestionar la disponibilidad de asientos
    bool hayAsientosDisponibles() const;
    void reservarAsiento();
    void cancelarReserva();
    int obtenerAsientosDisponibles() const;
    bool validarVuelo() const;

    void setEquipaje(Equipaje* equipaje);
    Equipaje* getEquipaje();
    void imprimiInformacion();
    void setComentario(const string& comentario);
    string getComentario() const;


};


#endif // VUELO_H_INCLUDED
