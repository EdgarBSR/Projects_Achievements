#include "BuscadorDeVuelos.h"

using namespace std;

std::vector<Vuelo* > BuscadorDeVuelos::buscarVuelos(const std::string& origen, const std::string& destino) {
    // Ejemplo de vuelos disponibles

    std::vector<Vuelo> vuelosDisponibles = {
        { "Ciudad A", "Ciudad B", "Aerolínea 1", 200.0 },
        { "Ciudad A", "Ciudad C", "Aerolínea 2", 150.0 },
        { "Ciudad B", "Ciudad C", "Aerolínea 3", 180.0 },
        { "Ciudad C", "Ciudad A", "Aerolínea 1", 220.0 },
        { "Ciudad B", "Ciudad D", "Aerolínea 2", 300.0 },
        // Agrega más ejemplos de vuelos según sea necesario
    }

    // Filtrar los vuelos que coinciden con los criterios de búsqueda
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
