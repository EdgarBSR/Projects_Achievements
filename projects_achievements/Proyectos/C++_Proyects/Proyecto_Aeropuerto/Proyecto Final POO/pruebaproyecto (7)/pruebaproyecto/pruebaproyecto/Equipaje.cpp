#include "Equipaje.h"

Equipaje::Equipaje()
{
     peso=0;
     costoAdicional=0;
     seguimiento="";
}


void Equipaje::setPeso(int peso) {
    if (peso < 8) {
        throw PesoInvalidoException();
    }
    this->peso = peso;
}



Equipaje::Equipaje(int peso, int costoAdicional, const string& seguimiento)
    : peso(peso), costoAdicional(costoAdicional), seguimiento(seguimiento){}

int Equipaje::getPeso() const {
    return peso;
}

void Equipaje::setCostoAdicional(int costo) {
    costoAdicional = costo;
}

int Equipaje::getCostoAdicional() const {
    return costoAdicional;
}

void Equipaje::setSeguimiento(const std::string& seguimiento) {
    this->seguimiento = seguimiento;
}

std::string Equipaje::getSeguimiento() const {
    return seguimiento;
}




void Equipaje::imprimirInformacion()
{
    std::cout << "Peso: " << peso << " kg" << std::endl;
    std::cout << "Costo Adicional: $" << costoAdicional << std::endl;
    std::cout << "Numero de Seguimiento: " << seguimiento << std::endl;
}
