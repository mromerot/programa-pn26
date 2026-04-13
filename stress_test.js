import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
    stages: [
        { duration: '1m', target: 500 },  // Rampa: de 0 a 500 usuarios en 1 min
        { duration: '2m', target: 2000 }, // El Gran Salto: de 500 a 2000 usuarios
        { duration: '1m', target: 2000 }, // Meseta: mantener 2000 usuarios viendo la agenda
        { duration: '1m', target: 0 },    // Bajada: los usuarios se van
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // El 95% de las peticiones deben durar menos de 500ms
        http_req_failed: ['rate<0.01'],   // Menos del 1% de errores
    },
};

export default function () {
    // Probamos la página de la agenda que es la más crítica
    const res = http.get('https://mromerot.github.io/programa-pn26/program/');

    check(res, {
        'status is 200': (r) => r.status === 200,
        'contenido cargado': (r) => r.body.includes('PN26'),
    });

    sleep(1); // Simula el tiempo que un humano tarda en leer
}