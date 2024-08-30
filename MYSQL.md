
#### comando de ayuda

verificar si la tabla es InnoDB o MyISAM
Si es otro motor (como MyISAM), las transacciones no serán soportadas de manera adecuada.

SHOW TABLE STATUS LIKE 'gastos';

#### Cambiar el Motor de Almacenamiento a InnoDB

ALTER TABLE nombre_de_tu_tabla ENGINE=InnoDB;