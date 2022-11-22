## Mejia Galindo Carlos Alejandro

function factorial()
  index = parse(Int128, ARGS[1])
  solution::BigInt = 1
  for i in 1:index ## Se inicia el bucle 
    solution *= i
  end
  println(solution)
end

factorial()
