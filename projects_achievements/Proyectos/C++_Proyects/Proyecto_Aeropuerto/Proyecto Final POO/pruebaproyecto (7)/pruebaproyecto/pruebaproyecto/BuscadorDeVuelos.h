#ifndef BUSCADORDEVUELOS_H_INCLUDED
#define BUSCADORDEVUELOS_H_INCLUDED

#include <vector>
#include <string>
#include "Vuelo.h"

class BuscadorDeVuelos : public Vuelo {

public:
    std::vector<Vuelo> buscarVuelos(const string& origen, const string& destino);
};

#endif // BUSCADORDEVUELOS_H_INCLUDED
