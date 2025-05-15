-- Insertar 10 libros
INSERT INTO ElementoBiblioteca (titulo, autor, ano_publicacion, tipo)
VALUES 
('Cien Años de Soledad', 'Gabriel García Márquez', 1967, 'Libro'),
('1984', 'George Orwell', 1949, 'Libro'),
('El Señor de los Anillos', 'J.R.R. Tolkien', 1954, 'Libro'),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 'Libro'),
('La Sombra del Viento', 'Carlos Ruiz Zafón', 2001, 'Libro'),
('Crónica de una Muerte Anunciada', 'Gabriel García Márquez', 1981, 'Libro'),
('Rayuela', 'Julio Cortázar', 1963, 'Libro'),
('Ficciones', 'Jorge Luis Borges', 1944, 'Libro'),
('El Alquimista', 'Paulo Coelho', 1988, 'Libro'),
('La Ciudad y los Perros', 'Mario Vargas Llosa', 1963, 'Libro');

-- Suponiendo que los IDs generados son del 1 al 10
INSERT INTO Libro (id, isbn, numero_paginas, genero, editorial)
VALUES
(1, '978-0307474728', 417, 'Realismo mágico', 'Sudamericana'),
(2, '978-0451524935', 328, 'Distopía', 'Secker & Warburg'),
(3, '978-0618640157', 1216, 'Fantasía', 'Allen & Unwin'),
(4, '978-8491050284', 863, 'Novela clásica', 'Francisco de Robles'),
(5, '978-8408172175', 576, 'Misterio', 'Planeta'),
(6, '978-0307387738', 122, 'Novela', 'Sudamericana'),
(7, '978-8437600362', 688, 'Novela experimental', 'Cátedra'),
(8, '978-0307950924', 174, 'Ficción', 'Sur'),
(9, '978-0062315007', 208, 'Autoayuda', 'HarperOne'),
(10, '978-6073128651', 384, 'Novela', 'Alfaguara');

-- Insertar 10 DVDs
INSERT INTO ElementoBiblioteca (titulo, autor, ano_publicacion, tipo)
VALUES 
('Inception', 'Christopher Nolan', 2010, 'DVD'),
('The Matrix', 'The Wachowskis', 1999, 'DVD'),
('Interstellar', 'Christopher Nolan', 2014, 'DVD'),
('Parasite', 'Bong Joon-ho', 2019, 'DVD'),
('The Godfather', 'Francis Ford Coppola', 1972, 'DVD'),
('Pulp Fiction', 'Quentin Tarantino', 1994, 'DVD'),
('Spirited Away', 'Hayao Miyazaki', 2001, 'DVD'),
('The Dark Knight', 'Christopher Nolan', 2008, 'DVD'),
('Fight Club', 'David Fincher', 1999, 'DVD'),
('The Shawshank Redemption', 'Frank Darabont', 1994, 'DVD');

-- Suponiendo que los IDs generados son del 11 al 20
INSERT INTO DVD (id, duracion, genero)
VALUES
(11, 148, 'Ciencia ficción'),
(12, 136, 'Acción'),
(13, 169, 'Ciencia ficción'),
(14, 132, 'Thriller'),
(15, 175, 'Crimen'),
(16, 154, 'Drama'),
(17, 125, 'Animación'),
(18, 152, 'Acción'),
(19, 139, 'Drama psicológico'),
(20, 142, 'Drama');

-- Insertar 10 Revistas
INSERT INTO ElementoBiblioteca (titulo, autor, ano_publicacion, tipo)
VALUES 
('National Geographic', 'Varios', 2023, 'Revista'),
('Scientific American', 'Varios', 2023, 'Revista'),
('TIME', 'Varios', 2023, 'Revista'),
('Forbes', 'Varios', 2023, 'Revista'),
('Nature', 'Varios', 2023, 'Revista'),
('The New Yorker', 'Varios', 2023, 'Revista'),
('Harvard Business Review', 'Varios', 2023, 'Revista'),
('Muy Interesante', 'Varios', 2023, 'Revista'),
('Quo', 'Varios', 2023, 'Revista'),
('PC Magazine', 'Varios', 2023, 'Revista');

-- Suponiendo que los IDs generados son del 21 al 30
INSERT INTO Revista (id, numero_edicion, categoria)
VALUES
(21, 101, 'Ciencia'),
(22, 245, 'Tecnología'),
(23, 330, 'Actualidad'),
(24, 200, 'Negocios'),
(25, 789, 'Investigación'),
(26, 985, 'Cultura'),
(27, 612, 'Management'),
(28, 456, 'Curiosidades'),
(29, 399, 'Ciencia Popular'),
(30, 300, 'Tecnología');

