#ifndef PANTALON_H_INCLUDED
#define PANTALON_H_INCLUDED

#include "atributos.h"

class Pantalon: public Atributos {
    public:
        Pantalon();
        Pantalon(string);

        void set_color(string);
        string get_color();
        void describe();
    private:
        string color;

};

#endif // PANTALON_H_INCLUDED
