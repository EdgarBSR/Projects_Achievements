#include <iostream>
#include <string>
using namespace std;
#include "atributos.h"



Atributos::Atributos(){
    nombre="n/a";
    genero="n/a";
    invent=0;
    compra=0;
}
Atributos::Atributos(string name, string gender, int stock,int buy){
    name=nombre;
    genero=gender;
    invent=stock;
}
void Atributos::set_Nombre(string name){
    cout<<"Inserte nombre de la marca:"<<endl;
    cin>>name;
    nombre=name;
}
void Atributos::set_Genero(string gender){
    cout<<"Inserte el genero:"<<endl;
    cin>>gender;
    genero=gender;
}
void Atributos::set_invent(int stock){
    cout<<"Ingresa inventario de la ropa:"<<endl;
    cin>>stock;
    invent=stock;
}
int Atributos::get_invent(){
    return invent;
}
void Atributos::restarinvent(){
    cout<<"\nNumero de prendas a comprar:"<<endl;
    cin>>compra;
    invent=invent-compra;
}
void Atributos::ticket(){
    cout<<"\n============================="<<endl;
        cout<<"------TICKET DE COMPRA-------"<<endl;
        cout<<"============================="<<endl;
        cout<<"Articulo:---------- "<<nombre<<endl;
        cout<<"Cantidad:---------- "<<compra<<" piezas"<<endl;
        cout<<"Descuento:--------- %"<<descuento*100<<endl;
        cout<<"Total:------------- $"<<get_precio()*compra-(subt()*compra)<<endl;
        cout<<"============================="<<endl;
        }
