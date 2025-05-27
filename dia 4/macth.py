#serie = "N-02"

#match serie:
 #   case "N-01":
  #      print("Sansung")
   # case "N-02":
    #    print("Nokia")
    #case "N-03":
     #   print("Motorola")
    #case "N-04":
     #   print("No existe este producto")

cliente = {"nombre": "fabian",
           "edad": 29,
           "ocupacion": "trabajador"}
pelicula = {"titulo": "matrix",
            "ficha tecnica" :{"protagonista" : "keanu reeves",
                                                  "director": "lana y lilly wachowski"}}
elementos = [cliente , pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo": titulo,
              "ficha tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("no se que es esto")


