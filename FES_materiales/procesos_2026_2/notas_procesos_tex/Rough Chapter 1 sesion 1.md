#Rough Chapter 1 sesion 1



Clase 1:

Ideas a introducir:  Definición formal de proceso estocástico, espacio de estados, probabilidad de transición,
 distribución inicial

 Markov fue alumno de chebyshev igual que Kolmogorov, pero sus contribuciones no fueron tan formales como las de Kolmogorov, por lo que se le considera un precursor de la teoría de procesos estocásticos.
 En aquellos tiempos los procesos que se estudiaban eran principalmente procesos a tiempo discreto, y el enfoque era más probabilístico que analítico. Sin embargo, con el tiempo, la teoría de procesos estocásticos se ha desarrollado y se ha formalizado, y ahora incluye tanto procesos a tiempo discreto como a tiempo continuo, así como una amplia variedad de aplicaciones en diferentes campos.

Considere un sistema que puede caracterizarse por estar en cualquiera de
un conjunto de estados previamente especificado. Suponga que el sistema
evoluciona o cambia de un estado a otro a lo largo del tiempo de acuerdo con
una cierta ley de movimiento, y sea Xt el estado del sistema al tiempo t. Si
se considera que la forma en la que el sistema evoluciona no es determinista,
sino provocada por alg´un mecanismo azaroso, entonces puede considerarse
que Xt es una variable aleatoria para cada valor del ´ındice t. Esta colecci´on
de variables aleatorias es la definici´on de proceso estoc´astico, y sirve como
modelo para representar la evoluci´on aleatoria de un sistema a lo largo del
tiempo. En general, las variables aleatorias que conforman un proceso no
son independientes entre s´ı, sino que est´an relacionadas unas con otras de
alguna manera particular. Las distintas formas en que pueden darse estas
dependencias es una de las caracter´ısticas que distingue a unos procesos
de otros. M´as precisamente, la definici´on de proceso estoc´astico toma como
base un espacio de probabilidad Ω, F , P y puede enunciarse de la siguiente
forma.
Definici´on 1.1 Un proceso estoc´astico es una colecci´on de variables aleato-
rias Xt : t T parametrizada por un conjunto T , llamado espacio parame-
tral, en donde las variables toman valores en un conjunto S llamado espacio
de estados.
En los casos m´as sencillos se toma como espacio parametral el conjunto
discreto T 0, 1, 2, . . . y estos n´umeros se interpretan como el tiempo visto en pasos. En 
este caso se dice que el proceso es a tiempo discreto, y en general este tipo
de procesos se denotar´a por Xn : n 0, 1, . . . , as´ı, para cada n, Xn es el valor del proceso o estado del sistema al tiempo n.
Este modelo corresponde a un vector aleatorio de dimensi´on infinita. El espacio parametral puede tambi´en tomarse como el conjunto continuo
. Se dice entonces que el proceso es a tiempo continuo, y se
T 0, denotar´a por
Xt : t 0.
Por lo tanto, seguiremos la convenci´on de que si el sub´ındice es n, entonces
los tiempos son discretos, y si el sub´ındice es t, el tiempo se mide de manera
continua. Los posibles espacios de estados que consideraremos son subcon-
juntos de Z, y un poco m´as generalmente tomaremos como espacio de esta-
dos el conjunto de n´umeros reales R, aunque en algunos pocos casos tam-
bi´en consideraremos a Zn o Rn. Naturalmente, espacios m´as generales son
posibles, tanto para el espacio parametral como para el espacio de estados.
En particular, para poder hablar de variables aleatorias con valores en el
espacio de estados S, es necesario asociar a este conjunto una σ-´algebra.

Diremos que el proceso estocástico es una cadena cuando

Ejemplos 
Anotar la sucesion de resultados de un dado-
Observar el precio de una acción en la bolsa a lo largo del tiempo
El dinero en nuestra cartera cada d´ıa
Nuestra situación sentimental cada día (hacer un diagrama de cadena)
El decil al que pertenece cada primogénito de nuestra familia
Registrar la temperatura ambiente cada hora durante un d´ıa
Medir la estatura de una persona cada a˜no
Medir la cantidad de habitantes de una población
El movimiento de una partícula en un fluido (ojo, el espacio de estados es R2 o R3)

Estamos interesados en estudiar la probabilidad de que el proceso tome ciertos valores o estados, y para esto es necesario conocer la distribución de probabilidad de las variables aleatorias que conforman el proceso.
En particular, es importante conocer la distribución inicial del proceso, es decir, la distribución de X0, así como las probabilidades de transición entre estados, que describen cómo evoluciona el proceso a lo largo del tiempo. Estas probabilidades de transición pueden depender del estado actual del proceso, lo que da lugar a diferentes tipos de procesos estocásticos con distintas propiedades y comportamientos.

Consideremos el primer ejemplo, la sucesión de resultados de un dado. En este caso, el espacio parametral es T = N, ya que estamos observando los resultados en pasos discretos (cada lanzamiento del dado), y el espacio de estados es E = {1, 2, 3, 4, 5, 6}, que son los posibles resultados del dado. La distribución inicial del proceso podría ser uniforme, es decir, cada resultado tiene una probabilidad de 1/6. 
Ejemplos de probabilidades en las que estamos interesados para este fenomeno son:
- La probabilidad de obtener un 6 en el tercer lanzamiento, es decir, P(X3 = 6).
- La probabilidad de que al final de la primera ronda de 5 lanzamientos ya haya salido al menos un 7
- Una probabilidad condicional dado el estado anterior (probabilidad de transición)

--seleccionar algunos ejemplos de arriba y formular preguntas interesantes de cada uno que se puedan poner como probabilidades, de transición, iniciales 

El ejemplo de las clases sociales puede servir para preguntarnos cual es la proba de que una persona tomada al azar tenga un nieto que pertenezca a la clase alta. Para esto tenemos que considerar la distribución de la población en este momento, o sea la ley de X_0

Un proceso estoc´astico, tambi´en llamado proceso aleatorio, puede conside-
rarse como una funci´on de dos variables
X : T Ω S
tal que a la pareja t, ω se le asocia el valor o estado X t, ω , lo cual
tambi´en puede escribirse como Xt ω . Para cada valor de t en T , el mapeo
ω Xt ω es una variable aleatoria, mientras que para cada ω en Ω fijo,
la funci´on t Xt ω es llamada una trayectoria o realizaci´on del proceso.

En este curso T ser´a un subconjunto de R. Los casos m´as comunes
T discreto (Procesos a tiempo discreto): T= N, T= {0,1,2,...}, T= Z.
T continuo (Procesos a tiempo continuo): T = [0,1], T = [0,∞), T= R.
En cuanto a los valores del proceso llamaremos Eal espacio de estados y consideraremos tambi´en dos
casos:
Valores discretos, por ejemplo E= {0,1,2,...}, E= N o E= Z
Valores continuos, por ejemplo E= [0,∞), E= R, etc


Sean {Yi,i∈N}una sucesi´on de variables aleatorias independientes e id´enticamente distribuidas, definidas
sobre un espacio de probabilidad (Ω,F; P) y que toman valores en los enteros E= Z; denotaremos por
pY la distribuci´on de Yi, es decir pY(x) = P(Yi = x),x∈Z. Consideremos la sucesi´on
Xn =
n
Yi, n∈N.

Este proceso estocástico se llama proceso de caminata aleatoria o proceso de suma acumulada, y es un ejemplo de proceso a tiempo discreto con valores enteros. En este caso, el espacio parametral es T = N y el espacio de estados es E = Z. La distribución inicial del proceso se puede determinar a partir de la distribución de las variables aleatorias Yi, ya que X0 = Y0. La probabilidad de transición entre estados se puede calcular utilizando la distribución de las variables aleatorias Yi, ya que Xn+1 = Xn + Yn+1. Este tipo de proceso es fundamental en la teoría de procesos estocásticos y tiene aplicaciones en diversas áreas como la física, la economía y la biología.

Ejemplo Y_i toma valor 1 y -1, cada uno con probabilidad 1/2, entonces el proceso Xn es una caminata aleatoria simétrica en los enteros, donde en cada paso se mueve hacia la derecha (incremento de 1) o hacia la izquierda (decremento de 1) con igual probabilidad. Este proceso es un modelo clásico para estudiar fenómenos como la difusión, el movimiento browniano y otros procesos de transporte en física, así como para modelar precios de activos financieros en economía.

Desarrollar el ejemplo y calcular algunas probabilidades...




Clase 2

Hablando informalmente, un proceso de Markov es un proceso aleatorio con la propiedad de que dado
el valor actual del proceso Xt, los valores futuros Xs para s>tson independientes de los valores pasados
Xu para u<t. Es decir, que si tenemos la informaci´on del estado presente del proceso, saber c´omo lleg´o
al estado actual no afecta las probabilidades de pasar a otro estado en el futuro.