#ifndef AEROPUERTO_H_INCLUDED
#define AEROPUERTO_H_INCLUDED

#include <string>
#include <iostream>

using namespace std;
class Aeropuerto {
private:
    string codigoAeropuerto;
    string nombre;
    string ciudad;
    string pais;

public:
    // Constructor
    Aeropuerto();

    // M�todos para establecer y obtener la informaci�n del aeropuerto
    void setCodigoAeropuerto(const string& codigo);
    string getCodigoAeropuerto() const;
    void setNombre(const string& nombre);
    string getNombre() const;
    void setCiudad(const string& ciudad);
    string getCiudad() const;
    void setPais(const string& pais);
    string getPais() const;
    void imprimirINformacion();
    // Otros m�todos relevantes para la clase Aeropuerto
};


#endif // AEROPUERTO_H_INCLUDED
