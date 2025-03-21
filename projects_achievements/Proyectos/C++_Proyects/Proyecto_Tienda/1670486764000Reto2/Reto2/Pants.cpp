#include <iostream>
#include <string>

#include "Pants.h"
#include "atributos.h"

using namespace std;

Pants::Pants(){
}
    void Pants::describe(){
        cout<<"-----------------------------"<<endl;
        cout<<">>INVENTARIO ACTUAL DE PANTS<<"<<endl;
        cout<<"El nombre del PANTS: "<<nombre<<endl;
        cout<<"El genero del PANTS: "<<genero<<endl;
        cout<<"El stock del PANTS: "<<get_invent()<<" piezas"<<endl;
        cout<<"El precio del PANTS: $"<<get_precio()<<endl;
        cout<<"El descuento del PANTS: %"<<descuento*100<<endl;
        cout<<"-----------------------------"<<endl;
    }

