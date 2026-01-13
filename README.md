Este es el código del proyecto de TFG: "Asistente Inteligente para la mejora del Feedback en Plataformas de Evaluación Automática de Código".

Para ejecutar las pruebas descritas de nuevo, es necesario tener en cuenta las siguientes instrucciones:

1. Asegúrate de tener instalado Python 3.11 o superior en tu sistema.
2. Genera 10 API_KEYS diferentes en https://aistudio.google.com/api-keys, y pega dichas keys en 10 líneas en el fichero "API_KEYS.txt"
2. Intala las dependencias en terminal o consola con el siguiente comando:

    pip install google-genai numpy

3. Ejecuta el siguiente comando para inicar el script principal con los resultados de Feedback en Python y enviar soluciones al Jutge.org:

    python3 mainScript tries account pass max_reviews problems

    tries = número de repeticiones por cada problema con soluciones diferentes.
    account = la cuenta de gmail de Jutge.org que quieres que se abra con la API.
    pass = la contraseña de dicha cuenta.
    max_reviews = el máximo de tamaño de soluciones que quieres que llegue a generar, se desconoce el límite de soluciones que tiene registrada cada problema, solo que es igual o mayor a 100.
    problems = número de problemas de la lista "problems.txt" que quieres que evalúe, si se pone 0 los evaluará todos en conjunto. [0 - 14]

4. Ejecuta el siguiente script si quieres generar los resultados de Feedback en C++, con los mismos atributos que en el anterior comando.

    python3 mainScript_CC tries account pass max_reviews problems

5. La ubicación de los resultados estarán en:

    ./FEEDBACKS = los resultados de Feedback en Python junto con los prompts.

    ./SOLVING = los resultados de Resolución

    ./FEEDBACKS_CC = los resultados de Feedback en C++ junto con los prompts.

    time_log_feedback.txt = los resultados de cálculo temporal para feedback.

    time_log_solving.txt = los resultados de cálculo temporal para resolución.

    ./DENDOGRAMA/DENDORGRAMAS = los dendrogramas generados para Python.
    
    ./DENDROGRAMA_CC/DENDROGRAMAS = los dendrogramas generados para C++.
