# Sistema CRUD de Interacciones Farmacológicas (SQLite)

Proyecto académico desarrollado en Python que implementa un sistema de base de datos relacional para la gestión de medicamentos, alimentos, interacciones farmacológicas y riesgos alimentarios en pacientes trasplantados.
El objetivo es demostrar el manejo de operaciones CRUD, el diseño de tablas relacionales y la realización de consultas SQL utilizando SQLite.

## Objetivos del proyecto
Este trabajo de clase demuestra:
    -Creación de base de datos con SQLite
    -Diseño de modelo relacional
    -Inserciones masivas con executemany
    -Operaciones CRUD completas
    -Consultas con JOIN
    -Uso básico de control de permisos mediante decoradores
    -Estructura de la base de datos

## La base de datos Interacciones.bd contiene las siguientes tablas:
    Medicamentos
    Información de fármacos de la pauta del paciente.
    Campos principales:
    Id_medicamento (PK)
    Nombre_comercial
    PA (principio activo)
    Laboratorio
    Dosis
    Tipo_transplante
    Alimentos
    Catálogo de alimentos relevantes.
    Campos:
        Id_alimento (PK)
        Nombre_alimento
        Tipo_alimento
        Interacciones
        Descripción y nivel de riesgo de interacciones.
        Campos:
        Id_interaccion (PK)
        Descripcion_interaccion
        Nivel_riesgo
        Inter_Med_Alim
        Tabla de relación muchos-a-muchos entre medicamentos y alimentos.
        Inter_Med_Med
        Tabla de relación muchos-a-muchos entre medicamentos.
        Riesgo_Alimenticio
        Riesgos alimentarios relevantes para pacientes trasplantados.
        Usuarios
        Tabla simulada para control de permisos.

Nota: Las contraseñas se almacenan en texto plano únicamente con fines educativos.

## Funcionalidades implementadas:
    CREATE:
        -Creación automática de todas las tablas
        -Inserción de datos de ejemplo
        -Inserción individual de medicamento
    READ:
        Consultas implementadas:
        Medicamentos del laboratorio Cinfa
        Riesgos alimentarios de la pauta
        Interacciones del medicamento Prograf
    Uso de:
    SELECT
    JOIN
    UNION
    UPDATE
    Ejemplo:
        UPDATE Medicamentos
        SET dosis = '400 mg'
        WHERE Nombre_comercial = 'Paracetamol';
    DELETE: Eliminación de registros de medicamentos.
    Control de permisos (simulado)
    Se implementa:
        -función login
        -decorador @verificar_permisos
## Objetivo:
    -Simular control de acceso a operaciones DDL.
    -Demostrar uso de decoradores en Python.
    -Implementación simplificada con fines didácticos.
## Cómo ejecutar:
Requisitos:
    -Python 3.x
    -Biblioteca estándar sqlite3
Ejecución:
    ```bash
    python BBDD_python.py

La base de datos se crea automáticamente en el directorio del proyecto.
## Contexto académico
Este proyecto ha sido desarrollado exclusivamente con fines educativos como ejercicio práctico de:
    -SQL
    -SQLite
    -Python
    -Operaciones CRUD
    -Diseño de bases de datos
No está destinado a uso clínico real.

Autor: HacheGeGit