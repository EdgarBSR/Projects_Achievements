#include "SistemaComentarios.h"

void SistemaComentarios::agregarComentarioVuelo(const std::string& comentario) {
    if (comentario.empty()) {
        throw ComentarioVacioException();
    }
    comentariosVuelos.push_back(comentario);
}


void SistemaComentarios::agregarComentarioPasajero(const string& comentario) {
    comentariosPasajeros.push_back(comentario);
}

void SistemaComentarios::imprimirComentariosVuelos() const {
    cout << "Comentarios de vuelos:" << endl;
    for (const string& comentario : comentariosVuelos) {
        cout << "- " << comentario << endl;
    }
}

void SistemaComentarios::imprimirComentariosPasajeros() const {
    cout << "Comentarios de pasajeros:" << endl;
    for (const string& comentario : comentariosPasajeros) {
        cout << "- " << comentario << endl;
    }
}


