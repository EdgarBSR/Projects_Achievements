#include <iostream>
#include "opcion1.h"
//constructor
using namespace std;
registro::registro(){
    nombre_cliente= "n/a";


}
registro::registro(string nombrecliente){
    nombre_cliente=nombrecliente;

}
registro::~registro(){

}

string registro::getNombre(){
    return nombre_cliente;
}


void registro::setNombre(string nombrecliente){
    nombre_cliente=nombrecliente;

}
void registro::mostrarN(){
    cout<<nombre_cliente<<endl;
}


