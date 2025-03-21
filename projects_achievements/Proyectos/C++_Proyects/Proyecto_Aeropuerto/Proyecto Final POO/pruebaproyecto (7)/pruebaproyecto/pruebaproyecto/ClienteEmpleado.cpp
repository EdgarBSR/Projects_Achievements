#include "ClienteEmpleado.h"

ClienteEmpleado::ClienteEmpleado(){
    folioCE="";


}
/*
ClienteEmpleado::ClienteEmpleado(string nombre_r, string direccion_r, string fechaNacimiento_r, const string& folio_r, const string& fechaActual_r,  const string& ID_a, const string& puesto_a , const string& folioCE_r ):Persona(nombre_r,direccion_r,fechaNacimiento_r),Cliente(folio_r, fechaActual_r),Empleado(ID_a, puesto_a)
{
    this->folioCE=folioCE_r;
}
*/
void ClienteEmpleado::set_folioCE(const string& folioCE_r)
{
    this->folioCE=folioCE_r;
}
string ClienteEmpleado::getFolioce(){
    return folioCE;

}

void ClienteEmpleado::imprimirInformacion() {
    // Implementación para imprimir la información del ClienteEmpleado
    Persona::imprimirInformacion();
    Cliente::imprimirInformacion();
    Empleado::imprimirInformacion();
    cout<<"El folio es: "<<getFolioce()<<endl;


}
