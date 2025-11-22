# Sistema de Gestión de Correos en Python
Este proyecto simula un sistema simple de mensajería (entre usuarios) utilizando programación orientada a objetos. Incluye funciones para poder enviar, recibir, listar y organizar mensajes en carpetas que corresponden a una bandeja de entrada.

# Descripción
El sistema simula el comportamiento de un servidor de correo y la interacción de sus usuarios. Cada usuario puede enviar y recibir mensajes, los cuales se almacenan en carpetas específicas. El diseño está basado en principios de abstracción, encapsulamiento y herencia.

# Tecnologías utilizadas
- Python 3.x
- Programación orientada a objetos (OOP)
- Módulo `abc` para clases abstractas

# Estructura del proyecto
- GestionCorreo: Interfaz abstracta que define los métodos esenciales para la gestión de correos.
- ServidorCorreo: Clase que representa el servidor, gestiona usuarios registrados.
- Usuario: Implementa la interfaz `GestionCorreo`, representa un usuario con su email y carpetas.
- Mensaje: Clase que modela un mensaje con emisor, destinatarios, asunto y contenido.
- Carpeta: Clase que gestiona los mensajes dentro de una carpeta específica.

# Proceso de elaboración del programa.
1. Inconvenientes para acceder al repositorio remoto para que cada uno pueda trabajar y visualizar el codigo del compañero.
2. Se trabajó en archivos diferentes (individuales) hasta poder reunir el codigo en el repositorio.
3. Durante el primer día se estableció la base principal del codigo, este incluia las distintas clases a utilizar (GestionCorreo(interfaz), ServidorCorreo, Usuario, Mensaje, Carpeta).
4. Posteriormente se implementaron los atributos y los distintos metodos para cada clase.
5. Una vez concluida la estructuración del código se paso a la fase de elaboración del diagrama en base al codigo para poder visualizar la relación entre las clases.

2º Entrega
1. Se importó la clase Mensaje e implementó el arbol de carpetas dentro de la clase Carpeta que permite la adición de subcarpetas ("carpetas hijas").
2. Se utilizó un metodo para mover mensajes entre carpetas y buscar mensajes recursivamente de manera tal que busque desde la primer carpeta hasta la ultima mediante filtros (asunto y correo del emisor)
3. Se corrigieron los errores en los metodos recursivos, se cambio el parametro "mensaje" por "texto" para que sea más especifico y claro sobre lo que trabaja. 
4. En la recursividad de buscar_msjs habia un error de accesos en la propiedad .asunto, .mensaje y .emisor, el cual ya fue solucionado eliminando los "__". 
5. Considerando los casos limites, cuando el usuario ingrese un parametro que no es un string, el programa lanzará un error, esto se soluciono con la adición del metodo "isinstance" para que la busqueda funcione correctamente transformando aquellos None, numero (354, 2, 3), listas, etc, en cadenas de texto. Por ejemplo: (123) = ("123).
6. Con respecto al movimiento de mensajes, implementamos un caso base para que el metodo empiece a recorrer las carpetas y sus subC con el fin de encontrar un mensaje. Por otro lado, para evitar errores se utilizo el metodo "isinstance" para verificar que un parametro corresponda con lo existencia de mensajes y/o carpetas. Esto hace que, si el usuario ingresa un mensaje o carpeta no válido, se le comunique el error.

3º Entrega
1. Como los filtros tienen que ser definidos por el usuario se consideró que sus metodos esten en la clase USUARIO.ç
2. El planteo esta basado en dejar tres carpetas iniciales: "inbox", "enviados", "papelera", posteriormente se pueden agregar más. El más importante de estos la carpeta "inbox", que será utilizado en los metodos "filtro" como base, lugar donde llegarán inicialmente los mensajes.
3. Para los metodos de filtrado de palabras se utilizo un diccionario vacio para que el usuario pueda acceder y localizar filtros de forma más clara. Se utilizó el metodo "agg_filtros" mediante el cual el user coloque que palabras clave irán a que carpeta especificas. El primer problema a resolver fue la busqueda de carpetas destino a la que el usuario le añada la palabra clave a filtrar, para ello utilizamos if y raise.
4. Para el siguiente metodo (mostrar los filtros añadidos) primero se comprueba si hay filtros ya añadidos, en el caso de que no los haya se notifica y en el caso de que haya se sigue con el metodo: tomar la palabra clave y la carpeta filtrada para luego imprimirlas. 
5. Además se incorporó la opción de eliminar un filtro que haya agregado el user, utilizando if para ver si se encuentra y el metodo del, que permitirá eliminar la palabra clave filtrada del diccionario de filtros. 
6. Para concluir se modificó el metodo recibir msjs ya que inicialmente la recepción base es en la carpeta "inbox" para luego tomar la palabra clave y modificar la carpeta a la que va a ir la misma.
7. Para agregar mensajes como urgentes y mostrarlos en primer lugar necesitamos crear una nueva lista en la que se van a alojar aquellos recibidos que en su ASUNTO tiene contenido "urgente". Estos van a ser dos metodos, el primero se va a encargar de revisar los mensajes y, si corresponden, meterlos en la lista de urgentes para posteriormente imprimirlos en el segundo metodo (listar) que fue modificado con esta ultima implementación.  

entrega final
1.Se redistribuyeron los archivos a la carpeta entrega final para tener mejor organizacion.
2.Se creo el archivo grafo donde se establece la red de servidores de correo a través de la forma de un grafo. Cada servidor se considera un nodo, mientras que cada enlace entre los servidores representa una arista del grafo.
El grafo tiene una estructura interna (diccionario) que guarda los servidores y sus conexiones.
El archivo contiene métodos para agregar servidores y conectarlos, métodos bfs() y dfs() que encuentran caminos entre servidores.
y Un método enviar_por_red() que simula el envío de un mensaje recorriendo la red.
En resumen se agrega la lógica de comunicación entre servidores.
3. Se implementó una interfaz creando un archivo "menu.py" con sus respectivos FROM para que herede los datos, metodos que necesita el menu. Este permitirá al usuario navegar entre distintas opciones para que importe o extraiga la información necesaria.