import nltk
import unidecode
from nltk.chat.util import Chat, reflections

# Definir los patrones y respuestas del chatbot
pares = [
    [
        r".*(carreras|opciones).*(oferta|ofertadas|disponibles|ofrece|dispone|tiene).*",
        ["En el ITSUR ofrecemos las siguientes carreras: \n\n- Gastronomía\n- Ing. S. Automotrices\n- Ing. Ambiental\n- Ing. Sistemas C.\n- Ing. Industrial\n- Ing. Electrónica\n- Ing. Gestión Empresarial"]
    ],

    [
        r".*(carrera|información|info).*sistemas.*",
        ["La carrera de sistemas está actualmente especializada en Desarrollo web y aplicaciones móviles, si tienes más dudas puedes preguntarme de la carga académica de esta especialidad por semestre o solamente en general"]
    ],
    [
        r".*(materias|asignaturas).*primer semestre.*sistemas.*",
        ["Las materias del primer semestre son: \n\n- Cálculo diferencial\n- Fundamentos de Programación\n- Taller de Ética\n- Matemáticas Discretas\n- Taller de Administración\n- Fundamentos de Investigación\n- Tutoría I\n- Extracurriculares I"]
    ],
    [
        r".*(materias|asignaturas).*segundo semestre.*sistemas.*",
        ["Las materias del segundo semestre son: \n\n- Cálculo Integral\n- Programación Orientada a Objetos\n- Contabilidad Financiera\n- Química\n- Desarrollo Sustentable\n- Probabilidad y Estadística\n- Tutoría II\n- Extracurriculares II"]
    ],
    [
        r".*(materias|asignaturas).*tercer semestre.*sistemas.*",
        ["Las materias del tercer semestre son: \n\n- Cálculo Vectorial\n- Estructura de Datos\n- Cultura Empresarial\n- Álgebra Lineal\n- Sistemas Operativos\n- Física General\n- Servicio Social I\n- Inglés I"]
    ],
    [
        r".*(materias|asignaturas).*cuarto semestre.*sistemas.*",
        ["Las materias del cuarto semestre son: \n\n- Ecuaciones Diferenciales\n- Tópicos avanzados de Programación\n- Lenguaje y Autómatas I\n- Fundamentos de Bases de Datos\n- Taller de Sistemas Operativos\n- Principios Elec. y Aplic. Dig.\n- Inglés II"]
    ],
    [
        r".*(materias|asignaturas).*quinto semestre.*sistemas.*",
        ["Las materias del quinto semestre son: \n\n- Métodos Numéricos\n- Fundamentos de Telecomunicaciones\n- Lenguaje y Autómatas II\n- Taller de Bases de Datos\n- Fundamentos de Ing. de Software\n- Arquitectura de Computadoras\n- Inglés III"]
    ],
    [
        r".*(materias|asignaturas).*sexto semestre.*sistemas.*",
        ["Las materias del sexto semestre son: \n\n- Simulación\n- Redes de Computadoras\n- Graficación\n- Administración de Bases de Datos\n- Ingeniería de Software\n- Lenguajes de Interfaz\n- Actividad complementaria V\n- Inglés IV"]
    ],
    [
        r".*(materias|asignaturas).*séptimo semestre.*sistemas.*",
        ["Las materias del séptimo semestre son: \n\n- Programación y Lógica Funcional\n- Conmutación y Enrutamiento de Redes de Datos\n- Taller de Investigación I\n- Programación Web\n- Gestión de Proyectos de Software\n- Sistemas Programables\n- Programación Móvil I\n- Inglés V"]
    ],
    [
        r".*(materias|asignaturas).*octavo semestre.*sistemas.*",
        ["Las materias del octavo semestre son: \n\n- Inteligencia Artificial\n- Administración de Redes\n- Taller de Investigación II\n- Programación Web II\n- Programación Web III\n- Investigación de Operaciones\n- Programación Móvil II\n- Form. y eval. de proy. de inv."]
    ],
    [
        r".*(materias|asignaturas).*noveno semestre.*sistemas.*",
        ["El noveno semestre es el de Residencia Profesional. En este semestre se lleva a cabo la realización de la Residencia Profesional, un proyecto práctico en el ámbito laboral bajo la supervisión de un tutor académico."]
    ],
    [
        r".*(materias|asignaturas).*sistemas.*",
        ["Estas son las materias ofertadas en el ITSUR en la Ingeniería de Sistemas Computacionales: \n\n- Cálculo diferencial\n- Fundamentos de Programación\n- Taller de Ética\n- Matemáticas Discretas\n- Taller de Administración\n- Fundamentos de Investigación\n- Tutoría I\n- Extracurriculares I\n\n- Cálculo Integral\n- Programación Orientada a Objetos\n- Contabilidad Financiera\n- Química\n- Desarrollo Sustentable\n- Probabilidad y Estadística\n- Tutoría II\n- Extracurriculares II\n\n- Cálculo Vectorial\n- Estructura de Datos\n- Cultura Empresarial\n- Álgebra Lineal\n- Sistemas Operativos\n- Física General\n- Servicio Social I\n- Inglés I\n\n- Ecuaciones Diferenciales\n- Tópicos avanzados de Programación\n- Lenguaje y Autómatas I\n- Fundamentos de Bases de Datos\n- Taller de Sistemas Operativos\n- Principios Elec. y Aplic. Dig.\n- Inglés II\n\n- Métodos Numéricos\n- Fundamentos de Telecomunicaciones\n- Lenguaje y Autómatas II\n- Taller de Bases de Datos\n- Fundamentos de Ing. de Software\n- Arquitectura de Computadoras\n- Inglés III\n\n- Simulación\n- Redes de Computadoras\n- Graficación\n- Administración de Bases de Datos\n- Ingeniería de Software\n- Lenguajes de Interfaz\n- Actividad complementaria V\n- Inglés IV\n\n- Programación y Lógica Funcional\n- Conmutación y Enrutamiento de Redes de Datos\n- Taller de Investigación I\n- Programación Web\n- Gestión de Proyectos de Software\n- Sistemas Programables\n- Programación Móvil I\n- Inglés V\n\n- Inteligencia Artificial\n- Administración de Redes\n- Taller de Investigación II\n- Programación Web II\n- Programación Web III\n- Investigación de Operaciones\n- Programación Móvil II\n- Form. y eval. de proy. de inv.\n\n- Residencia Profesional"]
    ],
    [
        r".*inteligencia artificial.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales la capacidad de aplicar técnicas de Inteligencia Artificial mediante el desarrollo y programación de modelos matemáticos, estadísticos y de simulación a la solución de problemas complejos de control automático, diagnóstico, toma de decisiones, clasificación, minería de datos, es decir, problemas propios de la Inteligencia Artificial. "]
    ],
    [
        r".*administracion de redes.*",
        ["Esta asignatura proporciona dominio de las herramientas básicas para poder configurar y administrar servicios e infraestructuras de redes e implementar políticas de seguridad con el propósito de mejorar la fiabilidad y el desempeño de las mismas."]
    ],
    [
        r".*taller de investigacion ii.*",
        ["Ésta asignatura es parte del eje del investigación que apoya el proceso de titulación de los estudiantes del SNEST; corresponde al tercer momento de dicho eje. Ésta materia aporta elementos para que el futuro profesionista desarrolle habilidades que le permitan  la integración de un proyecto de investigación afín a su a carrera, sin pretender llegar a formarlo como científico. "]
    ],
    [
        r".*programacion web ii.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad de publicar sitios web de acuerdo a las necesidades requeridas, conocer la programación web del lado del servidor utilizando la técnica adecuada y aplicar nuevas tecnologías para la comunicación clienteservidor. "]
    ],
    [
        r".*programacion web iii.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad de desarrollar y administrar sistemas de información basados en tecnologías WEB, tomando en cuenta las principales cuestiones de seguridad, la arquitectura de los servicios, aplicando interfaces gráficas interactivas, los principios básicos de diseño visual general y considerando los elementos básicos de diseño responsive. "]
    ],
    [
        r".*investigacion de operaciones.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales  la capacidad para aplicar técnicas y modelos de investigación de operaciones en la solución de problemas, utilizando o desarrollando herramientas de software para la toma de decisiones. "]
    ],
    [
        r".*programacion movil ii.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad de desarrollar aplicaciones empresariales aplicando tecnologías móviles "]
    ],
    [
        r".*formulacion y evaluacion de proyectos de inversion.*",
        ["Esta asignatura contribuye al perfil de egreso con los conocimientos y herramientas necesarios para formular, evaluar y llevar a cabo proyectos de inversión o productivos con criterios de sustentabilidad, utilizando técnicas y métodos cualitativos y cuantitativos para la toma de decisiones con una visión directiva y empresarial en gestión. "]
    ],
    [
        r".*ayuda.*",
        ["Puedes preguntarme sobre las carreras ofertadas en el ITSUR o pedir información específica sobre alguna carrera en particular."]
    ],
    [
        r".*(gracias|adios).*",
        [
            "De nada.",
            "No hay problema.",
            "Estoy aquí para ayudar.",
            "¡Feliz de poder ayudar!",
            "Siempre a tu servicio."
        ]
    ],
    [
        r"(.*)",
        ["Lo lamento, no tengo una respuesta para eso, intenta de nuevo :c"]
    ]
]

# Convertir a minúsculas y eliminar acentos


def preprocess_text(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    return text

# Crear el chatbot


def crear_chatbot():
    print("¡Hola! Soy Chatito, el aistente del ITSUR. ¿En qué puedo ayudarte hoy?")
    chatbot = Chat(pares, reflections)
    # Sobrescribir método _preprocess para el procesamiento personalizado del texto
    chatbot._preprocess = preprocess_text
    chatbot.converse()


# Ejecutar el chatbot
crear_chatbot()
