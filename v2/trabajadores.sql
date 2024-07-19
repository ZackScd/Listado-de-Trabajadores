--Creacion de Tablas 
CREATE DATABASE ListaTrabajadores;

USE ListaTrabajadores; 

CREATE TABLE cargos (
    cargoid INT PRIMARY KEY AUTO_INCREMENT,
    cargo VARCHAR(100)
);

CREATE TABLE contactosemergencia (
    rut VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(100),
    relacioncontrabajador VARCHAR(50),
    contacto VARCHAR(20)
);

CREATE TABLE cargasfamiliares (
    rut VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(100),
    sexo CHAR(1),
    parentescoid INT,

    FOREIGN KEY (parentescoid) REFERENCES parentezcos(id)
);

CREATE TABLE parentezcos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    parentesco VARCHAR(50)
);

CREATE TABLE trabajadorescargas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ruttrabajador VARCHAR(12),
    rutcarga VARCHAR(12),

    FOREIGN KEY (ruttrabajador) REFERENCES trabajadores(rut),
    FOREIGN KEY (rutcarga) REFERENCES cargasfamiliares(rut)
);

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ruttrabajador VARCHAR(12) UNIQUE,
    nombreusuario VARCHAR(50),
    contrasena VARCHAR(100),
    cargo VARCHAR(50),
    
    FOREIGN KEY (ruttrabajador) REFERENCES trabajadores(rut)
);

CREATE TABLE trabajadores (
    rut VARCHAR(12) PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    sexo CHAR(1),
    cargoid INT,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    fechaingreso DATE,
    contactoemergenciarut VARCHAR(12),
    usuarioid INT UNIQUE,

    FOREIGN KEY (cargoid) REFERENCES cargos(cargoid),
    FOREIGN KEY (contactoemergenciarut) REFERENCES contactosemergencia(rut),
    FOREIGN KEY (usuarioid) REFERENCES usuarios(id)
);

--Inserción de datos Dummy
INSERT INTO trabajadores (rut, nombres, apellidos, sexo, cargoid, direccion, telefono, fechaingreso, contactoemergenciarut, usuarioid)
VALUES ('12345678-9', 'Juan', 'Pérez', 'M', 1, 'Calle Falsa 123', '123456789', '2022-01-01', '87654321-0', 1);

INSERT INTO cargos (cargo)
VALUES ('Gerente');

INSERT INTO contactosemergencia (rut, nombre, relacioncontrabajador, contacto)
VALUES ('87654321-0', 'María Gómez', 'Esposa', '987654321');

INSERT INTO cargasfamiliares (rut, nombre, sexo, parentescoid)
VALUES ('98765432-1', 'Juanita Pérez', 'F', 1);

INSERT INTO parentezcos (parentesco)
VALUES ('Hija');

INSERT INTO trabajadorescargas (ruttrabajador, rutcarga)
VALUES ('12345678-9', '98765432-1');

INSERT INTO usuarios (ruttrabajador, nombreusuario, contrasena, cargo)
VALUES ('12345678-9', 'juanperez', SHA2('micontrasena', 256), 'Gerente');

INSERT INTO usuarios (ruttrabajador, nombreusuario, contrasena, cargo)
VALUES ('admin', 'admin', SHA2('admin123', 256), 'Admin');