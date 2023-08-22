resistividad = {
    "AL": (0.28, "Aluminio"),
    "CU": (0.017, "Cobre"),
    "AU": (0.23, "Oro"),
    "NI": (0.12, "Niquel"),
    "ZN": (0.06, "Zinc"),
    "SN": (0.12, "Estaño")
}

L = float(input("Ingresa la longitud del conductor en [m]: "))
S = float(input("Ingresa la sección del conductor en [mm2]: "))

while True:
    material = input("Ingresa el símbolo del material: ")
    
    if material.islower():
        print("Error, ingresa el material en mayúsculas. Vuelve a intentarlo.")
    else:
        material = material.upper()
        if material in resistividad:
            p = resistividad[material][0]
            print("Resistividad de ", resistividad[material][1], "=[ohm.mm1/m]")

            if S == 0:
                print("Error, la sección no puede ser cero. Ingresa una sección diferente.")
            else:
                R = p * L / S
                print("La resistencia de ", R, "ohms")
            break  # Salir del ciclo si todo está correcto
        else:
            print("Material no encontrado. Por favor, ingresa un símbolo de material válido en mayúsculas.")
