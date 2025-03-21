#ifndef PRECIOS_H_INCLUDED
#define PRECIOS_H_INCLUDED
using namespace std;


class Precios {
    private:
        float precio;


    public:

        float descuento;
        Precios();
        Precios(float);
        float subt();
        void set_precio(float);
        void set_descuento(float);
        float get_precio();

};
#endif // PRECIOS_H_INCLUDED
