import csv

pathFile = input("Ingrese la ruta del archivo CSV: ")
def procesar_datos(input_file=pathFile):
    
    output_file='Salida-2.sql'
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        outfile.write("INSERT INTO persona2 (RUT, Nombre, Edad, Direccion) VALUES\n")

        ruts_vistos = set()
        primera_linea = True

        for row in reader:
            RUT = row[0].strip()  
            Nombre = row[1].strip()  
            Edad = row[2].strip()  
            Direccion = row[3].strip()  

            if len(RUT) < 10:
                RUT = RUT.zfill(10)

            if RUT in ruts_vistos:
                continue
            ruts_vistos.add(RUT)

            if len(Edad) == 1:
                Edad = '0' + Edad

            linea_sql = f"('{RUT}','{Nombre}','{Edad}','{Direccion}')"
            if not primera_linea:
                outfile.write(",\n")
            else:
                primera_linea = False
            outfile.write(linea_sql)

        outfile.write(";\n") 

# Llamar a la función
procesar_datos(input_file=pathFile)