create table empleados (
    id_empleado int auto_increment primary key,
    nombre_empleado varchar(100) not null,
    apellido_empleado  varchar(100) not null,
    fecha_contratacion date not null,
    salario decimal(10, 2) not null
);;
