#ifndef OPCION1_H_INCLUDED
#define OPCION1_H_INCLUDED
using namespace std;

class registro{
    private:
    string nombre_cliente;
    public:
        registro();
        registro(string);//Constructor
        ~registro();

        void setNombre(string);
        string getNombre();
        void mostrarN();


};


#endif // OPCION1_H_INCLUDED
