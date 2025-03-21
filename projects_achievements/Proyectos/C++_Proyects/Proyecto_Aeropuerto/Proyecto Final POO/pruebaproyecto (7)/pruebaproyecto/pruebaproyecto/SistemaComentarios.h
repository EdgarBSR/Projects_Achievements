#ifndef SISTEMACOMENTARIOS_H_INCLUDED
#define SISTEMACOMENTARIOS_H_INCLUDED

#include <string>
#include "Vuelo.h"
#include "Pasajero.h"

#include <iostream>
#include <vector>
#include <string>
#include "Vuelo.h"
#include "Pasajero.h"

class SistemaComentarios {
private:
    vector<string> comentariosVuelos;
    vector<string> comentariosPasajeros;

    class ComentarioVacioException : public std::exception {
    public:
        const char* what() const noexcept override {
            return "El comentario no puede estar vacío.";
        }
    };


public:
    void agregarComentarioVuelo(const string& comentario);
    void agregarComentarioPasajero(const string& comentario);
    void imprimirComentariosVuelos() const;
    void imprimirComentariosPasajeros() const;
};

#endif // SISTEMACOMENTARIOS_H_INCLUDED
