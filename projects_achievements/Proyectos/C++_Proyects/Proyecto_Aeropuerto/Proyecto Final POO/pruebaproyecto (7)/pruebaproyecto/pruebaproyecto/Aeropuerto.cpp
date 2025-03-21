#include "Aeropuerto.h"

Aeropuerto::Aeropuerto() {}

void Aeropuerto::setCodigoAeropuerto(const string& codigo) {
    codigoAeropuerto = codigo;
}

string Aeropuerto::getCodigoAeropuerto() const {
    return codigoAeropuerto;
}

void Aeropuerto::setNombre(const string& nombre) {
    this->nombre = nombre;
}

string Aeropuerto::getNombre() const {
    return nombre;
}

void Aeropuerto::setCiudad(const string& ciudad) {
    this->ciudad = ciudad;
}

string Aeropuerto::getCiudad() const {
    return ciudad;
}

void Aeropuerto::setPais(const string& pais) {
    this->pais = pais;
}

string Aeropuerto::getPais() const {
    return pais;
}

void Aeropuerto::imprimirINformacion()
{
    cout<<"El codigo del aeropuerto es: "<<getCodigoAeropuerto()<<endl;
    cout<<"El nombre del aeropuerto es: "<<getNombre()<<endl;
    cout<<"La ciudad es: "<<getCiudad()<<endl;
    cout<<"El pais es: "<<getPais()<<endl;

}
