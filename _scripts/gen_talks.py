#!/usr/bin/env python3
"""Generate 264 unique talks for PN26. Run from project root."""

import os, re, random, glob

PROJECT = "/Users/mauricio/Documents/Data-science-local/programa-pn26"
TALKS_DIR = os.path.join(PROJECT, "_talks")

# ── SPEAKER GENERATION ────────────────────────────────────────────────────────
random.seed(77)

FIRST_F = ["Ana","Beatriz","Carolina","Claudia","Diana","Elena","Esperanza",
           "Fabiola","Gloria","Heidy","Ingrid","Irene","Jana","Kelly","Liliana",
           "Lorena","Lucía","Luisa","Manuela","Margarita","Marisol","Marta",
           "Natalia","Nelly","Nora","Ofelia","Paola","Patricia","Paula","Piedad",
           "Renata","Rocío","Rosa","Sara","Silvia","Sofía","Tatiana","Teresa",
           "Valentina","Vanessa","Verónica","Viviana","Ximena","Yolanda","Zulma",
           "Alejandra","Astrid","Bibiana","Carla","Carmen","Constanza","Dora",
           "Fernanda","Flor","Graciela","Juliana","Lina","Marcela","Mónica",
           "Olga","Pilar","Sandra","Sara","Andrea","Isabel","Daniela","Clara"]

FIRST_M = ["Alejandro","Alberto","Álvaro","Andrés","Antonio","Arturo","Camilo",
           "Carlos","César","Daniel","David","Diego","Eduardo","Ernesto","Esteban",
           "Felipe","Fernando","Gabriel","Germán","Gustavo","Harold","Héctor",
           "Hernando","Ignacio","Iván","Jaime","Jairo","Jorge","Juan","Julián",
           "Leonardo","Luis","Manuel","Marco","Mauricio","Miguel","Néstor",
           "Nicolás","Orlando","Oscar","Pablo","Pedro","Rafael","Ramón",
           "Ricardo","Roberto","Rodrigo","Sergio","Sebastián","Tomás","Víctor",
           "Wilson","Nelson","César","Raúl","Orlando","Harold","Camilo","Marco"]

LAST = ["Acosta","Aguilar","Arbeláez","Arango","Barrera","Becerra","Bedoya",
        "Bernal","Bermúdez","Botero","Calderón","Cano","Cárdenas","Carvajal",
        "Castaño","Castillo","Castro","Ceballos","Cifuentes","Córdoba","Correa",
        "Daza","Delgado","Díaz","Duque","Echeverri","Escobar","Fernández",
        "Flórez","Fonseca","Fuentes","Galvis","Galeano","García","Giraldo",
        "Gómez","González","Guerrero","Gutiérrez","Henao","Herrera","Infante",
        "Isaza","Jaramillo","Jiménez","Leiva","Loaiza","Londoño","Lozano",
        "López","Macías","Marulanda","Medina","Mejía","Mendoza","Molina",
        "Montoya","Morales","Moreno","Muñoz","Naranjo","Navarro","Nieto",
        "Noreña","Ochoa","Orozco","Ortiz","Ossa","Ospina","Palacios","Palomino",
        "Parra","Patiño","Pedraza","Pérez","Pineda","Posada","Pulido","Quintero",
        "Quiroga","Ramos","Rengifo","Restrepo","Reyes","Ríos","Robledo","Rojas",
        "Romero","Rueda","Salazar","Sánchez","Serrano","Sierra","Soto","Suárez",
        "Tamayo","Tobón","Torres","Trujillo","Uribe","Urquijo","Urrea","Valencia",
        "Vargas","Vásquez","Vélez","Velásquez","Vera","Wilches","Yépez","Zapata",
        "Zuluaga","Ramírez","Rodríguez","Martínez","Galindo","Holguín","Reina"]

TITLES_F = ["Dra.","Ing.","MSc.","Lic.","PhD.","Dra.","Ing."]
TITLES_M = ["Dr.","Ing.","MSc.","Lic.","PhD.","Dr.","Ing."]

INSTS = ["SGC","IDEAM","IGAC","DANE","DNP","UNGRD","PNUD","OCHA","Uniandes",
         "UNAL Bogotá","EAFIT","Javeriana","Cruz Roja Col.","Defensa Civil",
         "MinTIC","MinCiencias","AIS","OSSO Corp","INVEMAR","Fondo Adaptación",
         "ETH Zurich","Banco Mundial","USAID Col.","WMO","DIMAR","U. Antioquia",
         "U. EIA","Cenicafé","LIGA","Área Metro VAB","PAHO","GIZ","JICA","AECID",
         "CEPAL","OPS","CARE Int.","World Vision","Oxfam Col.","Save the Children",
         "UN Hábitat","ACNUR","OIM","IFRC","UNDRR","CIAT","Humboldt","WWF Col.",
         "TNC Colombia","ICANH","ProColombia","Colciencias","SENA","ICBF","CVC",
         "Corpocaldas","Cornare","CAR","Corpoamazonia","Corponariño","CDMB",
         "Secretaría Distrital Bogotá","Alcaldía Medellín","Gobernación Antioquia",
         "Gobernación Valle","Gobernación Nariño","Gobernación Cundinamarca",
         "U. del Valle","U. del Norte","U. de Manizales","U. Surcolombiana",
         "U. Pontificia Bolivariana","U. Tecnológica de Pereira","U. de Caldas",
         "U. de Córdoba","U. del Pacífico","ESAP","Escuela de Ingeniería de Antioquia"]

EXISTING = {
    "Ana María Quintero","Andrés Felipe Moreno","Beatriz Elena Acosta",
    "Carlos Andrade Ospina","Claudia Milena Torres","César Augusto Vargas",
    "Diana Carolina Ruiz","Eduardo Herrera Llano","Felipe Restrepo Arias",
    "Gustavo Adolfo Cano","Hernando Garavito Silva","Iván Darío Pérez",
    "Jorge Iván Salamanca","Julián Ernesto Barrera","Lina María Cortés",
    "Luz Adriana Peñuela","Marcela Sánchez Duque","María Elena Rodríguez",
    "Mónica Patricia Zamora","Natalia Ospina Vélez","Nelson Fabián Ochoa",
    "Olga Lucía Mendoza","Patricia Vásquez Cano","Pilar Sofía Guerrero",
    "Rafael Adolfo Castaño","Roberto Arango Mejía","Rodrigo Suárez Parra",
    "Sandra Lucía Gómez","Viviana Alejandra Muñoz","Álvaro Enrique Díaz",
}

def make_speakers(n):
    used = set(EXISTING)
    result = []
    attempts = 0
    while len(result) < n and attempts < 50000:
        attempts += 1
        g = random.choice(['f','m'])
        if g == 'f':
            fn = random.choice(FIRST_F); title = random.choice(TITLES_F)
        else:
            fn = random.choice(FIRST_M); title = random.choice(TITLES_M)
        ln1 = random.choice(LAST)
        ln2 = random.choice(LAST)
        while ln2 == ln1:
            ln2 = random.choice(LAST)
        full = f"{fn} {ln1} {ln2}"
        if full not in used:
            used.add(full)
            inst = random.choice(INSTS)
            result.append(f"{title} {fn} {ln1} {ln2} · {inst}")
    return result

speakers = make_speakers(264)

# ── TALK DATA ────────────────────────────────────────────────────────────────
TALKS = {
    "Resiliencia (Sala 1)": {
        "Miércoles": [
            "Actualización del modelo nacional de amenaza sísmica 2025",
            "Mapeo de microzonificación sísmica en ciudades intermedias colombianas",
            "Inventario nacional de movimientos en masa: metodología y estado actual",
            "Modelación bidimensional de flujos torrenciales en cuencas andinas",
            "Calibración de modelos hidrológicos con datos de radar meteorológico",
            "Evaluación de la amenaza por tsunami en el litoral Pacífico colombiano",
            "Análisis estadístico de series históricas de precipitación extrema en Colombia",
            "Cartografía geomorfológica aplicada a la evaluación de amenazas naturales",
            "Monitoreo geodésico de volcanes activos con técnicas InSAR",
            "Datación de depósitos de lahar mediante carbono-14 en el Nevado del Ruiz",
            "Registro histórico de terremotos destructivos en Colombia 1566-2025",
        ],
        "Jueves": [
            "Modelación probabilista de amenaza volcánica con árboles de eventos",
            "Susceptibilidad a deslizamientos: comparativa de métodos estadísticos y ML",
            "Estimación de la amenaza sísmica en sitio con coeficientes de amplificación",
            "Análisis de cuencas de recepción para flujos de detritos en el Eje Cafetero",
            "Variabilidad climática ENSO e intensidad de temporadas de lluvias en Colombia",
            "Evaluación multiamenaza en municipios priorizados del Pacífico colombiano",
            "Caracterización geotécnica de materiales volcánicos en laderas inestables",
            "Sensores GNSS de bajo costo para monitoreo de deformaciones superficiales",
            "Delimitación de zonas de protección hídrica con análisis de inundación histórica",
            "Efectos de sitio en suelos blandos: municipio de Armenia post-sismo 1999",
            "Paleosismología y recurrencia de grandes terremotos en la falla Cauca-Romeral",
        ],
        "Viernes": [
            "Red sismológica nacional: estado de la instrumentación y planes de expansión",
            "Análisis espectral de señales sísmicas para clasificación automática de eventos",
            "Vulnerabilidad geotécnica de infraestructura vial en zonas de alta sismicidad",
            "Escenarios de inundación por lluvias extremas bajo cambio climático en Colombia",
            "Registro LiDAR de cicatrices de deslizamiento en la cuenca del río Magdalena",
            "Zonificación de amenaza por erosión costera en el Caribe colombiano",
            "Modelación de la propagación de tsunamis en el océano Pacífico colombiano",
            "Análisis de recurrencia de avenidas torrenciales en cuencas de la Sierra Nevada",
            "Determinación del nivel freático como factor detonante de deslizamientos",
            "Evaluación de la amenaza sísmica en plantas de generación eléctrica colombianas",
            "Geología del cuaternario y riesgo de licuefacción en depósitos aluviales",
        ],
    },
    "Participación (Sala 2)": {
        "Miércoles": [
            "Índice de vulnerabilidad social multidimensional para municipios colombianos en riesgo",
            "Percepción local del riesgo en comunidades afrocolombianas del Pacífico",
            "Capital social y capacidad de respuesta en barrios de ladera en Medellín",
            "Etnomapeo de riesgos en resguardos indígenas de la Amazonía colombiana",
            "Evaluación de vivienda rural no convencional en zonas sísmicas intermedias",
            "Autoreforzamiento de viviendas con participación comunitaria: guías técnicas",
            "Desigualdad urbana y distribución espacial del riesgo en Bogotá D.C.",
            "Riesgo de desastres y desnutrición crónica: vínculos en la ruralidad colombiana",
            "Adultos mayores y discapacidad en planes de preparación para emergencias",
            "Movilidad humana previa y post-desastre en el Archipiélago de San Andrés",
            "Análisis de género en los impactos diferenciados de inundaciones en el Meta",
        ],
        "Jueves": [
            "Brigadas comunitarias de gestión del riesgo: evaluación de competencias técnicas",
            "Saberes tradicionales y gestión del territorio en comunidades campesinas del Huila",
            "Escuelas seguras frente a desastres: diagnóstico de infraestructura educativa",
            "Acceso a información de riesgo en comunidades con bajos niveles de escolaridad",
            "Cartografía de riesgos con perspectiva de género en el Caribe colombiano",
            "Vulnerabilidad de asentamientos informales ante inundaciones en Cali",
            "Resiliencia familiar post-desastre: factores protectores y de riesgo identificados",
            "Migración rural-urbana y acumulación de riesgo en ciudades intermedias colombianas",
            "Participación de las mujeres en los Consejos Municipales de Gestión del Riesgo",
            "Niñez y juventud como actores en la construcción de cultura de gestión del riesgo",
            "Eficacia de redes comunitarias de alerta ante crecientes súbitas en el Cauca",
        ],
        "Viernes": [
            "Recuperación de medios de vida en comunidades pesqueras post-desastre costero",
            "Acceso a servicios de salud en emergencias para poblaciones dispersas en Vichada",
            "Comunidades negras e indígenas frente a la sequía en La Guajira colombiana",
            "Impactos del desplazamiento forzado en la acumulación de riesgo urbano",
            "Tejido social y cohesión comunitaria como factores de resiliencia post-inundación",
            "Evaluación de competencias en gestión del riesgo de funcionarios municipales",
            "Diálogo intercultural para la integración del conocimiento local en la GRD",
            "Rol de la mujer cabeza de hogar en la recuperación post-desastre en el Chocó",
            "Violencia basada en género en contextos de desastre: evidencia colombiana",
            "Memoria histórica de desastres como herramienta de sensibilización comunitaria",
            "Riesgo socioambiental en zonas de minería artesanal en el Bajo Cauca antioqueño",
        ],
    },
    "Solidaridad (Sala 3)": {
        "Miércoles": [
            "Diseño de rutas de evacuación en municipios de alta montaña volcánica",
            "Cadena de mando y coordinación interinstitucional en la respuesta a desastres",
            "Logística de distribución de ayuda humanitaria en zonas de difícil acceso fluvial",
            "Evaluación de daños en infraestructura hospitalaria después de un sismo",
            "Gestión de albergues temporales con enfoque de género y diversidad",
            "Protocolos de búsqueda y rescate en estructuras colapsadas por terremoto",
            "Manejo de fallecidos en eventos de masas y su impacto en la salud pública",
            "Telecomunicaciones de emergencia y planes de contingencia ante colapso de redes",
            "Primeros auxilios psicológicos en respuesta a emergencias de masas",
            "Atención integral a personas con discapacidad en situaciones de emergencia",
            "Planes de contingencia para el sistema de acueducto en emergencias sísmicas",
        ],
        "Jueves": [
            "Coordinación civil-militar en operaciones de respuesta a desastres en Colombia",
            "Gestión logística de la ayuda humanitaria durante la emergencia por Ola Invernal",
            "Triaje en situaciones de múltiples víctimas: protocolos START y SALT adaptados",
            "Evaluación estructural rápida de puentes post-sismo para apertura de vías",
            "Operaciones de rescate en zonas inundadas con embarcaciones de motor",
            "Gestión de residuos sólidos y escombros en fases de recuperación temprana",
            "Cadena de frío y distribución de medicamentos en zonas de emergencia prolongada",
            "Movilización de recursos del Fondo Nacional de Calamidades: procedimientos",
            "Voluntariado corporativo en respuesta a emergencias: marcos de colaboración",
            "Simulacros de evacuación en edificios de gran altura: análisis de comportamiento",
            "Evaluación del impacto de los simulacros nacionales en la cultura de preparación",
        ],
        "Viernes": [
            "Lecciones aprendidas de la respuesta al deslizamiento de Mocoa en 2017",
            "Gestión de la información en el Centro de Operaciones de Emergencias Nacional",
            "Desmovilización de voluntarios tras operaciones de respuesta prolongadas",
            "Impacto psicológico a largo plazo en respondedores de primera línea en Colombia",
            "Acuerdos de asistencia mutua entre municipios: marco jurídico y operativo",
            "Mantenimiento de equipos de búsqueda y rescate en contextos de alta humedad",
            "Evaluación post-operación en el Sistema Comando de Incidentes colombiano",
            "Restablecimiento de servicios esenciales en la fase de recuperación temprana",
            "Integración de actores privados en los planes municipales de contingencia",
            "Gestión del conocimiento en organizaciones de respuesta a emergencias",
            "Planificación de la continuidad operativa en entidades del SNGRD",
        ],
    },
    "Cimientos (Sala 4)": {
        "Miércoles": [
            "Implementación de la Ley 1523 de 2012: balance a trece años de vigencia",
            "Los Planes Municipales de Gestión del Riesgo como instrumentos de planificación",
            "Integración del riesgo en los Planes de Ordenamiento Territorial: estado del arte",
            "Rendición de cuentas en la ejecución de recursos para la gestión del riesgo",
            "Marco normativo de las CAR en la gestión del riesgo de desastres en Colombia",
            "Competencias de los Concejos Municipales en la reducción del riesgo de desastres",
            "Financiamiento público de la GRD: análisis del presupuesto nacional 2018-2025",
            "Transferencia de riesgo al sector privado: seguros y bonos catástrofe en Colombia",
            "El papel del Ministerio de Vivienda en la reducción del riesgo en asentamientos",
            "Política pública de reasentamiento de hogares en zonas de alto riesgo no mitigable",
            "Rol del Congreso de la República en la legislación sobre gestión del riesgo",
        ],
        "Jueves": [
            "Acuerdo de Escazú y acceso a la información ambiental en contextos de riesgo",
            "Descentralización fiscal y capacidad municipal para la gestión del riesgo",
            "Enfoque de derechos humanos en la política de gestión del riesgo de Colombia",
            "Mecanismos de veeduría ciudadana en proyectos de reducción del riesgo",
            "Régimen especial de contratación para la atención de desastres en Colombia",
            "Integración del riesgo de desastres en los planes de desarrollo departamental",
            "Gobernanza del riesgo en las Áreas Metropolitanas: experiencia de Cali y Bogotá",
            "El Marco de Sendai y su implementación en el ordenamiento jurídico colombiano",
            "Cooperación descentralizada en GRD: municipios colombianos y socios europeos",
            "Actuación del Ministerio Público en la prevención y atención de desastres",
            "Reforma institucional del SNGRD: propuestas para una segunda generación",
        ],
        "Viernes": [
            "Gestión del riesgo en zonas de frontera: desafíos de coordinación binacional",
            "Política de asentamientos humanos y reducción del riesgo en Colombia",
            "Instrumentos económicos para la gestión del riesgo: tasas, cargos y subsidios",
            "Corrupción en la contratación de obras de mitigación: casos y lecciones aprendidas",
            "Evaluación de impacto de los Planes Departamentales de Gestión del Riesgo",
            "Articulación entre la política de GRD y la política de cambio climático en Colombia",
            "Participación de la sociedad civil en los espacios de gobernanza del SNGRD",
            "La gestión del riesgo como eje transversal en la política de desarrollo rural",
            "Marco regulatorio de las telecomunicaciones en situaciones de emergencia",
            "Análisis costo-beneficio de las inversiones en reducción del riesgo en Colombia",
            "Integración del riesgo de desastres en los ODS en el contexto colombiano",
        ],
    },
    "Gobernanza (Sala VIP)": {
        "Miércoles": [
            "Infraestructura nacional de datos geoespaciales para la gestión del riesgo",
            "Plataformas SIG en la nube para la gestión del riesgo a escala municipal",
            "Algoritmos de detección de cambios en imágenes Sentinel-2 post-desastre",
            "Integración de datos LiDAR aerotransportado en modelos de amenaza de ladera",
            "Redes de monitoreo sísmico en tiempo real: arquitectura y protocolos de datos",
            "Teledetección SAR para el mapeo de inundaciones en la Orinoquía colombiana",
            "Visión por computador para clasificación de daños estructurales post-sismo",
            "Digital twins de infraestructura crítica para simulación de escenarios de riesgo",
            "APIs abiertas para el intercambio de datos de riesgo entre entidades del SNGRD",
            "Sistemas NoSQL para la gestión de datos en emergencias de gran escala",
            "Ciberseguridad en los sistemas de información del SNGRD",
        ],
        "Jueves": [
            "Modelos de lenguaje grande (LLM) aplicados a la síntesis de informes de situación",
            "Procesamiento de imágenes de drones con software libre en evaluación post-desastre",
            "Redes neuronales convolucionales para la detección automatizada de deslizamientos",
            "Internet de las cosas aplicado a cuencas hidrográficas: telemetría de bajo costo",
            "Computación en la frontera (edge computing) para alertas tempranas en zonas rurales",
            "Crowdsourcing para la validación de mapas de daños post-evento en Colombia",
            "Análisis de sentimiento en redes sociales durante emergencias con NLP",
            "Simulación de evacuación mediante dinámica de fluidos computacional",
            "Reconocimiento automático de patrones sísmicos con redes LSTM",
            "Interoperabilidad de sistemas de alerta temprana bajo el estándar CAP 1.2",
            "Arquitectura de microservicios para plataformas de gestión de emergencias",
        ],
        "Viernes": [
            "Evaluación de la madurez digital de las entidades del SNGRD colombiano",
            "Inteligencia artificial explicable (XAI) en modelos de predicción de riesgo",
            "Integración de datos de satélites de baja órbita (LEO) en sistemas de alerta",
            "Gemelos digitales urbanos para la planificación del riesgo en Bogotá",
            "Plataforma nacional de datos abiertos de riesgo: gobernanza y estándares",
            "Machine learning para la detección automática de asentamientos en zonas de riesgo",
            "Análisis de redes complejas en sistemas de infraestructura crítica interdependiente",
            "Blockchain y trazabilidad en la cadena logística de la ayuda humanitaria",
            "Procesamiento de señales de infrasónico para detección de erupciones volcánicas",
            "Realidad virtual e inmersiva en la formación para la gestión del riesgo",
            "Perspectivas de la computación cuántica para la modelación del riesgo de desastres",
        ],
    },
    "Entretejidos (Mezzanine)": {
        "Miércoles": [
            "Nexo entre cambio climático, degradación ambiental y aumento del riesgo",
            "Ecosistemas de manglar como infraestructura natural para reducción del riesgo costero",
            "Restauración de cuencas hidrográficas como medida de reducción del riesgo",
            "Riesgo de desastres y seguridad alimentaria en regiones agrícolas vulnerables",
            "Integración de la gestión del riesgo en los planes de salud territorial",
            "Riesgo tecnológico e industrial en el corredor petroquímico de Barrancabermeja",
            "Patrimonio cultural en riesgo: estrategias de conservación preventiva en Colombia",
            "Impacto de los desastres en la cobertura educativa en zonas rurales colombianas",
            "Desastres y pobreza: análisis de la trampa de la vulnerabilidad en Colombia",
            "Biodiversidad y ecosistemas como factores de resiliencia territorial",
            "Articulación entre la gestión del riesgo y la política de seguridad hídrica",
        ],
        "Jueves": [
            "Gestión integral del recurso hídrico en cuencas compartidas y riesgo de desastres",
            "Infraestructura verde urbana y reducción del riesgo de inundación en ciudades",
            "Nexo agua-energía-alimentos en contextos de riesgo climático en Colombia",
            "Gestión de riesgos en el sector turístico costero: experiencias del Caribe",
            "Riesgo sísmico en la infraestructura de petróleo y gas en la cuenca de los Llanos",
            "Impactos en la biodiversidad de los grandes movimientos en masa en el Pacífico",
            "Gestión del riesgo en corredores logísticos de alto valor económico para Colombia",
            "Análisis de riesgo en infraestructura vial de montaña: el caso de la vía al Llano",
            "Contaminación hídrica post-desastre y afectación a ecosistemas acuáticos",
            "Riesgo de desastres en el sector minero-energético de Colombia",
            "Turismo de riesgo y memoria: oportunidades para el desarrollo local en Colombia",
        ],
        "Viernes": [
            "Integración del riesgo de desastres en las cuentas nacionales ambientales",
            "Gestión del riesgo en sistemas de transporte masivo en ciudades colombianas",
            "Impacto de los desastres en el patrimonio arqueológico colombiano",
            "Riesgo de desastres en la economía del cuidado: afectaciones diferenciadas por género",
            "Gestión del riesgo en zonas de producción cafetera: lecciones del Cenicafé",
            "Infraestructura de telecomunicaciones resiliente para zonas de alta sismicidad",
            "Seguro agrícola paramétrico como herramienta de transferencia del riesgo rural",
            "Gestión del riesgo en el sector salud: hospitales seguros en Colombia",
            "Impacto de la deforestación en la generación de deslizamientos en el piedemonte",
            "Riesgo sistémico y cascada de fallas en infraestructura crítica interdependiente",
            "Resiliencia urbana y planificación municipal en la región del Eje Cafetero",
        ],
    },
    "Horizonte (Capilla)": {
        "Miércoles": [
            "Escenarios de riesgo de desastres en Colombia al 2050 bajo cambio climático",
            "Innovación social en la gestión del riesgo: experiencias en municipios rurales",
            "Riesgo de eventos compuestos (compound events) en el sistema climático colombiano",
            "Nanotecnología aplicada a materiales de construcción sismo-resistentes",
            "Impacto del cambio de uso del suelo en la generación de inundaciones urbanas",
            "Ciudades esponja: principios y aplicaciones en el contexto colombiano",
            "Financiamiento basado en resultados para la reducción del riesgo de desastres",
            "Riesgo de desastres en el contexto de la transición energética colombiana",
            "Innovación en sistemas de alerta temprana comunitaria de bajo costo",
            "Ciudades resilientes: indicadores y marcos de evaluación para Colombia",
            "Prospectiva estratégica en la gestión del riesgo de desastres",
        ],
        "Jueves": [
            "Gobernanza anticipatoria del riesgo: marcos para la acción preventiva en Colombia",
            "Riesgo de desastres y digitalización de la economía colombiana",
            "Impacto de megaproyectos de infraestructura en la generación de nuevos riesgos",
            "Sistemas de seguros paramétricos para catástrofes naturales en Colombia",
            "Perspectivas del financiamiento privado en la reducción del riesgo de desastres",
            "Innovación en la gestión de residuos post-desastre con economía circular",
            "Análisis de tipping points en sistemas socioecológicos expuestos al riesgo",
            "Gestión del riesgo de desastres en la agenda de los Objetivos de Desarrollo Sostenible",
            "Gestión adaptativa del riesgo ante la incertidumbre climática en Colombia",
            "Enfoques de sistemas complejos para la comprensión del riesgo de desastres",
            "Planeación de largo plazo en la gestión del riesgo: el caso de los POMCAS",
        ],
        "Viernes": [
            "Riesgo emergente por calor extremo urbano en las ciudades colombianas",
            "Impactos del deshielo de nevados colombianos en la disponibilidad hídrica",
            "Riesgo de sequía en la región Caribe ante escenarios de cambio climático",
            "Transición hacia ciudades bajas en carbono y co-beneficios en resiliencia",
            "Innovación en modelos de financiamiento de la recuperación post-desastre",
            "Riesgo de pandemias y desastres compuestos: lecciones post-COVID para Colombia",
            "Aprendizaje automático para la actualización dinámica de mapas de riesgo",
            "Perspectivas de la economía conductual en la adopción de medidas preventivas",
            "Riesgo de desastres en la era de la inteligencia artificial generalizada",
            "El rol de la filantropía estratégica en el financiamiento de la resiliencia",
            "Futuro de la cooperación internacional en gestión del riesgo post-2030",
        ],
    },
    "Sinergia (Sala Piso 2)": {
        "Miércoles": [
            "Cooperación triangular en gestión del riesgo: Colombia-Chile-CEPAL",
            "Gestión del riesgo en países andinos: comparativa regional de avances",
            "El modelo japonés de preparación ante desastres: lecciones para Colombia",
            "Alianzas público-privadas para la financiación de infraestructura resiliente",
            "Gestión del riesgo en pequeños estados insulares del Caribe: lecciones aplicables",
            "El papel de la academia en la implementación del Marco de Sendai en América Latina",
            "Riesgo de desastres y migración climática en Centroamérica y norte de Suramérica",
            "Experiencias de reducción del riesgo en comunidades rurales de Bangladesh",
            "Instrumentos financieros multilaterales para la gestión del riesgo en Colombia",
            "Gestión del conocimiento en redes internacionales de práctica en GRD",
            "Estándares internacionales de calidad en ayuda humanitaria: el proyecto ESFERA",
        ],
        "Jueves": [
            "Gestión del riesgo en ciudades costeras de Asia Pacífico: transferencia de conocimiento",
            "Cooperación Sur-Sur en gestión del riesgo: experiencias de Colombia en África",
            "Arquitectura de gobernanza global del riesgo de desastres: UNDRR y el sistema ONU",
            "Riesgo de desastres y comercio internacional: implicaciones para Colombia",
            "El rol del sector privado en la reducción del riesgo: iniciativas y pactos globales",
            "Gestión del riesgo en ciudades patrimonio de la humanidad: el desafío de la conservación",
            "Experiencias de recuperación post-desastre en Haití: catorce años de lecciones",
            "Ecosistemas de innovación para la resiliencia: modelos referentes en el mundo",
            "Mecanismos de solidaridad internacional post-desastre: del CERF a los llamamientos",
            "Riesgo de desastres y cadenas de suministro globales: vulnerabilidades expuestas",
            "Intercambio tecnológico en gestión del riesgo entre Colombia y la Unión Europea",
        ],
        "Viernes": [
            "El Marco de Sendai 2015-2030 a mitad de camino: avances y brechas globales",
            "Experiencias latinoamericanas de integración del riesgo en el ordenamiento territorial",
            "Gestión del riesgo en megaciudades: Ciudad de México, Lima y Bogotá comparadas",
            "Transferencia de conocimiento en gestión del riesgo: el modelo de la red CAPRA",
            "Riesgo de desastres y refugiados climáticos: marcos internacionales de protección",
            "Financiamiento climático para la adaptación y reducción del riesgo: brechas globales",
            "Experiencias de alerta temprana comunitaria en África Subsahariana",
            "Gestión del riesgo en contextos de conflicto armado: el nexo humanitario-desarrollo",
            "El papel de las ciudades en la diplomacia del riesgo de desastres",
            "Indicadores globales de reducción del riesgo: medición y comparabilidad entre países",
            "Nuevas arquitecturas de financiamiento para la resiliencia post-2030",
        ],
    },
}

ROOM_TRACK = {
    "Resiliencia (Sala 1)": "Sesión temática",
    "Participación (Sala 2)": "Sesión paralela",
    "Solidaridad (Sala 3)": "Sesión paralela",
    "Cimientos (Sala 4)": "Sesión temática",
    "Gobernanza (Sala VIP)": "Sesión especial",
    "Entretejidos (Mezzanine)": "Sesión temática",
    "Horizonte (Capilla)": "Laboratorio de aprendizaje",
    "Sinergia (Sala Piso 2)": "Plenaria",
}

SLOTS = [
    ("07:30", "08:15"),
    ("08:15", "09:00"),
    ("09:15", "10:00"),
    ("10:00", "10:45"),
    ("10:45", "11:30"),
    ("14:00", "14:45"),
    ("14:45", "15:30"),
    ("15:45", "16:30"),
    ("16:30", "17:15"),
    ("17:30", "18:15"),
    ("18:15", "19:00"),
]

DAYS = ["Miércoles", "Jueves", "Viernes"]

DAY_META = {
    "Miércoles": ("Mié", "2026-05-20"),
    "Jueves":    ("Jue", "2026-05-21"),
    "Viernes":   ("Vie", "2026-05-22"),
}

AUDITORIO = {
    "Miércoles": [
        ("Apertura institucional: Plataforma Nacional 2026",    "09:00", "10:00"),
        ("Diálogo de alto nivel: cooperación internacional en GRD", "14:00", "15:00"),
    ],
    "Jueves": [
        ("Panel plenario: tecnología e innovación en gestión del riesgo", "09:00", "10:00"),
        ("Diálogo de financiamiento: inversión para la resiliencia",      "14:00", "15:00"),
    ],
    "Viernes": [
        ("Clausura PN26: declaración y compromisos", "09:00", "10:00"),
    ],
}

# ── SLUGIFY ───────────────────────────────────────────────────────────────────
def slugify(text):
    s = text.lower()
    for a, b in [("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"),("ü","u"),
                 ("ñ","n"),("à","a"),("è","e"),("ì","i"),("ò","o"),("ù","u")]:
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9\s\-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:70].rstrip("-")

# ── BUILD FLAT LIST ────────────────────────────────────────────────────────────
entries = []  # (title, speaker, track, slug)
speaker_idx = 0
for day in DAYS:
    for room, day_data in TALKS.items():
        titles = day_data[day]
        for title in titles:
            spk = speakers[speaker_idx]
            speaker_idx += 1
            track = ROOM_TRACK[room]
            entries.append((title, spk, track, slugify(title)))

print(f"Total talks: {len(entries)}, speakers used: {speaker_idx}")

# ── DELETE OLD TALK FILES (keep 5 Auditorio Principal ones) ───────────────────
KEEP = {
    "apertura-pn26.md",
    "dialogo-alto-nivel-cooperacion.md",
    "panel-tecnologia-innovacion-grd.md",
    "dialogo-financiamiento-resiliencia.md",
    "clausura-pn26.md",
}

for f in glob.glob(os.path.join(TALKS_DIR, "*.md")):
    if os.path.basename(f) not in KEEP:
        os.remove(f)
print(f"Old talk files removed (kept {len(KEEP)} Auditorio Principal files)")

# ── WRITE TALK FILES ──────────────────────────────────────────────────────────
BODY_TEMPLATES = [
    "Esta sesión presenta los resultados de investigación y experiencias prácticas en el campo de {topic}. Los participantes podrán conocer metodologías, casos de estudio y recomendaciones aplicables al contexto colombiano de gestión del riesgo de desastres.",
    "La presentación aborda los avances más recientes en {topic}, con énfasis en su aplicabilidad para los actores del Sistema Nacional para la Gestión del Riesgo de Desastres. Se comparten lecciones aprendidas y se abren espacios de diálogo con los asistentes.",
    "Este espacio examina la relevancia de {topic} en el fortalecimiento de la resiliencia territorial colombiana. Se presentan evidencias empíricas, herramientas prácticas y propuestas de política pública para la toma de decisiones en los distintos niveles de gobierno.",
]

slug_count = {}
for title, speaker_str, track, slug_base in entries:
    slug_count[slug_base] = slug_count.get(slug_base, 0) + 1
    count = slug_count[slug_base]
    slug = slug_base if count == 1 else f"{slug_base}-{count}"
    filepath = os.path.join(TALKS_DIR, f"{slug}.md")

    # Extract speaker name (without title and institution)
    parts = speaker_str.split("·")
    speaker_name = parts[0].strip()
    # Remove title prefix (Dr., Ing., etc.)
    for pfx in ["Dra. ","Dr. ","Ing. ","MSc. ","Lic. ","PhD. "]:
        if speaker_name.startswith(pfx):
            speaker_name = speaker_name[len(pfx):]
            break

    # Short topic for body (first 4 words of title)
    topic_words = title.lower().split()[:5]
    topic = " ".join(topic_words)

    body_template = random.choice(BODY_TEMPLATES)
    body = body_template.format(topic=topic)

    safe_title = title.replace('"', '\\"')
    content = f"""---
name: "{safe_title}"
speakers:
  - {speaker_name}
track: {track}
---
{body}
"""
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(content)

print(f"Written {len(entries)} talk files to {TALKS_DIR}")

# ── WRITE program.yml ─────────────────────────────────────────────────────────
# Re-build mapping: (day, room, slot_idx) → title
title_map = {}
sp_idx = 0
for day in DAYS:
    for room, day_data in TALKS.items():
        titles = day_data[day]
        for slot_i, title in enumerate(titles):
            title_map[(day, room, slot_i)] = title

yml_lines = ["days:"]
for day in DAYS:
    abbr, date = DAY_META[day]
    yml_lines += [
        f"  - name: {day}",
        f"    abbr: {abbr}",
        f"    date: {date}",
        f"    rooms:",
        f'      - name: "Auditorio Principal"',
        f"        talks:",
    ]
    for t_name, t_start, t_end in AUDITORIO[day]:
        yml_lines += [
            f'          - name: "{t_name}"',
            f'            time_start: "{t_start}"',
            f'            time_end: "{t_end}"',
        ]
    yml_lines.append("")

    for room, day_data in TALKS.items():
        titles = day_data[day]
        yml_lines += [
            f'      - name: "{room}"',
            f"        talks:",
        ]
        for slot_i, title in enumerate(titles):
            t_start, t_end = SLOTS[slot_i]
            # Escape quotes in title
            safe = title.replace('"', '\\"')
            yml_lines += [
                f'          - name: "{safe}"',
                f'            time_start: "{t_start}"',
                f'            time_end: "{t_end}"',
            ]
        yml_lines.append("")

program_path = os.path.join(PROJECT, "_data", "program.yml")
with open(program_path, "w", encoding="utf-8") as fh:
    fh.write("\n".join(yml_lines) + "\n")

print(f"Written {program_path}")
print("Done!")
