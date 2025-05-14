-- Crear base de datos
CREATE DATABASE biblioteca;

-- Usar la base de datos creada
USE biblioteca;

-- Tabla para ElementoBiblioteca (tabla base)
CREATE TABLE ElementoBiblioteca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano_publicacion INT NOT NULL,
    tipo VARCHAR(50) NOT NULL
);

-- Tabla para DVD (hereda de ElementoBiblioteca)
CREATE TABLE DVD (
     id INT PRIMARY KEY,
     duracion INT NOT NULL,
     genero VARCHAR(100) NOT NULL,
     FOREIGN KEY (id) REFERENCES ElementoBiblioteca(id) ON DELETE CASCADE
);

-- Tabla para Libro (hereda de ElementoBiblioteca)
CREATE TABLE Libro (
   id INT PRIMARY KEY,
   isbn VARCHAR(50) NOT NULL,
   numero_paginas INT NOT NULL,
   genero VARCHAR(100) NOT NULL,
   editorial VARCHAR(255) NOT NULL,
   FOREIGN KEY (id) REFERENCES ElementoBiblioteca(id) ON DELETE CASCADE
);

CREATE TABLE Revista (
     id INT PRIMARY KEY,
     numero_edicion INT NOT NULL,
     categoria VARCHAR(100),
     FOREIGN KEY (id) REFERENCES ElementoBiblioteca(id)
);