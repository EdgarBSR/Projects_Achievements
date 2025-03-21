#include <iostream>
#include "Pants.h"
#include "Pantalon.h"
#include "opcion1.h"
using namespace std;



int menu(void)
{

cout<<"\n****************************TIENDA VIRTUAL****************************"<<endl;
cout<<"\n1. Crear cliente nuevo."<<endl;
cout<<"\n2. Crear inventario."<<endl;
cout<<"\n3. Checar inventario y vender."<<endl;
cout<<"\n4. Salir."<<endl;
cout<<"\nIngrese su opcion: "<<endl;
}
int main (){
int opcion, opc2, inventario,i=1;
string nombre,genero,name,color;
int stock,buy;
float desc,price;

registro cliente;
Pantalon rustico;
Pants moderno;

while(opc2 == 2);{

    while(i==1){



    menu();
    cin>>opcion;

    if(opcion==1)
    {
        cout<<"Ingrese nombre del cliente:"<<endl;
        cin>>name;
        cliente.setNombre(name);
        cliente.mostrarN();
        menu();
        cin>>opcion;
    }
    if(opcion==2){
            cout<<"Desea crear de pants o pantalon?"<<endl;
            cout<<"\n1. Inventario de pants."<<endl;
            cout<<"\n2. Inventario de pantalon."<<endl;
            cin>>inventario;
            if(inventario==1){
                cout<<"\nBienvenido a la creacion del inventario de Pants--"<<endl;
                moderno.set_Nombre(nombre);
                moderno.set_Genero(genero);
                moderno.set_invent(stock);
                moderno.set_precio(price);
                moderno.set_descuento(price);
            menu();
            cin>>opcion;
            }

            else if(inventario==2){
                cout<<"\nBienvenido a la creacion del inventario de Pantalon--"<<endl;
                rustico.set_Nombre(nombre);
                rustico.set_Genero(genero);
                rustico.set_invent(stock);
                rustico.set_precio(price);
                rustico.set_descuento(price);
                rustico.set_color(color);
            menu();
            cin>>opcion;

        }

        }
    if(opcion==3){
            cout<<"\Bienvenido al inventario---"<<endl;
            cout<<"\n1. Inventario de pants."<<endl;
            cout<<"\n2. Inventario de pantalon."<<endl;
            cin>>inventario;
            if(inventario==1){
                moderno.describe();
                moderno.restarinvent();
                moderno.ticket();
                menu();
                cin>>opcion;
            }
            else if(inventario==2){
                rustico.describe();
                rustico.restarinvent();
                rustico.ticket();
                menu();
                cin>>opcion;
            }
    }
    if(opcion==4){
        cout<<"Muchas gracias por visitarnos, vuelva pronto"<<endl;
        break;


    }


    }
    }

}
