#ifndef PERSONA_H_INCLUDED
#define PERSONA_H_INCLUDED

#include <string>
#include "imprimible.h"
#include <iostream>

using namespace std;
class Persona {
protected:
    string nombre;
    string direccion;
    string fechaNacimiento;

public:
    // Constructor
    Persona();
    Persona(const string& nombre, const string& direccion, const string& fechaNacimiento);

    // M�todos para establecer y obtener la informaci�n de la persona
    void setNombre(const string& nombre);
    string getNombre();
    void setDireccion(const string& direccion);
    string getDireccion();
    void setFechaNacimiento(const string& fechaNacimiento);
    string getFechaNacimiento();

    // M�todo virtual puro para imprimir la informaci�n de la persona
    virtual void imprimirInformacion() = 0;
};

#endif // PERSONA_H_INCLUDED
