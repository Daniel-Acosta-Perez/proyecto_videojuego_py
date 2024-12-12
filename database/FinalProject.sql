-- drop database videojuegosistema;
create database videojuegosistema;
use videojuegosistema;


create table jugadores(
    jug_ID int not null auto_increment,
    jug_nombre varchar (50),
    jug_nivel int,
    jug_puntuacion int, 
    jug_equipo varchar (50), 
    jug_inventario JSON,
    PRIMARY KEY(jug_ID));

create table partidas(
    par_ID int not null auto_increment,
    fecha datetime, 
    equipo1 varchar(20), 
    equipo2 varchar(20), 
    resultado varchar(15),
    PRIMARY KEY(par_ID));

create table mundo(
mun_ID int not null auto_increment,
grafo_serializado JSON,
PRIMARY KEY(mun_ID));

CREATE TABLE ranking (
ID_jugador INT NOT NULL,
puntuacion INT NOT NULL DEFAULT 0,
posicion INT NOT NULL,
PRIMARY KEY (ID_jugador),
FOREIGN KEY (ID_jugador) REFERENCES jugadores(jug_ID));

drop procedure insertJugadores;
delimiter //
create procedure insertJugadores()
BEGIN
INSERT INTO jugadores (jug_nombre, jug_nivel, jug_puntuacion, jug_equipo, jug_inventario)
VALUES 
('Ana', 11, 220, 'Equipo Negro', '{"items": ["Arco", "Flechas de fuego", "Poción de fuerza"], "oro": 450}'),
('Ana', 8, 250, 'Equipo Azul', '{"items": ["Arco", "Flechas", "Poción de vida"], "oro": 300}'),
('Carlos', 15, 1000, 'Equipo Verde', '{"items": ["Hacha", "Casco"], "oro": 500}'),
('Sofía', 12, 800, 'Equipo Rojo', '{"items": ["Bastón mágico", "Amuleto"], "oro": 400}'),
('Luis', 5, 100, 'Equipo Amarillo', '{"items": ["Daga", "Capa"], "oro": 50}'),
('Valeria', 18, 1200, 'Equipo Azul', '{"items": ["Lanza", "Escudo de fuego"], "oro": 600}'),
('Diego', 7, 300, 'Equipo Verde', '{"items": ["Martillo", "Armadura ligera"], "oro": 250}'),
('Mariana', 11, 450, 'Equipo Rojo', '{"items": ["Espada corta", "Botas rápidas"], "oro": 200}'),
('Fernando', 20, 1500, 'Equipo Amarillo', '{"items": ["Hacha pesada", "Guantes de poder"], "oro": 1000}'),
('Lucía', 14, 700, 'Equipo Azul', '{"items": ["Arco largo", "Capa invisible"], "oro": 350}');
END//
delimiter ;

delimiter //
create procedure updateJugador()
BEGIN
	update jugadores
    set jug_equipo = "Equipo negro"
    WHERE jug_ID = 2;
    
    update jugadores
    set jug_nivel = "20"
    WHERE jug_ID = 6;
    
    update jugadores
    set jug_nombre = "Manolo Jose"
    WHERE jug_ID = 7;
    
    update jugadores
    set jug_puntuacion = "340"
    WHERE jug_ID = 3;
    
    update jugadores
    set jug_nombre = "Galvan Bael"
    WHERE jug_ID = 5;
END//
delimiter ;

-- drop procedure deleteJugadores;

DELIMITER //

CREATE PROCEDURE deleteJugadores()
BEGIN
    DELETE FROM jugadores WHERE jug_ID = 9;
END //

DELIMITER ;

delimiter //

CREATE PROCEDURE seeJugador()
BEGIN
select * from jugadores;
END //

delimiter ; 

call insertJugadores();
call updateJugador();
call deleteJugadores();
call seeJugador();