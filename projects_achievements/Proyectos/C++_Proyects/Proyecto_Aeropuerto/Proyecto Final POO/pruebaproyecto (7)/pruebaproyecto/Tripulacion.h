#ifndef TRIPULACION_H_INCLUDED
#define TRIPULACION_H_INCLUDED

#include "Persona.h"

using namespace std;
class Tripulacion : public Persona {
private:
    string ID;
    string puesto;

public:
    // M�todos para establecer y obtener la informaci�n de la tripulaci�n
    void setID(const string& ID);
    string getID() const;
    void setPuesto(const string& puesto);
    string getPuesto() const;

    void imprimirInformacion() override;
};


#endif // TRIPULACION_H_INCLUDED
