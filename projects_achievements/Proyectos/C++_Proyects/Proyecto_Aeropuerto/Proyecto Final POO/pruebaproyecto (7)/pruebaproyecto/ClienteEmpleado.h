#ifndef CLIENTEEMPLEADO_H_INCLUDED
#define CLIENTEEMPLEADO_H_INCLUDED

#include "Empleado.h"
#include "cliente1.h"
#include <iostream>
#include <string>

using namespace std;
class ClienteEmpleado : public Empleado,public Cliente {
    // Implementación de los atributos y métodos de ClienteEmpleado...
private:
    string folioCE;



public:
    ClienteEmpleado();
    ClienteEmpleado(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& folio_r, const string& fechaActual_r,  const string& ID_a, const string& puesto_a , const string& folioCE_r);
    string getFolioce();
    void set_folioCE(const string& folioCE_r);
    void imprimirInformacion() override;
};


#endif // CLIENTEEMPLEADO_H_INCLUDED
