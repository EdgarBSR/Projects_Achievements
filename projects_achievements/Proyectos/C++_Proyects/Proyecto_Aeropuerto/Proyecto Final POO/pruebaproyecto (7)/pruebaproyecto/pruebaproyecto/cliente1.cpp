
#include "cliente1.h"


Cliente::Cliente(){
    folio="";
    fechaActual="";
}

Cliente::Cliente(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& folio_r, const string& fechaActual_r):Persona(nombre_r,direccion_r,fechaNacimiento_r),folio(folio_r), fechaActual(fechaActual_r)
{
    this->folio=folio_r;
    this->fechaActual=fechaActual_r;
}


void Cliente::set_folio(const string& folio_r){
    this->folio=folio_r;

}

string Cliente::getFolio(){
    return folio;

}
void Cliente::set_fechaActual(const string& fechaActual_r){
    this->fechaActual=fechaActual_r;

}

string Cliente::getFechaActual(){
    return fechaActual;

}

void Cliente::imprimirInformacion(){
    Persona::imprimirInformacion();
    cout<<"El folio es: "<<getFolio()<<endl;
    cout<<"La fecha actual: "<<getFechaActual()<<endl;

}

