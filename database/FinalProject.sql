CREATE DATABASE IF NOT EXISTS videojuegosistema;
USE videojuegosistema;
-- drop database videojuegosistema;
-- Tabla de equipos
CREATE TABLE equipos (
    equipo_ID INT NOT NULL AUTO_INCREMENT,
    equipo_nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (equipo_ID)
);


-- Tabla de jugadores
CREATE TABLE jugadores (
    jug_ID INT NOT NULL AUTO_INCREMENT,
    jug_nombre VARCHAR(50) NOT NULL,
    jug_nivel INT NOT NULL DEFAULT 1,
    jug_puntuacion INT NOT NULL DEFAULT 0, 
    equipo_ID INT,
    PRIMARY KEY (jug_ID),
    FOREIGN KEY (equipo_ID) REFERENCES equipos(equipo_ID)
);



-- Tabla de inventarios
CREATE TABLE inventarios (
    inventario_ID INT NOT NULL AUTO_INCREMENT,
    jug_ID INT NOT NULL,
    item_nombre VARCHAR(50) NOT NULL,
    item_descripcion VARCHAR(255),
    PRIMARY KEY (inventario_ID),
    FOREIGN KEY (jug_ID) REFERENCES jugadores(jug_ID)
);

-- Tabla de partidas
CREATE TABLE partidas (
    par_ID INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME NOT NULL, 
    equipo1_ID INT NOT NULL, 
    equipo2_ID INT NOT NULL, 
    resultado VARCHAR(15) NOT NULL,
    PRIMARY KEY (par_ID),
    FOREIGN KEY (equipo1_ID) REFERENCES equipos(equipo_ID),
    FOREIGN KEY (equipo2_ID) REFERENCES equipos(equipo_ID)
);


-- Tabla de rankings
CREATE TABLE ranking (
    rank_ID INT NOT NULL AUTO_INCREMENT,
    ID_jugador INT NOT NULL,
    puntuacion INT NOT NULL DEFAULT 0,
    posicion INT NOT NULL,
    PRIMARY KEY (rank_ID),
    FOREIGN KEY (ID_jugador) REFERENCES jugadores(jug_ID)
);

ALTER TABLE jugadores ADD COLUMN inventario TEXT;

INSERT INTO equipos (equipo_nombre) VALUES 
('Equipo Rojo'), 
('Equipo Azul'), 
('Equipo Verde'), 
('Equipo Prueba');


-- Tabla de mundos
CREATE TABLE mundos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de ubicaciones
CREATE TABLE ubicaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    mundo_id INT,
    FOREIGN KEY (mundo_id) REFERENCES mundos(id)
);

-- Tabla de conexiones entre ubicaciones
CREATE TABLE conexiones (
    origen_id INT,
    destino_id INT,
    distancia INT,
    PRIMARY KEY (origen_id, destino_id),
    FOREIGN KEY (origen_id) REFERENCES ubicaciones(id),
    FOREIGN KEY (destino_id) REFERENCES ubicaciones(id)
);

INSERT INTO mundos (nombre) VALUES ('Mundo1');

-- Inserta ubicaciones
INSERT INTO ubicaciones (nombre, mundo_id) VALUES ('Ubicacion1', 1);
INSERT INTO ubicaciones (nombre, mundo_id) VALUES ('Ubicacion2', 1);
INSERT INTO ubicaciones (nombre, mundo_id) VALUES ('Ubicacion3', 1);

-- Conectar ubicaciones
INSERT INTO conexiones (origen_id, destino_id, distancia) VALUES (1, 2, 5);
INSERT INTO conexiones (origen_id, destino_id, distancia) VALUES (2, 3, 3);
INSERT INTO conexiones (origen_id, destino_id, distancia) VALUES (1, 3, 10);

use viedeojuegosistema;
delete from conexiones;

SELECT * FROM ubicaciones;
SELECT * FROM conexiones;

SELECT c.origen_id, c.destino_id, c.distancia
FROM conexiones c;

UPDATE conexiones
SET distancia = 10
WHERE distancia IS NULL;

SELECT c.origen_id, c.destino_id, c.distancia
FROM conexiones c;

UPDATE conexiones
SET distancia = 10
WHERE distancia IS NULL;

SELECT c.origen_id, c.destino_id, c.distancia, u1.nombre AS origen, u2.nombre AS destino
FROM conexiones c
JOIN ubicaciones u1 ON c.origen_id = u1.id
JOIN ubicaciones u2 ON c.destino_id = u2.id;

DESCRIBE inventarios;
ALTER TABLE inventarios ADD COLUMN jugador_id INT NOT NULL;
ALTER TABLE inventarios ADD COLUMN objeto VARCHAR(255) NOT NULL;
ALTER TABLE inventarios DROP COLUMN jugador_id;


DROP TABLE IF EXISTS partidas;

CREATE TABLE partidas (
    par_ID INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME NOT NULL, 
    jugadores TEXT NOT NULL,
    resultado VARCHAR(15) NOT NULL,
    PRIMARY KEY (par_ID)
);
DROP TABLE IF EXISTS ranking;
CREATE TABLE ranking (
    jugador_ID INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    puntuacion INT NOT NULL DEFAULT 0,
    PRIMARY KEY (jugador_ID),
    FOREIGN KEY (jugador_ID) REFERENCES jugadores(jug_ID)
);


DELIMITER $$

CREATE PROCEDURE actualizar_ranking()
BEGIN
    -- Limpia la tabla ranking
    TRUNCATE TABLE ranking;

    -- Recalcula la puntuación total para cada jugador
    INSERT INTO ranking (jugador_ID, nombre, puntuacion)
    SELECT
        j.jugador_ID,
        j.nombre,
        COALESCE(SUM(
            CASE
                WHEN p.resultado LIKE CONCAT('%', j.nombre, '%') THEN 10 -- Suma 10 puntos si el jugador ganó
                ELSE 0
            END
        ), 0) AS puntuacion
    FROM jugadores j
    LEFT JOIN partidas p ON FIND_IN_SET(j.nombre, p.jugadores)
    GROUP BY j.jugador_ID, j.nombre
    ORDER BY puntuacion DESC;
END$$

DELIMITER ;
