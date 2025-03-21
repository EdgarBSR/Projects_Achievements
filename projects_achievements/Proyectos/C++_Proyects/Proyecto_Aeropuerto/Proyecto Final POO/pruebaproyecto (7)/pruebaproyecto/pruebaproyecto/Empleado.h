#ifndef EMPLEADO_H_INCLUDED
#define EMPLEADO_H_INCLUDED

#include "Persona.h"

class Empleado : virtual public Persona {
    // Implementación de los atributos y métodos de Empleado...

private:
    string ID;
    string puesto;

public:
    Empleado();
    Empleado(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& ID_a, const string& puesto_a );
    void set_ID(const string& ID_a);
    void set_puesto(const string& puesto_a);
    void imprimirInformacion();
    string getIDEmpleado();
    string getpuesto();

};

#endif // EMPLEADO_H_INCLUDED
