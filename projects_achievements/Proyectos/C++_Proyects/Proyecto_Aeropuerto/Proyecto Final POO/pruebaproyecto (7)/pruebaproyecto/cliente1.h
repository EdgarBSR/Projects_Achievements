#ifndef CLIENTE1_H_INCLUDED
#define CLIENTE1_H_INCLUDED

#include "Persona.h"
#include <iostream>
#include <string>
using namespace std;

class Cliente: virtual public Persona {
    // Implementación de los atributos y métodos de Cliente...
private:
    string folio;
    string fechaActual;

public:
    Cliente();
    Cliente(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& folio_r, const string& fechaActual_r);
    void set_folio(const string& folio_r);
    void set_fechaActual(const string& fechaActual_r);
    void imprimirInformacion() override;
    string getFolio();
    string getFechaActual();
};


#endif // CLIENTE1_H_INCLUDED
