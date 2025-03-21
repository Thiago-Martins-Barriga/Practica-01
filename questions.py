import random

# Lista de preguntas
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Opciones de respuesta para cada pregunta
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índices de las respuestas correctas para cada pregunta
correct_answers_index = [1, 2, 0, 3, 1]




for _ in range(3):
    question_index = random.randint(0, len(questions) - 1)
    print(questions[question_index])
    
   
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    
   
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1  
            
            
            if user_answer < 0 or user_answer >=5:
                print("Respuesta no válida")
            elif user_answer == correct_answers_index[question_index]:
                print("¡Correcto!")
                
                break  
            else:
               
                if intento == 0:
                    print("Incorrecto. Intenta de nuevo.")
                else:
                   
                    print("Incorrecto. La respuesta correcta es:")
                    print(answers[question_index][correct_answers_index[question_index]])
                    
        except ValueError:
            print("Respuesta no válida, ingresa un número.")
    
    print()  
