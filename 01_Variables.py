#varaibles 
var_int = 3
print (var_int)

var_string = "Quintana"
print (var_string)

var_float = 1.4
print (var_float)

var_bool = True
print (var_bool)

#concatenación 
print(var_int,var_string,var_float,var_bool)

#función str (cambia a string)
var_cambio = str(var_int)
print (var_cambio)
print(type(var_cambio))

#función len (cuenta todas caracteres)
print (len(var_string))

#variables en una sola línea
name,apellido, age, apodo = "Criss","Quintana",19,"Trica"
print ("me llamo: ",apellido,name,"\ntengo: ",age,"\nme conocen como: ",apodo)

#función input (ingresar variables)
var_edad = input("Ingresar su edad: ")
print ("tiene : ",var_edad)

#forzamos el tipo de dato ?
address: str = "mi dirección"
num = 2
print(address)
