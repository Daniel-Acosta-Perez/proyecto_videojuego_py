CREATE DATABASE IF NOT EXISTS videojuegosistema;
USE videojuegosistema;

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

-- Tabla de equipos
CREATE TABLE equipos (
    equipo_ID INT NOT NULL AUTO_INCREMENT,
    equipo_nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (equipo_ID)
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

-- Tabla de mundos
CREATE TABLE mundos (
    mun_ID INT NOT NULL AUTO_INCREMENT,
    grafo_serializado JSON NOT NULL,
    PRIMARY KEY (mun_ID)
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

-- Eliminar procedimiento previo si existe
DROP PROCEDURE IF EXISTS insertJugadores;
DELIMITER //

CREATE PROCEDURE insertJugadores()
BEGIN
    -- Insertar jugadores
    INSERT INTO jugadores (jug_nombre, jug_nivel, jug_puntuacion, equipo_ID)
    VALUES 
    ('Ana', 11, 220, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Negro')),
    ('Ana', 8, 250, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Azul')),
    ('Carlos', 15, 1000, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Verde')),
    ('Sofía', 12, 800, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Rojo')),
    ('Luis', 5, 100, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Amarillo')),
    ('Valeria', 18, 1200, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Azul')),
    ('Diego', 7, 300, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Verde')),
    ('Mariana', 11, 450, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Rojo')),
    ('Fernando', 20, 1500, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Amarillo')),
    ('Lucía', 14, 700, (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Azul'));

    -- Insertar inventarios
    INSERT INTO inventarios (jug_ID, item_nombre, item_descripcion) 
    VALUES 
    ((SELECT jug_ID FROM jugadores WHERE jug_nombre = 'Ana'), 'Arco', 'Arco largo con gran alcance'),
    ((SELECT jug_ID FROM jugadores WHERE jug_nombre = 'Ana'), 'Flechas de fuego', 'Flechas imbuidas con fuego'),
    ((SELECT jug_ID FROM jugadores WHERE jug_nombre = 'Ana'), 'Poción de fuerza', 'Poción que aumenta la fuerza'),
    ((SELECT jug_ID FROM jugadores WHERE jug_nombre = 'Carlos'), 'Hacha', 'Hacha afilada y resistente'),
    ((SELECT jug_ID FROM jugadores WHERE jug_nombre = 'Carlos'), 'Casco', 'Casco de metal de alta calidad'),
    -- Añadir más ítems para los demás jugadores
    ;
END //

DELIMITER ;

-- Eliminar procedimiento previo si existe
DROP PROCEDURE IF EXISTS updateJugador;
DELIMITER //

CREATE PROCEDURE updateJugador()
BEGIN
    -- Actualizar jugadores
    UPDATE jugadores
    SET equipo_ID = (SELECT equipo_ID FROM equipos WHERE equipo_nombre = 'Equipo Negro')
    WHERE jug_ID = 2;
    
    UPDATE jugadores
    SET jug_nivel = 20
    WHERE jug_ID = 6;
    
    UPDATE jugadores
    SET jug_nombre = 'Manolo Jose'
    WHERE jug_ID = 7;
    
    UPDATE jugadores
    SET jug_puntuacion = 340
    WHERE jug_ID = 3;
    
    UPDATE jugadores
    SET jug_nombre = 'Galvan Bael'
    WHERE jug_ID = 5;
END //

DELIMITER ;

-- Eliminar procedimiento previo si existe
DROP PROCEDURE IF EXISTS deleteJugadores;
DELIMITER //

CREATE PROCEDURE deleteJugadores()
BEGIN
    -- Eliminar jugador con ID = 9
    DELETE FROM jugadores WHERE jug_ID = 9;
END //

DELIMITER ;

-- Procedimiento para ver los jugadores
DELIMITER //

CREATE PROCEDURE seeJugador()
BEGIN
    SELECT 
        j.jug_ID,
        j.jug_nombre,
        j.jug_nivel,
        j.jug_puntuacion,
        e.equipo_nombre,
        i.item_nombre,
        i.item_descripcion
    FROM jugadores j
    JOIN equipos e ON j.equipo_ID = e.equipo_ID
    LEFT JOIN inventarios i ON j.jug_ID = i.jug_ID;
END //

DELIMITER ;

-- Ejecutar los procedimientos
CALL insertJugadores();
CALL updateJugador();
CALL deleteJugadores();
CALL seeJugador();
