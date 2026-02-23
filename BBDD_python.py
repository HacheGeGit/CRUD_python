# Importar librerías
import sqlite3 as sql

# Conexión a BBDD
con = sql.connect('Interacciones.bd')

# Creación de tablas
# Tabla medicamentos
con.execute("CREATE TABLE IF NOT EXISTS Medicamentos(Id_medicamento INT PRIMARY KEY," \
                                    "Nombre_comercial TEXT NOT NULL," \
                                    "PA TEXT NOT NULL," \
                                    "Laboratorio TEXT," \
                                    "Dosis TEXT NOT NULL," \
                                    "Tipo_transplante TEXT);")
# Tabla Alimentos
con.execute("CREATE TABLE IF NOT EXISTS Alimentos(Id_alimento INT PRIMARY KEY," \
                                    "Nombre_alimento TEXT NOT NULL," \
                                    "Tipo_alimento TEXT NOT NULL);")
# Tabla interacciones
con.execute("CREATE TABLE IF NOT EXISTS Interacciones(Id_interaccion INT PRIMARY KEY," \
                                    "Descripcion_interaccion TEXT NOT NULL," \
                                    "Nivel_riesgo TEXT NOT NULL);")

# Tabla Interacciones medicamento-alimento
con.execute("CREATE TABLE IF NOT EXISTS Inter_Med_Alim(Id_interaccion INT," \
                                    "Id_medicamento INT," \
                                    "Id_alimento INT," \
                                    "PRIMARY KEY (Id_medicamento, Id_alimento, Id_interaccion)," \
                                    "FOREIGN KEY (Id_medicamento) REFERENCES Medicamentos(Id_medicamento)," \
                                    "FOREIGN KEY (Id_alimento) REFERENCES Alimentos(Id_alimento)," \
                                    "FOREIGN KEY (Id_interaccion) REFERENCES Interacciones(Id_interaccion));")

# Tabla interacciones medicamento-medicamento
con.execute("CREATE TABLE IF NOT EXISTS Inter_Med_Med(Id_interaccion INT," \
                                    "Id_medicamento1 INT," \
                                    "Id_medicamento2 INT," \
                                    "PRIMARY KEY (Id_medicamento1, Id_medicamento2, Id_interaccion)," \
                                    "FOREIGN KEY (Id_medicamento1) REFERENCES Medicamentos(Id_medicamento)," \
                                    "FOREIGN KEY (Id_medicamento2) REFERENCES Medicamentos(Id_medicamento)," \
                                    "FOREIGN KEY (Id_interaccion) REFERENCES Interacciones(Id_interaccion));")

# Tabla con los riesgos alimenticios que tiene un paciente de transplante 
con.execute("CREATE TABLE IF NOT EXISTS Riesgo_Alimenticio(Id_riesgo INT PRIMARY KEY," \
                                    "Id_alimento INT NOT NULL," \
                                    "Descripcion TEXT NOT NULL," \
                                    "Nivel_riesgo TEXT NOT NULL," \
                                    "FOREIGN KEY (Id_alimento) REFERENCES Alimentos(Id_alimento));")

# Para la inserción de los datos crearé una lista para cada tabla con el fin de insertalos con un executemany para cada una

medicamentos = [
    (1, "Prograf", "Tacrolimus", "Astellas Pharma", "11.5 mg", "Pulmón"),
    (2, "Cellcept", "Micofenolato mofetilo", "Roche", "1000 mg", "Pulmón"),
    (3, "Prednisona", "Prednisona", "Cinfa", "7.5 mg", "Pulmón"),
    (4, "Mastical D", "Colecalciferol + probióticos", "Takeda", "1250 mg/400 UI", "Pulmón"),
    (5, "Magnogene", "Coenzima Q10", "Uriach", "53 mg", "Pulmón"),
    (6, "Omeprazol", "Omeprazol", "Cinfa", "20 mg", "Pulmón"),
    (7, "Letermovir", "Letermovir", "MSD", "480 mg", "Pulmón"),
    (8, "Septrim forte", "Sulfametoxazol/Trimetoprim", "Teofarma", "800/160 mg", "Pulmón"),
    (9, "Azitromicina", "Azitromicina", "Teva Pharma", "250 mg", "Pulmón"),
    (10, "Hidroferol", "Colecalciferol", "Faes Pharma", "0.266 mg", "Pulmón"),
    (11, "Ambisome", "Anfotericina B liposomal", "Gilead", "50 mg", "Pulmón"),
    (12, "Innohep", "Tinzaparina sódica", "LEO", "14000 UI", "Pulmón"),
    (13, "Polaramine", "Dexclorfeniramina", "ROVI", "2 mg", "Pulmón"),
    (14, "Eritromicina", "Eritromicina", "Normon", "500 mg", "Pulmón")
]

con.executemany("""
INSERT INTO Medicamentos (Id_medicamento, Nombre_comercial, PA, Laboratorio, Dosis, Tipo_transplante)
VALUES (?, ?, ?, ?, ?, ?)
""", medicamentos)

alimentos = [
    (1, "Pomelo", "Fruta cítrica"),
    (2, "Naranja", "Fruta cítrica"),
    (3, "Limón", "Fruta cítrica"),
    (4, "Ajo", "Condimento / vegetal"),
    (5, "Jengibre", "Condimento / vegetal"),
    (6, "Espinaca", "Verdura / vegetal"),
    (7, "Brócoli", "Verdura / vegetal"),
    (8, "Leche", "Lácteo"),
    (9, "Yogur", "Lácteo"),
    (10, "Queso", "Lácteo"),
    (11, "Almendras", "Frutos secos"),
    (12, "Nueces", "Frutos secos"),
    (13, "Té verde", "Bebida"),
    (14, "Café", "Bebida"),
    (15, "Jamón", "Carne cruda"),
    (16, "Sushi", "Pescado crudo"),
    (17, "Huevos", "Huevos crudos"),
]

con.executemany("""
INSERT INTO Alimentos (Id_alimento, Nombre_alimento, Tipo_alimento)
VALUES (?, ?, ?)
""", alimentos)

interacciones = [
    (1, "Puede aumentar los niveles de tacrolimus", "Alto"),
    (2, "Reduce la absorción de omeprazol", "Moderado"),
    (3, "Incrementa riesgo de hemorragia con anticoagulantes", "Alto"),
    (4, "Puede aumentar niveles de azitromicina", "Moderado"),
    (5, "Reduce absorción de ciertos minerales", "Bajo"),
    (6, "Aumento de la hepatotoxicidad", "Alto")
]

con.executemany("""
INSERT INTO Interacciones (Id_interaccion, Descripcion_interaccion, Nivel_riesgo)
VALUES (?, ?, ?)
""", interacciones)

inter_med_ali = [
    (1, 1, 1),  
    (2, 6, 2),  
    (3, 10, 5), 
]

con.executemany("""
INSERT INTO Inter_Med_Alim (Id_interaccion, Id_medicamento, Id_alimento)
VALUES (?, ?, ?)
""", inter_med_ali)

inter_med_med = [
    (6, 1, 14),   
    (3, 8, 3),  
    (4, 9, 4),   
]

con.executemany("""
INSERT INTO Inter_Med_Med (Id_interaccion, Id_medicamento1, Id_medicamento2)
VALUES (?, ?, ?)
""", inter_med_med)

riesgos_alimento = [
    (1, 15, "Carnes crudas o poco cocidas - riesgo de infección bacteriana", "Alto"),
    (2, 16, "Pescados y mariscos crudos o poco cocidos - riesgo de gastroenteritis", "Alto"),
    (3, 8, "Lácteos no pasteurizados - riesgo de Listeria y otros patógenos", "Alto"),
    (4, 10, "Quesos no pasteurizados - riesgo de Listeria (si no pasteurizados)", "Alto"),
    (5, 17, "Huevos crudos o poco cocidos - riesgo de Salmonella", "Alto"),
    (6, 2, "Frutas cítricas sin lavar adecuadamente - riesgo de contaminación bacteriana", "Moderado"),
    (7, 13, "Bebidas no pasteurizadas o jugos no tratados - riesgo de infecciones alimentarias", "Moderado"),
]

con.executemany("""
INSERT INTO Riesgo_Alimenticio (Id_riesgo, Id_alimento, Descripcion, Nivel_riesgo)
VALUES (?, ?, ?, ?)
""", riesgos_alimento)


#CRUD
# Inserción
con.execute("INSERT INTO Medicamentos(Id_medicamento, Nombre_comercial, PA, Laboratorio, Dosis, Tipo_transplante) " \
            "VALUES(15, 'Paracetamol','Paracetamol','Cinfa','650 mg','Pulmón');")

# Actualización
con.execute("UPDATE Medicamentos SET dosis = '400 mg' WHERE Nombre_comercial = 'Paracetamol'")


# Consultas
print('Medicamentos dentro de la pauta pertenecientes a la marca Cinfa:\n')

cursor = con.execute("SELECT Id_medicamento, Nombre_comercial, PA, Dosis " \
                     "FROM Medicamentos " \
                     "WHERE Laboratorio = 'Cinfa'")
for row in cursor:
    print(f"Id_medicamento: {row[0]}")
    print(f"Nombre_Comercial: {row[1]}")
    print(f"PA: {row[2]}")
    print(f"Dosis: {row[3]}\n")

print('Riesgos alimentarios derivados de la pauta:\n')

cursor = con.execute("SELECT a.Nombre_alimento, r.Descripcion, r.Nivel_riesgo " \
                     "FROM Riesgo_Alimenticio r JOIN Alimentos a " \
                     "ON r.Id_alimento = a.Id_alimento")
for row in cursor:
    print(f"{row[0]} - Riesgo {row[2]}: {row[1]}")

print('\nInteracciones del medicamento Prograf con el resto de la pauta:\n')

cursor = con.execute("SELECT m.Nombre_comercial, a.Nombre_alimento, i.Descripcion_interaccion, i.Nivel_riesgo " \
                     "FROM Medicamentos m " \
                     "JOIN Inter_Med_Alim ima ON m.Id_medicamento = ima.Id_medicamento " \
                     "JOIN Alimentos a ON ima.Id_alimento = a.Id_alimento " \
                     "JOIN Interacciones i ON ima.Id_interaccion = i.Id_interaccion " \
                     "WHERE m.Nombre_comercial = 'Prograf'" \
                     "UNION " \
                     "SELECT m1.Nombre_comercial, m2.Nombre_comercial, i.Descripcion_interaccion, i.Nivel_riesgo " \
                     "FROM Medicamentos m1 " \
                     "JOIN Inter_Med_Med imm ON m1.Id_medicamento = imm.Id_medicamento1 " \
                     "JOIN Medicamentos m2 ON imm.Id_medicamento2 = m2.Id_medicamento " \
                     "JOIN Interacciones i ON imm.Id_interaccion = i.Id_interaccion " \
                     "WHERE m1.Nombre_comercial = 'Prograf'")

for row in cursor:
    print(f"El {row[0]} interacciona con {row[1]}: {row[2]}. Nivel de riesgo: {row[3]}")

# Eliminación
con.execute("   DELETE " \
            "   FROM Medicamentos " \
            "   WHERE Nombre_comercial = 'Paracetamol'") 

print("\nSe ha borrado correctamente el registro.")
print('Lista de medicamentos actualizada: \n')

cursor = con.execute("SELECT Id_medicamento, Nombre_comercial, PA " \
                     "FROM Medicamentos")
for row in cursor:
    print(f"Id_medicamento: {row[0]}, Nombre_Comercial: {row[1]}, PA: {row[2]}")

# DCL para la gestión de usuarios y permisos
con.execute("CREATE TABLE IF NOT EXISTS Usuarios(Id_user INTEGER PRIMARY KEY AUTOINCREMENT," \
            "username TEXT UNIQUE NOT NULL," \
            "password TEXT NOT NULL," \
            "root_permissions BOOLEAN); ")

con.execute("INSERT INTO Usuarios(username, password, root_permissions)" \
            "VALUES ('Paciente','123456', False)") # Debería hashear la contraseña, pero al ser un ejercicio de prueba no lo haré

# No he pensado la app para el manejo de usuarios, básicamente porque no leí lo de DCL hasta que no estaba hecho el script,
# sin embargo, simularé cómo funcionaría aunque no se haga uso real en mi bbdd.
# Haré el manejo mediante un decorador y una función login que verificará si el usuario tiene permisos. En mi caso no tiene, por lo que no podrá
# tener acceso a nada que no sea DML. Cada vez que se quiera realizar una acción que no sea DML, se envolverá la función con el decorador.

def login(user, psswrd):
    cursor = con.cursor()    
    cursor.execute("SELECT root_permissions FROM Usuarios WHERE username = ? AND password = ?",(user,psswrd))
    row = cursor.fetchone()
    if row == None:
        return False
    return bool(row[0])
    
def verificar_permisos(func):
    def wrapper():
        user = input('Introduce tu nick: ')
        psswrd = input('Introduce tu contraseña: ')
        root = login(user,psswrd)
        if root != True:
            return '\nAcción denegada por falta de permisos.' 
        
        return func(), 'Tabla creada correctamente.'
    return wrapper
    
# Con la función decorada, siempre que se llame en el código, se ejecutará la verificación de permisos
@verificar_permisos
def crearTabla():
    con.execute("CREATE TABLE IF NOT EXISTS Alimentos2(Id_alimento INT PRIMARY KEY," \
                "Nombre_alimento TEXT NOT NULL," \
                "Tipo_alimento TEXT NOT NULL);")
 
print(crearTabla()[1])
print('\nTablas dentro de la BBDD:')

# Para comprobar que no se haya creado la tabla nueva "Alimentos2", se verificará qué tablas existen en la BBDD
cursor = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
for tabla in cursor:
    print(tabla[0])


    

