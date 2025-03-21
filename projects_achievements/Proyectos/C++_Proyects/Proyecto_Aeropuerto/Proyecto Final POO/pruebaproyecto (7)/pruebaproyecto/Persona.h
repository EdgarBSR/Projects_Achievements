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

    // Métodos para establecer y obtener la información de la persona
    void setNombre(const string& nombre);
    string getNombre();
    void setDireccion(const string& direccion);
    string getDireccion();
    void setFechaNacimiento(const string& fechaNacimiento);
    string getFechaNacimiento();

    // Método virtual puro para imprimir la información de la persona
    virtual void imprimirInformacion() = 0;
};

#endif // PERSONA_H_INCLUDED
