#ifndef EQUIPAJE_H_INCLUDED
#define EQUIPAJE_H_INCLUDED
#include <string>
#include <iostream>
using namespace std;

class Equipaje{
private:
    int peso;
    int costoAdicional;
    string seguimiento;


public:
    class PesoInvalidoException : public std::exception {
    public:
        const char* what() const noexcept override {
            return "El peso del equipaje es inválido.";
        }
    };

    Equipaje();
    Equipaje(int peso, int costoAdicional, const string& seguimiento);

    void setPeso(int peso);
    int getPeso() const;
    void setCostoAdicional(int costo);
    int getCostoAdicional() const;
    void setSeguimiento(const string& seguimiento);
    string getSeguimiento() const;

    void imprimirInformacion();
};

#endif // EQUIPAJE_H_INCLUDED
