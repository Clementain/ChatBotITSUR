import nltk
import unidecode
from nltk.chat.util import Chat, reflections

# Definir los patrones y respuestas del chatbot
pares = [
    [
        r".*(hola|buenos dias|buenas tardes|buenas noches).*",
        [
            "!hola!",
            "¿En qué te puedo ayudar hoy?",
            "¿Qué se te ofrece?",
            "¿Algo en lo que pueda ayudar?",
            "Hola, estoy a tu disposicion para brindarte información"
        ]
    ],
    [
        r".*(ubicacion|donde se encuentra|calle|direccion).*",
        ["DIRECCIÓN DEL PLANTEL:\nAv. EducaciÓn Superior #2000,\nCol. Benito Juárez.\nUriangato, Gto.\nC.P. 38980"]
    ],
    [
        r".*Cuantos alumnos?.*",
        ["Actualmente hay 1712 alumnos inscritos al ITSUR en alguna de sus 7 carreras"]
    ],
    [
        r".*(directorio|contacto).*",
        ["Claro, al tener varias áreas, es mejor que te proporcione el link al directorio para que encuentres lo que busques:\nhttp://www.itsur.edu.mx/directorio.php/"]
    ],
    [

        r".*(horario de atencion|horarios).*",
        ["De lunes a viernes en horario continuo de 8:00a.m. a 04:00p.m"]
    ],
    [
        r".*(ficha|tramitar ficha|fichas|inscripcion).*",
        ["Si deseas inscribirte o sacar una ficha para postularte al ITSUR, revisa frecuentementa las convocatorias en nuestra página oficial o ponte en contacto:\n 445 458 8278, 445 457 7468 al 71, 445 458 8311, 445 458 8312 ext. *116\n445 106 6007 fichas@itsur.edu.mx\nAv. Educación Superior No. 2000, Col. Juárez, Uriangato, Gto. C.P. 38982\nTodos los derechos reservados © ITSUR 2023\nDe igual forma puedes acceder a esta página para ver cual es el proceso de sacar una ficha:\nhttps://fichas.surguanajuato.tecnm.mx/"]
    ],
    [
        r".(cuales|que)?.(son)?.*(carreras|opciones).*(oferta|ofertadas|disponibles|ofrece|dispone|tiene)?.*",
        ["En el ITSUR ofrecemos las siguientes carreras: \n\n- Gastronomía\n- Ing. S. Automotrices\n- Ing. Ambiental\n- Ing. Sistemas C.\n- Ing. Industrial\n- Ing. Electrónica\n- Ing. Gestión Empresarial"]
    ],
    [
        r".*fecha limite*",
        ["Actualmente la fecha limite para inscripción para el examen de admisión es el 31 de Mayo del 2023"]
    ],
    [
        r".*(carrera|informacion|info).*sistemas.*",
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
    # Materias de primer semestre sistemas
    [
        r".*calculo diferencial.*",
        ["En el Cálculo diferencial el estudiante adquiere los conocimientos necesarios para afrontar con éxito cálculo integral, cálculo vectorial, ecuaciones diferenciales, asignaturas de física y ciencias de la ingeniería. Además, encuentra, también, los principios y las bases para el modelado matemático."]
    ],
    [
        r".*fundamentos de programacion.*",
        ["Esta asignatura aporta, al perfil del ingeniero, la capacidad para desarrollar un pensamiento lógico, identificar el proceso de creación de un programa y desarrollo de algoritmos para resolver problemas."]
    ],
    [
        r".*taller de etica.*",
        ["En el Modelo del Siglo XXI del SNEST se busca una formación profesional que  integre, en una totalidad dinámica, la competencia en el quehacer profesional con el ejercicio de una ciudadanía activa, responsable  y el desarrollo psicosocial de la persona. "]
    ],
    [
        r".*matematicas discretas.*",
        ["Esta asignatura aporta al perfil del egresado  los conocimientos matemáticos para entender, inferir, aplicar y desarrollar modelos matemáticos tendientes a resolver problemas en el área de las ciencias computacionales.\nEsta materia es el soporte para un conjunto de asignaturas que se encuentran vinculadas directamente con las competencias profesionales que se desarrollarán, por lo que se incluye en los primeros semestres de la trayectoria escolar. Aporta conocimientos a las materias de Estructura de Datos y Redes de Computadoras con los conceptos básicos de Grafos y Árboles. "]
    ],
    [
        r".*taller de administracion.*",
        ["Esta asignatura aporta al perfil del Ingeniero en sistemas computacionales la capacidad de coordinar y participar en proyectos interdisciplinarios y una visión empresarial para detectar áreas de oportunidad que le permitan emprender y desarrollar proyectos aplicando las tecnologías de la información y comunicación. "]
    ],
    [
        r".*fundamentos de investigacion.*",
        ["El programa de la asignatura de Fundamentos de investigación, está diseñado para contribuir en la formación integral de los estudiantes del Sistema Nacional de Educación Superior Tecnológica (SNEST) porque desarrolla las competencias investigativas que se utilizarán para el aprendizaje conceptual, procedimental y actitudinal contenidos en los planes de estudio de las carreras que oferta. "]
    ],
    # Materias de segundo semestre sistemas
    [
        r".*calculo integral.*",
        ["Esta asignatura contribuye a desarrollar un pensamiento lógico, heurístico y algorítmico al modelar fenómenos y resolver problemas en los que interviene la variación. "]
    ],
    [
        r".*(programacion orientada a objetos|poo).*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales la capacidad de analizar, desarrollar, implementar y administrar software de aplicación orientado a objetos, cumpliendo con estándares de calidad, con el fin de apoyar la productividad y competitividad de las organizaciones. "]
    ],
    [
        r".*contabilidad.*",
        ["Esta asignatura aporta al perfil del egresado los conocimientos básicos de contabilidad e información financiera como una herramienta para la toma de decisiones; además de ser parte fundamental para las materias afines con temas de emprendedores que serán vistas en cursos posteriores."]
    ],
    [
        r".*quimica.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Electrónica Ingeniero  Electrico, Ingeniero Mecatrónico Ingeniero Electromecánico  la capacidad para analizar fenómenos químicos y eléctricos involucrados en el y comportamiento de diferentes tipos de materiales."]
    ],
    [
        r".*desarrollo sustentable.*",
        ["La intención de esta asignatura es que el egresado adopte valores y actitudes humanistas, que lo lleven a vivir y ejercer profesionalmente de acuerdo con principios orientados hacia la sustentabilidad, la cual es el factor medular de la dimensión filosófica del SNEST."]
    ],
    [
        r".*probabilidad y estadistica.*",
        ["Esta asignatura aporta al perfil del egresado los conocimientos matemáticos adquiridos en esta materia proveen al futuro profesionista las competencias que le permitan entender, aplicar y desarrollar modelos matemáticos utilizando técnicas de probabilidad y estadística, para el análisis de información y toma de decisiones en las diferentes áreas de las ciencias computacionales. "]
    ],
    # Materias de tercer semestre sistemas
    [
        r".*calculo vectorial.*",
        ["En diversas aplicaciones de la ingeniería, la concurrencia de variables espaciales y temporales, hace necesario el análisis de fenómenos naturales cuyos modelos originan funciones vectoriales o escalares de varias variables. Se diseña esta asignatura con el fin de proveer al alumno de herramientas para analizar estas funciones de tal manera que se pueda predecir o estimar su comportamiento, y estudiar conceptos relacionados con ellas; haciendo hincapié en la interpretación geométrica siempre que sea posible. "]
    ],
    [
        r".*estructura de datos.*",
        ["La importancia de la materia radica en que aporta al perfil del egresado el conocimiento, la correcta selección y aplicación de las estructuras de datos en la solución de problemas, así como el determinar la eficiencia  de algoritmos que permitan la selección de los mismos con el fin de desarrollar soluciones eficientes."]
    ],
    [
        r".*cultura empresarial.*",
        ["Esta materia es transversal a la carrera de Ingeniería en Sistemas Computacionales porque en la actualidad todo profesionista debe ser capaz de ofrecer y vender sus servicios de manera autónoma."]
    ],
    [
        r".*algebra lineal.*",
        ["El álgebra lineal aporta, al perfil del ingeniero, la capacidad para desarrollar un pensamiento lógico, heurístico y algorítmico al modelar fenómenos de naturaleza lineal y resolver problemas."]
    ],
    [
        r".*sistemas operativos.*",
        ["Esta asignatura desempeña un papel fundamental en el plan de estudio de estas ingenierías porque a través de ella el estudiante conoce en detalle los componentes, las estructuras y las funciones de un sistema operativo concreto, así como aspectos generales de la construcción de sistemas operativos."]
    ],
    [
        r".*fisica general.*",
        ["El ingeniero en Sistemas Computacionales tendrá las herramientas necesarias para poder interactuar con profesionales en otros campos del saber, para que de ésta manera solucione problemas con bases cimentadas en la Física y poder afrontar los retos actuales del desarrollo tecnológico."]
    ],
    # Materias de cuarto semestre sistemas
    [
        r".*ecuaciones diferenciales.*",
        ["El curso de ecuaciones diferenciales es un campo fértil de aplicaciones ya que una ecuación diferencial describe la dinámica de un proceso; el resolverla permite predecir su comportamiento y da la posibilidad de analizar el fenómeno en condiciones distintas."]
    ],
    [
        r".*topicos avanzados de programacion.*",
        ["Esta materia aporta al perfil la competencia para desarrollar soluciones de software utilizando programación concurrente, programación de eventos, que soporte interfaz gráfica y comunicación con dispositivos móviles."]
    ],
    [
        r".*lenguajes y automatas i.*",
        ["Análisis y síntesis para la solución de un problema: dado un problema, proponer el mejor lenguaje que se ajusta a las especificaciones del mismo. Si no hay lenguaje disponible, proponer las características del lenguaje ideal para el problema a resolver."]
    ],
    [
        r".*fundamentos de base de datos.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad de administrar proyectos que involucren tecnologías de información en las organizaciones conforme a requerimientos establecidos. Diseñar, desarrollar y mantener sistemas de bases de datos asegurando la integridad, disponibilidad y confidencialidad de la información almacenada. Desarrollar e implementar sistemas de información para el control y la toma de decisiones utilizando metodologías basadas en estándares internacionales."]
    ],
    [
        r".*taller de sistemas operativos.*",
        ["El estudiante obtendrá las habilidades y el conocimiento práctico para seleccionar, instalar, configurar, administrar, optimizar y utilizar diferentes sistemas operativos para lograr un uso más eficiente y de acuerdo a las necesidades de cualquier organización."]
    ],
    [
        r".*principios electricos y aplicaciones digitales.*",
        ["Principios eléctricos y aplicaciones digitales, es una materia que aporta al perfil del Ingeniero en Sistemas Computacionales conocimientos y habilidades básicas para identificar y comprender las tecnologías de hardware así como proponer, desarrollar y mantener aplicaciones eficientes, diseñar e implementar interfaces hombre- máquina y máquina-máquina para la automatización de sistemas, integrar soluciones computacionales con diferentes tecnologías, plataformas o dispositivos."]
    ],
    # Materias de quinto semestre sistemas
    [
        r".*metodos numericos.*",
        ["Esta asignatura aporta al perfil del ingeniero la capacidad de aplicar métodos numéricos en la resolución de problemas de la ingeniería y  la ciencia auxiliándose del uso de computadoras."]
    ],
    [
        r".*fundamentos de telecomunicaciones.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad de identificar y analizar los elementos de un sistema de comunicación para el diseño eficiente de redes."]
    ],
    [
        r".*lenguajes y automatas ii.*",
        ["En esta asignatura se debe desarrollar el análisis semántico, la generación de código, la optimización y la generación del código objeto para obtener el funcionamiento de un compilador."]
    ],
    [
        r".*taller de base de datos.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales las competencias para  diseñar y desarrollar bases de datos conforme a los requerimientos definidos, las normas organizacionales de manejo y seguridad de la información, utilizando tecnologías emergentes con el fin de integrar soluciones computacionales con diferentes tecnologías, plataformas o dispositivos considerando los aspectos legales, éticos, sociales y de desarrollo sustentable."]
    ],
    [
        r".*fundamentos de ingenieria de software.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales los conceptos básicos relacionados con el desarrollo de sistemas, los tipos de modelos para el desarrollo y gestión de software considerando la calidad, lo que permite integrar soluciones computacionales con diferentes tecnologías en diversas áreas."]
    ],
    [
        r".*arquitectura de computadoras.*",
        ["Arquitectura de Computadoras es una materia que por la importancia de su contenido y aplicación, aporta al perfil del Ingeniero en Sistemas Computacionales conocimientos y habilidades que le permitan comprender el funcionamiento interno de las computadoras y la evolución tecnológica del hardware. "]
    ],
    # Materias de sexto semestre sistemas
    [
        r".*simulacion.*",
        ["La asignatura de Simulación aporta al perfil del Ingeniero en Sistemas  Computacionales la habilidad de establecer modelos de simulación que le permitan analizar el comportamiento de un sistema real, así como la  capacidad  de  seleccionar y aplicar herramientas matemáticas para el modelado, diseño y desarrollo de tecnología computacional."]
    ],
    [
        r".*redes de computadoras.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales la capacidad de conocer, analizar y aplicar los diversos componentes tanto físicos como lógicos involucrados en la planeación, diseño e instalación de las redes de computadoras."]
    ],
    [
        r".*graficacion.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computaciones la capacidad para diseñar modelos gráficos que coadyuven su implementación en  diversas áreas, tales como: Desarrollo de aplicaciones web y el diseño de agentes inteligentes que requieran el trazado de objetos bidimensionales y tridimensionales, así como, su adecuada manipulación y visualización."]
    ],
    [
        r".*administracion de base de datos.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales la capacidad para administrar sistemas de bases de datos observando  las normas internacionales de manejo y seguridad de la información, utilizando para ello herramientas y metodologías especializadas en el manejo de grandes volúmenes de información, con el propósito de integrar soluciones computacionales con diferentes tecnologías, plataformas y dispositivos, basadas en sistemas de bases de datos, observándose siempre en el desempeño de sus actividades profesionales considerando los aspectos legales, éticos, sociales y de desarrollo sustentable. "]
    ],
    [
        r".*ingenieria de software.*",
        ["Esta asignatura aporta al perfil del Ingeniero en Sistemas Computacionales las competencias profesionales para aplicar métodos y técnicas que permitan desarrollar soluciones de software, conforme a las  normas organizacionales de manejo y seguridad de la información, utilizando tecnologías emergentes."]
    ],
    [
        r".*lenguajes de interfaz.*",
        ["La presente asignatura aporta al perfil del Ingeniero en Sistemas Computacionales los conocimientos para el diseño e implementación de interfaces hombre-máquina y máquina-máquina para la automatización de sistemas. "]
    ],
    [
        r".*actividad complementaria v.*",
        ['Generalmente esta materia puede varias dependiendo de los maestros, te sugiiero que contactes con el coordinador de ésta carrera:\nIng. Miguel Cruz Pineda\nCoordinación de Sistemas, Edificio "B" Planta Alta\nTel. (445) 457-74-68 al 71 Ext. *107\nsistemas@itsur.edu.mx']
    ],
    # Materias de septimo semestre sistemas
    [
        r".*programacion logica y funcional.*",
        ["La asignatura de Programación Lógica y Funcional aporta al perfil del Ingeniero en Sistemas Computacionales la capacidad de desarrollar habilidades para la generación de soluciones automatizadas basadas en lenguajes de inteligencia artificial, considerando el entorno y la aplicación de diversas técnicas, herramientas y conocimientos. "]
    ],
    [
        r".*conmutacion y enrutamiento en redes de datos.*",
        ["Esta asignatura aporta al perfil del Ingeniero en sistemas computacionales las capacidades básicas  para el diseño e implementación de soluciones en redes de datos LAN y WAN en base a las normas y estándares vigentes de la industria.\nLa importancia de esta asignatura radica en la necesidad que tienen las empresas de optimizar sus procesos con el adecuado aprovechamiento de las tecnologías de la información, empleando redes de datos como la infraestructura que soporta dichas tecnologías."]
    ],
    [
        r".*taller de investigacion i.*",
        ["La formación de ingenieros en un mundo globalizado requiere del dominio de herramientas básicas de investigación, que los capacite para gestionar la información y para accesar a la sociedad del conocimiento, dado que, ya no es suficiente acumular información sino transformarla, de manera que, pueda ser transferida y aplicada a diferentes contextos de manera sustentable."]
    ],
    [
        r".*programacion web.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad para desarrollar e implementar sistemas de información en ambiente web para la automatización de procesos y toma de decisiones utilizando metodologías basadas en estándares internacionales y tecnologías emergentes, introduciéndonos a la arquitectura de las aplicaciones web, los conceptos básicos del lenguaje de marcas, al lenguaje de presentación de datos, al desarrollo de código de lado cliente y servidor e implementación de servicios web."]
    ],
    [
        r".*gestion de proyectos de software.*",
        ["La asignatura de Gestión de proyectos de software, proporciona al alumno los conceptos que requiere y que debe contemplar para la gestión o administración de un proyecto de software. Por otro lado, le da la posibilidad de poner en práctica dicha gestión, ya que se sugiere que en esta asignatura, el alumno desarrolle un proyecto de gestión de software para una empresa real, adquiriendo las competencias necesarias para estar al frente de dichos proyectos. "]
    ],
    [
        r".*sistemas programables.*",
        ["Sistemas programables aporta al perfil del Ingeniero en sistemas computacionales, la capacidad de diseñar  e implementar interfaces hombre- máquina y máquinamáquina para la automatización de sistemas, integrar soluciones computacionales con diferentes tecnologías, plataformas o dispositivos. "]
    ],
    [
        r".*programacion movil i.*",
        ["Esta asignatura aporta al perfil del egresado la capacidad de desarrollar y administrar sistemas de información vinculados a dispositivos móviles conforme a requerimientos establecidos, teniendo en cuenta las principales cuestiones de seguridad al momento de desarrollar sus aplicaciones. Conocer la arquitectura de programación para dispositivos móviles y considerar los principios básicos de diseño visual al momento de desarrollar sus aplicaciones."]
    ],
    # Materias de octavo semestre sistemas
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
    # Materias de noveno (residencias)
    [
        r".*(residencias|residencias profesionales).*",
        ["Es una estrategia educativa de carácter curricular, que permite al estudiante emprender un proyecto teórico-practico, analítico, reflexivo, crítico y profesional; con el propósito de resolver un problema específico de la realidad social y productiva, para fortalecer y aplicar sus competencias profesionales.\nEl proyecto de Residencia Profesional puede realizarse de manera individual, grupal o interdisciplinaria; dependiendo de los requerimientos, condiciones y características del proyecto de la empresa, organismo o dependencia."]
    ],
    # Ingles
    [
        r".*niveles.*ingles.*",
        ["Contamos con 10 niveles de acrerditación que llegan hasta B1, esto para estudiantes y para externos ofrecemos 12 niveles"]
    ],
    [
        r".*?ingles.*",
        ["Estando en cualquier carrera, debes de tener por minimo 5 niveles acreditados de inglés para liberar/hacer tu servicio social y 10 niveles para poder hacer tus residencias profesionales"]
    ],
    # Tutorias
    [
        r".*(tutoria|tutorias).*",
        ["Tutoría es el proceso de acompañamiento personalizado que un académico (docente - tutor) realiza a un alumno principalmente durante el primer año de su trayectoria escolar, a fin de coadyuvar al logro de los objetivos educativos establecidos en el programa académico en que está inscrito y ayudarle perfilar su proyecto de vida. El alumno y su tutor estarín en comunicación constante para prever problemas de tipo académico y orientar la vida estudiantil hacia una vida profesional a través del desarrollo de hábitos de estudio, la reflexión participativa y la práctica de los valores éticos que desencadenan en una convivencia social armoniosa."]
    ],
    # extracurriculaes
    [
        r".*extracurriculares.*",
        ['Las actividades extracurriculares o "extra-clase" son la herramienta efectiva en la formación del alumnado, así como para su desarrollo personal a través de sus capacidades físicas y para el manejo adecuado de sí mismo en su entorno, permitiendo la interacción de los aspectos sociales.\nCon esta finalidad, se considera básico trabajar dos tipos de actividades extracurriculares las cuales son: Actividades Culturales y Deportivas en las que a través de talleres, torneos, concursos y otros eventos, se sensibiliza sobre la importancia del cuidado de la salud y se orienta sobre aspectos de interés general que los y las alumnas deben enfrentar en su vida cotidiana.\nTalleres Deportivos.- Beisbol, Basquetbol, Futbol Soccer, KarateDo, Zumba, Baile Moderno, Porristas, Gimnasio-Pesas y Acrobacias.\nTalleres Culturales.- Ajedrez, Banda de Guerra, Banda de Viento, Danza Folklórica, Baile de Salón, Escolta de Bandera, Rondalla, Teatro y Artes.']
    ],
    # Servicio social
    [
        r".*servicio social.*",
        ["Es la actividad de carácter temporal y obligatoria que institucionalmente ejecuten y presten los y las estudiantes a beneficio de la sociedad y el Estado.\nObjetivo del Servicio Social:\nDesarrollar en el y la prestadora una conciencia de solidaridad y compromiso con la sociedad a la que pertenece, convirtiéndose en un verdadero vínculo de reciprocidad para con la misma, a través de los planes y programas del sector público, contribuyendo a la formación académica y capacitación profesional del prestador del Servicio Social."]
    ],
    [
        r".*costo de fichas de admision.*",
        ["Las fichas de admision para nuevos aspirantes tiene el costo de 700 pesos"]
    ],
    [
        r".*documentos.*.*(inscripcion|inscribirme|admision).*",
        ["Constancia del último semestre de bachillerato o Certificado de Bachillerato(formato pdf)\nActa de nacimiento(formato pdf)\n CURP(formato pdf)\nComprobante de domicilio(formato pdf)\nComprobante SUREDSU(formato pdf)\nFoto o selfie tomada completamente de frente, con el rostro serio, frente descubierta, a la altura de los hombros y fondo blanco o en un color claro (formato jpg o png) "]
    ],
    [
        r".*descuentos.*.*beca.*convenio.*",
        ["Claro! existen becas que relizan un descuento en las inscripciones, pregunta en servicios escolares para una informacion actualizada"]
    ],
    [
        r".*(ayuda|informacion).*",
        ["Puedes preguntarme sobre las carreras ofertadas en el ITSUR o pedir información específica sobre alguna carrera en particular."]
    ],
    # Otros idiomas
    [
        r".*otros idiomas.*",
        ["En el centro de idiomas se ofertan otros idiomas si se llega al cupo mínimo, entre estas están frances, japones, si se requiere saber más favor de comunicarse al siguiente correo: idiomas@itsur.edu.mx "]
    ],
    [
        r".*?(pagos|pago|pagar).*?(constancia|constancias|titulo).*?",
        ["Los pagos de cualquier tipo se realizan en la oficina de tesoreria en el horario de atención de 9:00 am a 4:00pm"]],
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
