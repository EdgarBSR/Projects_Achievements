#ifndef TRIPULACION_H_INCLUDED
#define TRIPULACION_H_INCLUDED

#include "Persona.h"

using namespace std;
class Tripulacion : public Persona {
private:
    string ID;
    string puesto;

public:
    // Métodos para establecer y obtener la información de la tripulación
    void setID(const string& ID);
    string getID() const;
    void setPuesto(const string& puesto);
    string getPuesto() const;

    void imprimirInformacion() override;
};


#endif // TRIPULACION_H_INCLUDED
