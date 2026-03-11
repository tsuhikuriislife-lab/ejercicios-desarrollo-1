#Empezamos saludando al usuario y mostrandole las opciones.

print("Bienvenido al conjunto de ejercicios!")
print("Lista de ejercicios:\n1.Heladeria\n2.Gimnasio\n3.Cafeteria\n4.Cine\n5.Tienda de mascotas\n6.Parqueadero\n7.Peluqueria\n8.Tienda deportiva\n9.Spa\n10.Academia de Baile\n11.Heladeria #2\n12.Gimnasio #2\n13.Cafeteria #2\n14.Cine #2\n15.Parqueadero #2\n16.Tienda de mascotas #2\n17.Peluqueria #2\n18.Centro de Idiomas\n19.Tienda de Ropa deportiva\n20.Club recreativo\n21.Salir")
opcion_inicio = int(input("-- A que ejercicio quieres ir?: "))

if opcion_inicio == 1:

    # Sabor mas pedido
    # Adicionalmente, creamos las variables de los tipos de helados para usarlos despues.

    vainilla = 0
    chocolate = 0
    fresa = 0

    # Para hacerlo mas sencillo, usare un par de funciones para definir el sabor escogido en cada opcion.

    def sabor_escogido(opcion1, opcion2, opcion3, vainilla, chocolate, fresa):
        if opcion1 == 1:
            vainilla += 1
        elif opcion1 == 2:
            chocolate += 2
        elif opcion1 == 3:
            fresa += 1
        if opcion2 == 1:
            vainilla += 1
        elif opcion2 == 2:
            chocolate += 2
        elif opcion2 == 3:
            fresa += 1
        if opcion3 == 1:
            vainilla += 1
        elif opcion3 == 2:
            chocolate += 2
        elif opcion3 == 3:
            fresa += 1
        return vainilla, chocolate, fresa

    # Se necesita primero mostrarle al usuario los sabores disponibles, y pedirle la cantidad de pedidos que quiere realizar

    print("Bienvenido a la heladeria, estos son nuestros sabores disponibles:\n1.Vainilla\n2.Chocolate\n3.Fresa\n")
    pedidos = int(input("Cuantos pedidos quieres realizar?\n--- "))

    # Ahora, creamos un bucle con la condicion de los 5 pedidos.

    ciclo = 0
    while ciclo < pedidos:
        print(f"Pedido #{ciclo+1}")
        opcion1 = int(input("Selecciona el primer sabor: "))
        opcion2 = int(input("Selecciona el segundo sabor: "))
        opcion3 = int(input("Selecciona el tercer sabor: "))
        vainilla, chocolate, fresa = sabor_escogido(opcion1, opcion2, opcion3, vainilla, chocolate, fresa)
        ciclo += 1

    print(f"Sabores escogidos:\n- Vainilla: {vainilla} veces\n- Chocolate: {chocolate} veces\n- Fresa: {fresa} veces")

elif opcion_inicio == 2:
    # Clases segun edad.
    # Declaramos una funcion para determinar la clase del usuario.

    def clase_usuario(edad):
        if edad <= 0:
            print("Edad invalida.")
        elif 0 < edad < 13:
            print("No puedes ingresar a ninguna clase.")
        elif 13 <= edad <= 17:
            print("Puedes entrar a la clase juvenil!")
        elif 18 <= edad <= 59:
            print("Puedes entrar a la clase general!")
        elif 59 <= edad:
            print("Puedes entrar a la clase de senior!")

    # Primero, le damos la bienvenida al usuario.
    print("Bienvenido a nuestro gimnasio!")
    # Creamos un bucle para ingresar la edad repetidamente, y que el usuario pueda cerrar el programa a su gusto.
    salir = 0
    while salir == 0:

        edad = int(input("Por favor digita tu edad: "))
        clase_usuario(edad)
        opcion_salida = input("Quiere cerrar el ejercicio? S/N")
        if opcion_salida == "s":
            salir += 1
        elif opcion_salida == "n":
            salir += 0

elif opcion_inicio == 3:
    # Total de una compra sencilla.
    # Como siempre, le damos la bienvenida al usuario.
    print("Bienvenido a la cafeteria!")
    valor_cafe = 4000
    valor_te = 3500
    valor_jugo = 5000
    print(f"Aqui tienes nuestro menu:\n1. Cafe - ${valor_cafe}\n2. Te - ${valor_te}\n3.Jugo - ${valor_jugo}")

    # Ahora necesitamos pedirle la cantidad de la compra al usuario.
    cantidad_cafe = int(input("Cuantos cafes deseas ordenar?: "))
    cantidad_te = int(input("Cuantos tes deseas ordenar?: "))
    cantidad_jugo = int(input("Cuantos jugos deseas ordenar?: "))

    cantidad_cafe = max(0, cantidad_cafe)
    cantidad_te = max(0, cantidad_te)
    cantidad_jugo = max(0, cantidad_jugo)

    print(f"Orden:\n1. Cafe: {cantidad_cafe}\n2. Te: {cantidad_te}\n3. Jugo: {cantidad_jugo}")

    salto = input("Presione ENTER para continuar...")

    print(f"Valor de la orden:\n1.Cafe: ${valor_cafe*cantidad_cafe}\n2. Te: ${valor_te*cantidad_te}\n3. Jugo: ${valor_jugo*cantidad_jugo}")
    print(f"Total: ${(cantidad_cafe*valor_cafe)+(cantidad_jugo*valor_jugo)+(cantidad_te*valor_te)}")

elif opcion_inicio == 4:
    # Entrada segun edad.

    def asignador_valor(edad):
        valor_niños = 8000
        valor_adultos = 12000
        valor_mayores = 9000
        if edad <= 0:
            print("Edad invalida.")
        elif edad > 0 and edad <= 12:
            print(f"El valor de tu boleto es de ${valor_niños}")
        elif edad >= 13 and edad < 60:
            print(f"El valor de tu boleto es de ${valor_adultos}")
        elif edad >= 60:
            print(f"El valor de tu boleto es de ${valor_mayores}")
    # Nuevamente bienvenida.
    print("Bienvenido al cine!")


    salir = 0
    while salir == 0:
        edad = int(input("Por favor ingresa tu edad: "))        
        asignador_valor(edad)
        opcion_salida = input("Deseas salir? S/N").lower()
        if opcion_salida == "s":
            salir += 1

elif opcion_inicio == 5:
    # Alimento segun animal.
    print("Bienvenido a la tienda de mascotas!")
    salir = 0
    while salir == 0:
            
        animal_usuario = input("Escoge tu tipo de mascota:\n1. Perro\n2. Gato\n3. Conejo\n--- ")
        if animal_usuario == "1":
            print("Te recomendamos comprar comida Dog Chaw!")
        elif animal_usuario == "2":
            print("Te recomendamos comprar comida Whiskas!")
        elif animal_usuario == "3":
            print("Te recomendamos comprar comida Burgess!")
        opcion_salida = input("Quieres salir? S/N").lower
        if opcion_salida == "s":
            salir+= 1

elif opcion_inicio == 6:
    #Cobro por horas.
    print("Bienvenido al parqueadero!")
    primera_hora = 5000
    horas_extra = 3000
    salir = 0 
    print(f"Valor por horas:\nPrimera hora: ${primera_hora}\nCada hora extra: ${horas_extra}")
    while salir == 0:
        tiempo_parqueadero = int(input("Cuantas horas estuviste en el parqueadero?: "))
        tiempo_parqueadero = max(0, tiempo_parqueadero)
        if tiempo_parqueadero == 1:
            print(f"El valor es de: ${primera_hora}")
        elif tiempo_parqueadero  > 1:
            print(f"El valor es de: ${primera_hora+((tiempo_parqueadero-1)*horas_extra)}")
        opcion_salida = input("Salir? S/N").lower()
        if opcion_salida == "s":
            salir += 1

elif opcion_inicio == 7:
    # Turno de dia.
    print("Bienvenido a la peluqueria!")
    salir = 0
    while salir == 0:
            
        hora_peluqueria = int(input("Por favor digita la hora de llegada en formato 24h: "))
        if hora_peluqueria in range (6,11):
            print("Horario de mañana.")
        elif hora_peluqueria in range (12, 17):
            print("Horario de tarde.")
        elif hora_peluqueria in range (18, 22):
            print("Horario nocturno.")
        else:
            print("Fuera de horario.")
        opcion_salida = input("Salir? S/N: ")
        if opcion_salida == "s":
            salir += 1

elif opcion_inicio == 8:
    print("Bienvenido a la tienda deportiva!")
    productos = int(input("Por favor digita la cantidad de productos: "))
    cantidad_productos = 0
    for i in range(0, productos):
        precios = int(input("Por favor digita el valor del producto: $"))
        if precios >= 100000:
            cantidad_productos += 1
    print(f"{cantidad_productos} productos con precios superiores a $100000!")

elif opcion_inicio == 9:
    servicios = ["masaje","facial","manicure"]
    print("Bienvenido al Spa!")
    print("Estos son nuestros servicios disponibles:\n1.Masaje\n2.Facial\n3.Manicure")
    spa = input("Que servicio deseas cotizar?: ")
    if spa in servicios:
        print("Tu servicio se encuentra disponible!")
    else:
        print("Servicio no disponible.")

elif opcion_inicio == 10:
    print("Bienvenido a la academia de baile!")
    asistencias = int(input("Por favor digite cuantas inasistencias tuvo este mes: "))
    if asistencias < 5:
        print("Asistencias bajas.")
    elif asistencias in range (5, 8):
        print("Asistencias medias.")
    elif asistencias > 9:
        print("Asistencias altas.")

elif opcion_inicio == 11:
    print("Bienvenido a la heladeria!")
    cono = 3000
    vaso = 4000
    banana = 9000
    print(f"Este es nuestro menu de precios:\n1.Cono: ${cono}\n2.Vaso: ${vaso}\n3.Banana split: ${banana}")
    cantidad_cono = 0
    cantidad_vaso = 0
    cantidad_banana = 0
    total = 0
    salir = 0
    ciclo = 0
    while salir == 0:
        cantidad_cono_temporal = 0
        cantidad_vaso_temporal = 0
        cantidad_banana_temporal = 0
        print(f"Pedido #{ciclo+1}")
        producto = int(input("Que producto desea ordenar?: "))
        if producto == 1:
            cantidad = int(input("Cuantos desea ordenar?: "))
            cantidad_cono_temporal += cantidad
            cantidad_cono += cantidad
            total_cono = cono * cantidad_cono_temporal
            total += total_cono
            print(f"El total es: ${total_cono}")
        elif producto == 2:
            cantidad = int(input("Cuantos desea ordenar?: "))
            cantidad_vaso_temporal += cantidad
            cantidad_vaso += cantidad
            total_vaso = vaso * cantidad_vaso_temporal
            total += total_vaso
            print(f"El total es: ${total_vaso}")
        elif producto == 3:
            cantidad = int(input("Cuantos desea ordenar?: "))
            cantidad_banana_temporal += cantidad
            cantidad_banana += cantidad
            total_banana = banana * cantidad_banana_temporal
            total += total_banana
            print(f"El total es: ${total_banana}")
        opcion_salida = input("Salir? S/N: ")
        if opcion_salida == "s":
            salir += 1
        ciclo += 1

    print(f"Total del dia:\nConos vendidos: {cantidad_cono}\nVasos vendidos: {cantidad_vaso}\nBanana split vendidas: {cantidad_banana}\nTotal vendido: ${total}\nClientes atendidos: {ciclo}")

elif opcion_inicio == 12:
    print("Bienvenido al gimnasio!")
    ciclos = int(input("Cuantas personas vas a registrar?: "))
    bajo = 0
    medio = 0
    alto = 0
    usuario = 0
    for i in range (0, ciclos):
        print(f"Usuario #{usuario+1}")
#        nombre = input("Ingrese su nombre: ")
        dias = int(input("Cuantos dias asistio esta semana?: "))
#        minutos = int(input("Cuantos minutos en promedio duraron sus sesiones?: "))
        if dias < 3:
            print("Bajo compromiso.")
            bajo += 1
        elif dias in range (3,4):
            print("Compromiso medio.")
            medio += 1
        elif dias >= 5:
            print("Compromiso alto.")
            alto += 1
        usuario += 1
    print(f"Cantidad de usuarios: {ciclos}\nBajo compromiso: {bajo}\nMedio compromiso: {medio}\nAlto compromiso: {alto}")

elif opcion_inicio == 13:
    print("Bienvenido a la cafeteria!")
    cafe = 4000
    capuchino = 7000
    pastel = 6000
    total = 0
    salir = 0
    c
    while salir == 0:
        print
            salir += 1
        
