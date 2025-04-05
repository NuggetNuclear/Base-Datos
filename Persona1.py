import csv

pathFile = input("Ingrese la ruta del archivo CSV: ")
def procesar_datos(input_file=pathFile):
    output_file='Salida-1.sql'
    
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        outfile.write("INSERT INTO persona1 (RUT, Nombre, Edad, Direccion) VALUES\n")

        for row in reader:
            RUT = row[0].strip()
            Nombre = row[1].strip()
            Edad = row[2].strip()
            Direccion = row[3].strip()

            RUT = RUT.zfill(10)

            if len(Edad) == 1:
                Edad = '0' + Edad 

            insert_statement = f"('{RUT}','{Nombre}','{Edad}','{Direccion}'),\n"
            outfile.write(insert_statement)

# Llamar a la función

procesar_datos(pathFile)