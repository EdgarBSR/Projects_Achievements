#include "BuscadorDeVuelos.h"

using namespace std;

std::vector<Vuelo* > BuscadorDeVuelos::buscarVuelos(const std::string& origen, const std::string& destino) {
    // Ejemplo de vuelos disponibles

    std::vector<Vuelo> vuelosDisponibles = {
        { "Ciudad A", "Ciudad B", "Aerol�nea 1", 200.0 },
        { "Ciudad A", "Ciudad C", "Aerol�nea 2", 150.0 },
        { "Ciudad B", "Ciudad C", "Aerol�nea 3", 180.0 },
        { "Ciudad C", "Ciudad A", "Aerol�nea 1", 220.0 },
        { "Ciudad B", "Ciudad D", "Aerol�nea 2", 300.0 },
        // Agrega m�s ejemplos de vuelos seg�n sea necesario
    }

    // Filtrar los vuelos que coinciden con los criterios de b�squeda
    std::vector<Vuelo> vuelosCoincidentes;
    for (const auto& vuelo : vuelosDisponibles) {
        if (vuelo.origen ==  && vuelo.destino == destino) {
            vuelosCoincidentes.push_back(vuelo);
        }
    }

    return vuelosCoincidentes;
}
*/
}
