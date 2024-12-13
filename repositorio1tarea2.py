# -*- coding: utf-8 -*-
"""Repositorio1Tarea2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UEa-Hr2Sh-2yDBX1dz3Q8FSIUqqvjYYt
"""

def promedio(lista):
  """
  Función que devuelve el promedio de los datos de una lista de números
  ---------------------------------------------
  Input:
    lista: Lista con datos numéricos
  Output:
    prom: Valor del promedio
  """
  i = 0
  for elemento in lista:
   i += elem
  prom = i/(len(lista))
  return prom

def mediana(lista):
  """
  Función que devuelve el valor correspondiente a la mediana de un grupo numérico
  ---------------------------------------------
  Input:
    lista: Lista con datos numéricos
  Output:
    media: Valor de la mediana
  """
  lista = sorted(lista)
  n = len(lista)
  if n%2 == 0:
    meds = []
    med1 = lista[(n//2)-1]
    med2 = lista[n//2]
    meds.append(med1)
    meds.append(med2)
    media = int(promedio(meds))
    return media
  else:
    media = lista[(n//2)]
    return media

def moda(lista):
  """
  Función que regresa una lista con los valores que más se repiten en una lista.
  ---------------------------------------------
  Input:
    lista: Lista con datos numérios
  Output:
    moda: Lista con todos los valores con mayor frecuencia
  """
  dict_conteo = {}

  for elem in lista:
    if elem in dict_conteo:
      dict_conteo[elem] += 1
    else:
      dict_conteo[elem] = 1

  moda = []

  lista_frecs = list(dict_conteo.values())
  lista_datos = list(dict_conteo.keys())
  lista_frecs_sort = sorted(lista_frecs)
  valor_moda = lista_frecs_sort[len(lista_frecs_sort)-1]

  for i in range(0,len(lista_frecs)):
    if lista_frecs[i]==valor_moda:
      moda.append(lista_datos[i])

  return moda

def rango(lista):
  """
  Función que regresa un valor numérico correspondiente a la diferencia entre
  el valor más grande con el valor más pequeño de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numérios
  Output:
    rango: diferencia entre el valor máximo y el mínimo
  """
  lista_sorted = sorted(lista)
  val_min = lista_sorted[0]
  val_max = lista_sorted[-1]

  rango = val_max - val_min

  return rango

def varianza(lista):
  """
  Función que regresa el valor numérico de la varianza de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numérios
  Output:
    varianza: la suma de las desviaciones cuadráticas respecto al promedio, dividido por el número de datos
  """
  x = promedio(lista)
  N = len(lista)
  sum = 0
  for elem in lista:
    wea = (elem-x)**2
    sum += wea

  varianza = (1/N)*(sum)

  return varianza

def desviacion_estandar(lista):
  """
  Función que regresa el valor numérico de la desviación estandar de una lista de datos
  ---------------------------------------------
  Input:
    lista: Lista con datos numéricos
  Output:
    desviacion: La raíz de la varianza
  """
  var = varianza(lista)
  desviacion = (var)**(1/2)
  return desviacion

def rango_intercuartilico(lista):
  """
  Función que calcula el rango intercuartilico de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numéricos
  Output:
    cuartiles: valor numérico correspondiente al rango intercuartílico
  """
  if len(lista)%2==0:
    Q1_index1 = len(lista)//4
    Q1_index2 = Q1_index1-1
    Q3_index1 = (len(lista)*3)//4
    Q3_index2 = Q3_index1-1
    Q1 = (float(lista[Q1_index1]) + float(lista[Q1_index2]))/2
    Q3 = (float(lista[Q3_index1]) + float(lista[Q3_index2]))/2

  else:
    Q1_index = len(lista)//4
    Q3_index = (len(lista)*3)//4
    Q1 = float(lista[Q1_index])
    Q3 = float(lista[Q3_index])

  IQR = Q3-Q1
  return IQR

def MAD(lista):
  """
  Función que calcula la desviación mediana absoluta de una lista de datos
  ---------------------------------------------
  Input:
    lista: lista con datos numéricos
  Output:
    mad: desviación mediana absoluta de la lista
  """
  med = mediana(lista)
  wea = []
  for elem in lista:
    wea.append(abs(elem-med))
  mad = mediana(wea)
  return mad

def covarianza(x,y):
  """
  Función que calcula la covarianza para dos listas con datos numéricos
  ---------------------------------------------
  Input:
    x: lista x con datos numéricos
    y: lista y con datos numéricos
  Output:
    cov: valor numérico correspondiente a la covarianza de x e y
  """
  x_prom = promedio(x)
  y_prom = promedio(y)
  N = len(x)
  sum = 0
  for i,j in zip(x,y):
    sum += ( (i-x_prom)*(j-y_prom) )
  cov = sum/N
  return cov

def coeficiente_correlacion(x,y):
  """
  Función que calcula el coeficiente de correlación entre dos listas con datos numéricos
  ---------------------------------------------
  Input:
    x: lista x con datos numéricos
    y: lista y con datos numéricos
  Output:
    r: valor numérico correspondiente al coeficiente de correlación entre x e y
  """
  covar = covarianza(x,y)
  varx = varianza(x)
  vary = varianza(y)
  r = covar/(varx*vary)
  return r