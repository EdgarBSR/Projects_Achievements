#include <iostream>
#include <vector>
#include <string>
#include "Pasajero.h"
#include "Vuelo.h"
#include "Reserva.h"
#include "Tripulacion.h"
#include "Aeropuerto.h"
#include "RegistrodeTripulacion.h"
#include "SistemaComentarios.h"
#include "BuscadorDeVuelos.h"




using namespace std;

int main() {

    /*
    Equipaje equipaje(20.5, 10.0, "En camino");
    // Crear un nuevo pasajero
    Pasajero* pasajero = new Pasajero();
    pasajero->setNombre("John Doe");
    pasajero->setDireccion("123 Main St");
    pasajero->setFechaNacimiento("1990-01-01");
    pasajero->setID("ABC123");
    pasajero->setEmail("johndoe@example.com");
    pasajero->setEquipaje(&equipaje);
    //pasajero->imprimirInformacion();

    // Crear un nuevo vuelo
    Vuelo* vuelo = new Vuelo();
    vuelo->setNumeroVuelo("FLIGHT123");
    vuelo->setOrigen("Ciudad A");
    vuelo->setDestino("Ciudad B");
    vuelo->setHoraSalida("10:00");
    vuelo->setHoraLlegada("12:00");
    vuelo->setAsientos(100);
    vuelo->setEquipaje(&equipaje);

     if (vuelo->validarVuelo()) {
        std::cout << "Vuelo valido" << std::endl;
    } else {
        std::cout << "Vuelo invalido" << std::endl;
    }

    vuelo->reservarAsiento();
    vuelo->cancelarReserva();

    // Crear una nueva reserva para el pasajero y el vuelo
    Reserva* reserva = new Reserva();
    reserva->setPasajero(pasajero);
    reserva->setVuelo(vuelo);
    reserva->setFechaReserva("2023-06-12");
    reserva->setEstatus("Confirmada");
    reserva->setIDReserva("011");
    reserva->imprimirInformacion();


    vuelo->imprimiInformacion();
    pasajero->imprimirInformacion();

    // Crear una instancia de Aeropuerto
    Aeropuerto* aeropuerto = new Aeropuerto();
    aeropuerto->setCodigoAeropuerto("ABC");
    aeropuerto->setNombre("Aeropuerto Internacional");
    aeropuerto->setCiudad("Ciudad de Ejemplo");
    aeropuerto->setPais("Pais de Ejemplo");

    // Crear una instancia de RegistroDeTripulacion
    RegistroDeTripulacion* registro = new RegistroDeTripulacion();

    // Crear instancias de Tripulacion y agregarlas al registro
    Tripulacion* tripulacion1 = new Tripulacion();
    tripulacion1->setID("123");
    tripulacion1->setPuesto("Piloto");
    registro->agregarTripulacion(tripulacion1);

    Tripulacion* tripulacion2 = new Tripulacion();
    tripulacion2->setID("456");
    tripulacion2->setPuesto("Auxiliar de vuelo");
    registro->agregarTripulacion(tripulacion2);

    // Establecer la asociación entre el registro y el aeropuerto
    registro->setAeropuerto(aeropuerto);

    // Acceder a la información de la asociación
    Aeropuerto* aeropuertoAsociado = registro->getAeropuerto();
    vector<Tripulacion*> tripulacionAsociada = registro->getTripulacion();

    // Imprimir la información de la tripulación y el aeropuerto asociados
    for (Tripulacion* tripulacion : tripulacionAsociada) {
        tripulacion->imprimirInformacion();
    }
    aeropuertoAsociado->imprimirINformacion();

    // Crear objeto de SistemaComentarios
    vuelo->setComentario("Excelente vuelo. Muy buen servicio.");
    pasajero->setResena("El vuelo fue muy cómodo y el personal amable.");

    vuelo->imprimiInformacion();
    pasajero->imprimirInformacion();

    // Imprimir información
    pasajero->imprimirInformacion();
    vuelo->imprimiInformacion();

    // Liberar la memoria
    delete registro;
    delete aeropuerto;
    for (Tripulacion* tripulacion : tripulacionAsociada) {
        delete tripulacion;
    }


    // Liberar la memoria
    delete reserva;
    delete vuelo;
    delete pasajero;
    */

     // Crear objetos iniciales
    Equipaje equipaje(0, 10.0, "En camino");
    Pasajero pasajero;
    Vuelo vuelo;
    Reserva reserva;
    Aeropuerto aeropuerto;
    RegistroDeTripulacion registro;
    SistemaComentarios sistemaComentarios;
    BuscadorDeVuelos buscador;


    // Variables para el bucle while


    char opcion;
    bool salir = false;

    while (!salir) {
        // Mostrar menú de opciones
        cout << "----- Menú -----" << endl;
        cout << "1. Realizar una reserva" << endl;
        cout << "2. Ver informacion de un vuelo" << endl;
        cout << "3. Ver informacion de un pasajero" << endl;
        cout << "4. Agregar tripulante al registro" << endl;
        cout << "5. Dejar un comentario o reseña" << endl;
        cout << "6. Buscar vuelos" << endl;
        cout<<"7. Salir del programa"<<endl;
        cout << "Ingrese su opcion: ";
        cin >> opcion;

        cin.ignore(); // Limpiar el buffer de entrada

        switch (opcion) {
            case '1': {
                // Realizar una reserva
                string nombrePasajero;
                string direccionPasajero;
                string fechaNacimientoPasajero;
                string IDPasajero;
                string emailPasajero;
                string numeroVuelo;
                string origenVuelo;
                string destinoVuelo;
                string horaSalidaVuelo;
                string horaLlegadaVuelo;
                int asientosVuelo;
                string fechaReserva;
                string estatus;
                string IDReserva;
                //int peso;
                //int costoadi;
                //string seguimiento;


                cout << "--- Realizar una reserva ---" << endl;

                // Pedir datos del pasajero
                cout << "Ingrese el nombre del pasajero: ";
                getline(cin, nombrePasajero);

                cout << "Ingrese la dirección del pasajero: ";
                getline(cin, direccionPasajero);

                cout << "Ingrese la fecha de nacimiento del pasajero (YYYY-MM-DD): ";
                getline(cin, fechaNacimientoPasajero);

                cout << "Ingrese el ID del pasajero: ";
                getline(cin, IDPasajero);

                cout << "Ingrese el email del pasajero: ";
                getline(cin, emailPasajero);

                pasajero.setNombre(nombrePasajero);
                pasajero.setDireccion(direccionPasajero);
                pasajero.setFechaNacimiento(fechaNacimientoPasajero);
                pasajero.setID(IDPasajero);
                pasajero.setEmail(emailPasajero);
                pasajero.setEquipaje(&equipaje);

                // Pedir datos del vuelo
                cout << "Ingrese el número del vuelo: ";
                getline(cin, numeroVuelo);

                cout << "Ingrese el origen del vuelo: ";
                getline(cin, origenVuelo);

                cout << "Ingrese el destino del vuelo: ";
                getline(cin, destinoVuelo);

                cout << "Ingrese la hora de salida del vuelo: ";
                getline(cin, horaSalidaVuelo);

                cout << "Ingrese la hora de llegada del vuelo: ";
                getline(cin, horaLlegadaVuelo);

                cout << "Ingrese la cantidad de asientos disponibles del vuelo: ";
                cin >> asientosVuelo;

                vuelo.setNumeroVuelo(numeroVuelo);
                vuelo.setOrigen(origenVuelo);
                vuelo.setDestino(destinoVuelo);
                vuelo.setHoraSalida(horaSalidaVuelo);
                vuelo.setHoraLlegada(horaLlegadaVuelo);
                vuelo.setAsientos(asientosVuelo);
                vuelo.setEquipaje(&equipaje);

                // Pedir datos de la reserva
                cin.ignore(); // Limpiar el buffer de entrada

                cout << "Ingrese la fecha de la reserva (YYYY-MM-DD): ";
                getline(cin, fechaReserva);

                cout << "Ingrese el estatus de la reserva: ";
                getline(cin, estatus);

                cout << "Ingrese el ID de la reserva: ";
                getline(cin, IDReserva);

                reserva.setPasajero(&pasajero);
                reserva.setVuelo(&vuelo);
                reserva.setFechaReserva(fechaReserva);
                reserva.setEstatus(estatus);
                reserva.setIDReserva(IDReserva);

                reserva.imprimirInformacion();
                break;
            }
            case '2':
                // Ver información de un vuelo
                vuelo.imprimiInformacion();
                break;
            case '3':
                // Ver información de un pasajero
                pasajero.imprimirInformacion();
                break;
            case '4': {
                // Agregar tripulante al registro
                string IDTripulacion;
                string puestoTripulacion;
                string nameareopuerto;

                cout << "--- Agregar tripulante al registro ---" << endl;

                cout << "Ingrese el ID del tripulante: ";
                getline(cin, IDTripulacion);

                cout << "Ingrese el puesto del tripulante: ";
                getline(cin, puestoTripulacion);

                cout << "Ingrese el nombre del aeropuerto: ";
                getline(cin, nameareopuerto);

                Tripulacion* tripulante = new Tripulacion();
                tripulante->setID(IDTripulacion);
                tripulante->setPuesto(puestoTripulacion);
                aeropuerto.setNombre(nameareopuerto);

                registro.agregarTripulacion(tripulante);
                cout << "Tripulante agregado correctamente" << endl;
                break;
            }
            case '5': {
                // Dejar un comentario o reseña
                string comentario;
                string resena;

                cout << "--- Dejar un comentario o resena ---" << endl;

                cout << "Ingrese un comentario sobre el vuelo: ";
                getline(cin, comentario);

                cout << "Ingrese una resena sobre su experiencia de vuelo: ";
                getline(cin, resena);

                //sistemaComentarios.agregarComentarioVuelo(vuelo, comentario);
                //sistemaComentarios.agregarComentarioPasajero(pasajero, resena);

                cout << "Comentario y reseña agregados correctamente" << endl;
                break;
            }

             case '6': {
                 /*

                 std::string origen, destino;
                std::cout << "Ingrese el origen: ";
                std::cin >> origen;
                std::cout << "Ingrese el destino: ";
                std::cin >> destino;

                std::vector<Vuelo> vuelosEncontrados = buscador.buscarVuelos(origen, destino);

                if (vuelosEncontrados.empty()) {
                    std::cout << "No se encontraron vuelos disponibles para los criterios de búsqueda." << std::endl;
                } else {
                    std::cout << "Vuelos disponibles:" << std::endl;
                    for (const auto& vuelo : vuelosEncontrados) {
                        std::cout << "Origen: " << vuelo.origen << ", Destino: " << vuelo.destino << ", Aerolínea: "
                                  << vuelo.aerolinea << ", Precio: " << vuelo.precio << std::endl;
                    }
                }
                */

            case '7': {
                // Salir del programa
                salir = true;
                break;
            default:
                cout << "Opción invalida. Intente nuevamente." << endl;

    }




        return 0;

    }
    }
}
}
