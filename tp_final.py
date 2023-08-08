import sqlite3

mi_conexion = sqlite3.connect("BaseDeDatosLey")
mi_cursor = mi_conexion.cursor()


class leyes():

    def __init__(self, ing_ley, insertar_ley, consultar_ley, borrar_ley, op):

        self.mi_cursor = mi_conexion.cursor()
        self.mi_conexion = sqlite3.connect("BaseDeDatosLey")
        self.ing_ley = ing_ley
        self.insertar_ley = insertar_ley
        self.consultar_ley = consultar_ley
        self.borrar_ley = borrar_ley
        self.op = op

    def crud(self):
    
     while self.op != 0:
         print("Bienvenidos a nuestro gestor de leyes, ingrese una opcion")
         self.ing_ley = int(input("ingrese una opcion: 1) Insertar Ley, 2) Consultar Ley, 3) Borrar Ley, 4) Salir del programa: "))
         self.op = -1
         self.op_1 = 1
         self.op_2 = 2
         self.op_3 = 3
         self.op_4 = 4

         if self.ing_ley == self.op_1:
             self.ing_ley = []
             self.ing_ley.append(int(input("Ingrese número de registro: ")))
             self.ing_ley.append(float(input("Ingrese tipo de norma: ")))
             self.ing_ley.append(int(input("Ingrese número de norma: ")))
             self.ing_ley.append(int(input("Ingrese número de categoría: ")))
             self.mi_cursor.execute("INSERT INTO LEYES VALUES (?,?,?,?)", self.ing_ley)
             print("Las leyes, fueron agregadas con exito!")

         elif self.ing_ley == self.op_2:
             self.mi_cursor.execute("SELECT * FROM LEYES")
             self.ing_ley = self.mi_cursor.fetchall()
             for self.consultar_ley in self.ing_ley:
               print("Número de registro:", self.consultar_ley[0], ",", "Tipo Normativa:", self.consultar_ley[1], ",", "Categoría:", self.consultar_ley[2], ",", "Número de normativa:", self.consultar_ley[3])
          
         elif self.ing_ley == self.op_3:
             self.borrar_ley=int(input("selecciona numero de registro a borrar:"))
             self.mi_cursor.execute(f"DELETE FROM LEYES WHERE NRO_REGISTRO= {self.borrar_ley}")
             print("El registro seleccionado, fue eliminado con exito!")

         elif self.ing_ley == self.op_4:
             break

program = leyes("1", "2", "3", "4", "5")
program.crud()

mi_conexion.commit()
mi_conexion.close()




