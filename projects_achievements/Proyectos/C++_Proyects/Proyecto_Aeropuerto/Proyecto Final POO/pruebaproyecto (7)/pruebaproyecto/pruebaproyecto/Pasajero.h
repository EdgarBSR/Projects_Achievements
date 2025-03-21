#ifndef PASAJERO_H_INCLUDED
#define PASAJERO_H_INCLUDED

#include "Persona.h"
#include "imprimible.h"
#include <string>
#include "Equipaje.h"


using namespace std;
class Pasajero : public Persona,Imprimible {
private:
    string ID;
    string email;
    Equipaje* equipaje; // Asociación con la clase Equipaje
    std::string resena;

public:
    // Métodos para establecer y obtener la información del pasajero
    Pasajero();
    Pasajero(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& ID, const string& email);
    void setID(const string& ID);
    string getID();
    void setEmail(const string& email);
    string getEmail();


    void imprimirInformacion() override;
    void setResena(const std::string& resena);
    std::string getResena() const;

    void setEquipaje(Equipaje* equipaje);
    Equipaje* getEquipaje();

};


#endif // PASAJERO_H_INCLUDED
