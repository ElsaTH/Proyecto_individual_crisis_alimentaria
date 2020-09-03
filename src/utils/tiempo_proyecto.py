import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import pyplot




def tiempo_proyecto(Tiempo):
    """
    Generar un gráfico circular con el tiempo necesario para cada sección de los pasos del proyecto
    """
    #Tiempo = (2,2,0.5,1,3,1,1)  # lo he generado en días
    pyplot.pie(Tiempo,colors=["#EBDEF0","#C39BD3","#58D68D","#D6EAF8","#C39BD3","#F9E79F","#58D68D"], labels=["Tema","Datos","Hipotesis","Limpieza","Graficos","Api","Explicacion"],startangle = 90, autopct = '%1.1f%%', explode = (0.1,0.1 , 0.1,0.1,0.1,0.1,0.1))
    plt.axis('equal', size=14, color="#5A5034")
    plt.title("Tiempo empleado para el proyecto:", size=25, color="#5A5034")
    plt.tight_layout()
    plt.savefig('Tiempo_proyecto.png')
    return plt.show() 

tiempo_proyecto(Tiempo = (2,2,0.5,1,3,1,1))
