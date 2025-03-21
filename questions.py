import random


questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1]


questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)


puntos = 0

for question, options, correct_index in questions_to_ask:
    print(question)

  
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1  

      
            if user_answer < 0 or user_answer >= len(options):
                print("Respuesta no válida, ingresa un número dentro del rango.")
                continue 

            if user_answer == correct_index:
                print("¡Correcto!")
                puntos += 1
                break 
            else:
                if intento == 0:
                    print("Incorrecto. Intenta de nuevo.")
                else:
                    print(f"Incorrecto. La respuesta correcta es: {options[correct_index]}")
                    puntos -= 0.5
                
                

        except ValueError:
            print("Entrada no válida. Ingresa un número.")


print(f"Puntaje final: {puntos}/3")