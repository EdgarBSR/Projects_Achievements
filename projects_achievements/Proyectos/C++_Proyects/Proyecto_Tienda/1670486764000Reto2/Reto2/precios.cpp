#include <iostream>
#include "precios.h"


Precios::Precios(){
    precio= 0.0;
    descuento= 0.0;

}
Precios::Precios(float price){
    price=precio;
}
void Precios::set_precio(float price){
    cout<<"Ingresa el precio de la prenda: "<<endl;
    cin>>price;
    precio=price;
}
void Precios::set_descuento(float desc){
    cout<<"Determine el descuento del para la prenda en entero:"<<endl;
    cin>>desc;
    descuento=desc/100;
}
float Precios::get_precio(){
    return precio;
}
float Precios::subt(){
    precio=precio*descuento;
    return precio;
}
