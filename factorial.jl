## Mejia Galindo Carlos Alejandro
using Printf

function factorial()
  index = parse(Int128, ARGS[1])
  solution::BigInt = 1
  for i in 1:index ## Se inicia el bucle 
    solution *= i ## Se obtiene el producto de todos los números anteriores a n
  end
  @printf("El factorial de %i es: \n", index)
  print(solution)
end

factorial()
