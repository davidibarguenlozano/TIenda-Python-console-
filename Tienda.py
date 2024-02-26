products = {0: ["Gaseosas",200 ,5000] , 1 : ["Papitas" ,50 ,2000]}
dinner= 300000 



condition = 0;
while condition != 5:
  print("Opcion 1 : ver productos en stock")
  print("Opcion 2 : registrar venta producto")
  print("Opcion 3 : ver productos en stock")
  print("Opcion 4 : ver productos en stock")
  print("Opcion 5 : ver productos en stock")

  condition = int(input("Selecciona: "))
  match condition:
    case 1 :
      print("caso 1")
      print(products)
    case 2 :
      print("caso 2")
      product = int(input("Ingrese el id de produto que quiere vender"))
      cantidad = int(input("Ingrese la cantidad de prodcutos que desea vender"))
      pd = (cantidad * products[product][2])
  

      

      
      products[product][1] = products[product][1] -cantidad
      dinner = dinner + pd
      billete = int(input("Ingrese la cantidad que le dieron"))
      def sistem_devolutions(billete,pd):
        devolver = billete -pd
        return devolver 
      
      
      print(products[0][1] )
      print("Devuelva : ",  sistem_devolutions(billete,pd)) 

      

      print("El dinero actual de la tienda es: " ,dinner)
      
      
      
    case 3 :
      print("caso 3")
    case 4 :
      print("caso 4")
      
    
    
  