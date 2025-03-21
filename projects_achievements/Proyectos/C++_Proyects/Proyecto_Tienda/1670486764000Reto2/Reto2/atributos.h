#ifndef ATRIBUTOS_H_INCLUDED
#define ATRIBUTOS_H_INCLUDED
using namespace std;
#include <iostream>
#include <string>
#include "precios.h"






class Atributos: public Precios{
    private:
    int invent;

    public:
    Atributos();
    Atributos(string,string,int,int);

    string nombre;
    string genero;
    int compra;

    void set_Nombre(string);
    void set_Genero(string);
    void set_invent(int);
    void restarinvent();
    void ticket();

    int get_invent();

};


#endif // ATRIBUTOS_H_INCLUDED
