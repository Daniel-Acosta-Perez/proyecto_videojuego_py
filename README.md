# Proyecto: Sistema de Videojuego Multijugador

## Descripción

Este proyecto es un sistema de videojuego multijugador desarrollado en Python utilizando un enfoque MVC (Modelo-Vista-Controlador). Proporciona funcionalidades para gestionar jugadores, equipos, mundos virtuales, partidas, rankings globales y consultas avanzadas.

## Funcionalidades Principales

### Gestión de Jugadores

- Crear, modificar, eliminar y listar jugadores.
- Asociar jugadores con equipos e inventarios personalizados.

### Gestión de Equipos

- Crear equipos y asignar jugadores.
- Consultar detalles de equipos junto con sus integrantes.

### Gestión de Mundos

- Crear mundos virtuales representados como grafos.
- Calcular rutas óptimas entre ubicaciones dentro del mundo.

### Gestión de Partidas

- Registrar partidas y sus resultados.
- Almacenar partidas en un árbol binario para consultas por fecha.

### Ranking Global

- Actualizar automáticamente el ranking global tras cada partida.
- Consultar el ranking global para ver a los jugadores mejor puntuados.

### Consultas y Análisis

- Listar partidas en un rango de fechas.
- Verificar el inventario de un jugador.
- Consultar estadísticas detalladas de jugadores (partidas jugadas, ganadas, perdidas).

## Tecnologías Utilizadas

- **Lenguaje**: Python
- **Bibliotecas**: Tkinter, MySQL Connector
- **Base de Datos**: MySQL
- **Estructuras de Datos**: Grafos, Árbol Binario

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/proyecto-videojuego.git
   ```
2. Instala los requisitos necesarios:
   ```bash
   pip install mysql-connector-python
   ```

# Nota: Tkinter está integrado en Python por defecto y no requiere instalación separada.

````
3. Configura la base de datos:
- Importa el archivo SQL proporcionado (`FinalProject.sql`) para crear las tablas necesarias.
- Ajusta las credenciales de la base de datos en `conexion_bd.py`.
  Ejemplo de configuración:
  ```python
  config = {
      'user': 'tu_usuario',
      'password': 'tu_contraseña',
      'host': 'localhost',
      'database': 'videojuego',
  }
  ``` Ajusta las credenciales de la base de datos en `conexion_bd.py`.

## Ejecución
1. Ejecuta el archivo `main.py` para iniciar el sistema:
```bash
python main.py
````

2. Interactúa con el menú principal para acceder a las distintas funcionalidades.

## Ejemplo de Flujo del Sistema

### Paso 1: Crear un Mundo Virtual
- El usuario accede a la funcionalidad de **Gestión de Mundos** desde el menú principal.
- Ingresa un nombre para el mundo y define ubicaciones iniciales.
- El sistema genera automáticamente un grafo inicial con las ubicaciones como nodos y sus conexiones como aristas.
- Las conexiones se almacenan en la base de datos.

### Paso 2: Mover Jugadores entre Ubicaciones
- Durante una partida, los jugadores eligen ubicaciones de origen y destino.
- El sistema calcula rutas óptimas entre estas ubicaciones utilizando el grafo generado.
- El jugador puede visualizar la ruta calculada y decidir el movimiento.

### Paso 3: Registrar una Partida
- Al finalizar una partida, el usuario accede a la funcionalidad de **Gestión de Partidas**.
- Se registran la fecha, los jugadores participantes y el resultado de la partida.
- Los datos se almacenan en un árbol binario (para consultas por fecha) y en la base de datos.

### Paso 4: Actualizar el Ranking Global
- Una vez registrada la partida, el sistema ejecuta automáticamente un procedimiento almacenado para actualizar el ranking global.
- Los jugadores se ordenan por puntuación en la tabla de ranking global, que puede consultarse desde su vista específica.

### Paso 5: Consultar Estadísticas y Análisis
- El usuario accede a la funcionalidad de **Consultas y Análisis**.
- Puede listar partidas por rango de fechas, verificar el inventario de jugadores y consultar estadísticas detalladas (partidas jugadas, ganadas y perdidas).

Este flujo garantiza que las principales funcionalidades del sistema estén completamente integradas y operativas.
2. **Mover jugadores**: Calcula rutas óptimas entre ubicaciones en el mundo.
3. **Registrar partida**: Los resultados de las partidas se almacenan en un árbol binario y en la base de datos.
4. **Actualizar ranking**: El ranking global se actualiza automáticamente tras registrar la partida.

## Estructura del Proyecto

```
proyecto_videojuego/
│
├── modelo/
│   ├── conexion_bd.py
│   ├── jugadores_modelo.py
│   ├── equipos_modelo.py
│   ├── mundos_modelo.py
│   ├── partidas_modelo.py
│   ├── ranking_modelo.py
│   ├── consultas_modelo.py
│
├── controlador/
│   ├── controlador_jugador.py
│   ├── controlador_equipos.py
│   ├── controlador_mundos.py
│   ├── controlador_partidas.py
│   ├── controlador_ranking.py
│   ├── controlador_consultas.py
│
├── vista/
│   ├── vista_jugador.py
│   ├── vista_equipos.py
│   ├── vista_mundos.py
│   ├── vista_partidas.py
│   ├── vista_ranking.py
│   ├── vista_consultas.py
│
├── main.py
├── README.md
```

## Contribuciones

1. Crea un fork de este repositorio.
2. Haz tus cambios en una rama separada:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Envía un pull request con una descripción detallada de los cambios.

## Créditos

- **Desarrollador**: Daniel Acosta
- **Contacto**: juan.acostaperez2@gmail.com

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

