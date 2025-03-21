#include <iostream>
#include <string>
using namespace std;
#include "atributos.h"
#include "Pantalon.h"

Pantalon::Pantalon(){
    color="n/a";
}
Pantalon::Pantalon(string colorf){
    colorf=color;
}
void Pantalon::set_color(string colorf){
    cout<<"El pantalon es color:"<<endl;
    cin>>colorf;
    color=colorf;
}

string Pantalon::get_color(){
    return color;
}
    void Pantalon::describe(){
        cout<<"-----------------------------"<<endl;
        cout<<">>INVENTARIO ACTUAL DE PANTALON<<"<<endl;
        cout<<"El nombre del PANTALON: "<<nombre<<endl;
        cout<<"El genero del PANTALON: "<<genero<<endl;
        cout<<"El stock delPANTALON: "<<get_invent()<<" piezas"<<endl;
        cout<<"El precio del PANTALON: $"<<get_precio()<<endl;
        cout<<"El descuento del PANTALON: %"<<descuento*100<<endl;
        cout<<"El color del pantalon es:"<<get_color()<<endl;
        cout<<"-----------------------------"<<endl;
    }

