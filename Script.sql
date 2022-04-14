create schema agenda_contactos;
use agenda_contactos;

create table contactos(
	id int primary key not null auto_increment,
    nombre varchar(255) not null,
    telefono varchar(255) not null,
	email varchar(255) not null
);
