import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import mining_data_tb
from folder_tb import fao1, fao2, fao3, fao4



def production_Spain(Spain_total):
    """
    Gráfica producción en España desde 1961 a 2013
    """
    plt.figure(figsize=(20, 10))
    Spain_total.plot(kind="line",label='España desde 1961 a 2013', color="#138D75", linewidth=3)
    plt.legend(title="Producción en 1000 toneladas",loc='top_left',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    #plt.title('Desde 1961 a 20013', size=20, color="#5A5034")
    plt.suptitle('PRODUCCIÓN EN ESPAÑA desde 1961 a 2013', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida por año",size=20, color="#5A5034")
    plt.ylabel("Producción",size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=12,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    #plt.savefig('Producción_España_desde1961.png')
    plt.show()
#production_Spain(mining_data_tb.production_years(fao1()))



def production_Spain_10years(Spain_years):
    """
    Gráfica de producción en España desde 2003 a 2013
    """
    plt.figure(figsize=(20, 10))
    Spain_years.plot(kind="line",label='España desde 2003 a 2013', color="#138D75",linewidth=3)
    plt.legend(title="Intersección de la gráfica en 2008. Producción en 1000 toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA de 2003 a 2013', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida por año", size=20, color="#5A5034")
    plt.ylabel("Producción",size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=12,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    plt.plot([5,5],[127500,145000],'k-', lw=3, color="#F8C471")
    #plt.savefig('Producción_España_2003-13.png')
    plt.show()
#production_Spain_10years(mining_data_tb.production_10_years(fao1()))

def comparation_production_Spain(Spain_produ):
    """
    Comparación de producción en España año 2007-2008-2012
    """
    plt.figure(figsize=(20, 10))
    Spain_produ.Y2007.plot(kind="line",label='Año 2007', color="#76D7C4")
    Spain_produ.Y2008.plot(kind="line",label='Año 2008', color="#F8C471")
    Spain_produ.Y2012.plot(kind="line",label='Año 2012',color="c")
    plt.legend(title="Producción en 1000 toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('COMPARACIÓN DE PRODUCCIÓN EN ESPAÑA', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=10,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    #plt.savefig('Comparación_Producción_España.png')
    plt.show()
#comparation_production_Spain(mining_data_tb.critical_years(fao1()))

def production_Spain2007(Spain_produ):
    """
    Gráfica de la producción en España año 2007 de todos los alimentos
    """
    plt.figure(figsize=(20, 10))

    Spain_produ.Y2007.plot(kind="bar",label='Todos los productos en 2007',align='center',color="#E2B553")

    plt.legend(title="Producción en 1000 toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA 2007', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Producción_España2007.png')
    plt.show()
#production_Spain2007(mining_data_tb.production_by_years(fao1()))


def production_Spain2008(Spain_produ):
    """
    Gráfica de la producción en España año 2008 de todos los alimentos
    """
    plt.figure(figsize=(20, 10))
    Spain_produ.Y2008.plot(kind="bar",label='Todos los productos en 2008',align='center', color="#909F43")
    plt.legend(title="Producción en 1000 toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA 2008', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    #plt.savefig('Producción_España2008.png')
    plt.show()
#production_Spain2008(mining_data_tb.production_by_years(fao1()))

def production_Spain2012(Spain_produ):
    """
    Gráfica de la producción en España año 2012 de todos los alimentos
    """
    plt.figure(figsize=(20, 10))
    Spain_produ.Y2012.plot(kind="bar",label='Todos los productos en 2012',align='center',color="#F6D573")
    plt.legend(title="Producción en 1000 toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA 2012', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    #plt.savefig('Producción_España2012.png')
    plt.show()
#production_Spain2012(mining_data_tb.production_by_years(fao1()))

def production_Spain2(year2):
    """
    Gráfica producción en España desde 1961 a 2013
    """
    plt.figure(figsize=(20, 10))
    year2.plot(kind="line",label='España desde 1961 a 2018', color="#138D75", linewidth=3)
    plt.legend(title="Producción en 1000 toneladas",loc='top_left',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA desde 1961', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida por año",size=20, color="#5A5034")
    plt.ylabel("Producción",size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=14,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Producción_España_desde1961_2018_FAO.png')
    plt.show()
#production_Spain2(mining_data_tb.production_years2(fao2()))

def comparation_production_Spain2(year2007,year2008,year2012):
    """
    Comparación de producción en España año 2007-2008-2012
    """  
    plt.figure(figsize=(20, 10))

    year2007.Value.plot(kind="line",label='Año 2007', color="#76D7C4")
    year2008.Value.plot(kind="line",label='Año 2008', color="#F8C471")
    year2012.Value.plot(kind="line",label='Año 2012',color="c")

    plt.legend(title="Producción en 1000 toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('COMPARACIÓN DE PRODUCCIÓN EN ESPAÑA', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=45,FontSize=12,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Comparación_Producción_España_FAO.png')
    plt.show()
#comparation_production_Spain2(mining_data_tb.critical_years2007(fao2()),mining_data_tb.critical_years2008(fao2()),mining_data_tb.critical_years2012(fao2()))



def production_Spain2007_2(year2007):
    """
    Gráfica de la producción en España año 2007 de todos los alimentos
    """
    plt.figure(figsize=(20, 10))
    year2007.Value.plot(kind="bar",label='Todos los productos en 2007',align='center',color="#E2B553")

    plt.legend(title="Producción toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA 2007', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Producción_España2007_FAO.png')
    plt.show()
#production_Spain2007_2(mining_data_tb.critical_years2007(fao2()))

def production_Spain2008_2(year2008):
    """
    Gráfica de la producción en España año 2007 de todos los alimentos
    """
    plt.figure(figsize=(20, 10))
    year2008.Value.plot(kind="bar",label='Todos los productos en 2008',align='center', color="#909F43")

    plt.legend(title="Producción toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA 2008', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=8,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Producción_España2008_FAO.png')
    plt.show()
#production_Spain2008_2(mining_data_tb.critical_years2008(fao2()))

def production_Spain2012_2(year2012):
    """
    Gráfica de la producción en España año 2007 de todos los alimentos
    """
    plt.figure(figsize=(20, 10))
    year2012.Value.plot(kind="bar",label='Todos los productos en 2012',align='center',color="#F6D573")

    plt.legend(title="Producción en toneladas",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRODUCCIÓN EN ESPAÑA 2012', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Producción", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Producción_España2012_FAO.png')
    plt.show()
#production_Spain2012_2(mining_data_tb.critical_years2012(fao2()))

def price_production_Spain_line(year_price_2007,year_price_2008,year_price_2012):
    """
    Gráfica de comparacion de precio-producción en España
    """
    plt.figure(figsize=(20, 10))

    year_price_2007.Value.plot(kind="line",label='Año 2007', color="#76D7C4")
    year_price_2008.Value.plot(kind="line",label='Año 2008', color="#F8C471")
    year_price_2012.Value.plot(kind="line",label='Año 2012',color="c")

    plt.legend(title="Precio producto (LCU/tonelada)",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('COMPARACIÓN DE PRECIO-PRODUCCIÓN EN ESPAÑA', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Precio producto (LCU/tonelada)", size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=12,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Comparación_Precio-Producción_España_FAO.png')
    plt.show()
#price_production_Spain_line(mining_data_tb.price_production_spain2007(fao3()),mining_data_tb.price_production_spain2008(fao3()),mining_data_tb.price_production_spain2012(fao3()))

def price_production_Spain2007(year_price_2007):
    """
    Gráfica de comparacion de precio-producción en España año 2007
    """
    plt.figure(figsize=(20, 10))

    year_price_2007.Value.plot(kind="bar",label='Todos los productos en 2007',align='center',color="#E2B553")

    plt.legend(title="Precio producto (LCU/tonelada)",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRECIO-PRODUCCIÓN EN ESPAÑA 2007', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Precio producto (LCU/tonelada)", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Precio-Producción_España2007_FAO.png')
    plt.show()
#price_production_Spain2007(mining_data_tb.price_production_spain2007(fao3()))

def price_production_Spain2008(year_price_2008):
    """
    Gráfica de comparacion de precio-producción en España año 2008
    """
    plt.figure(figsize=(20, 10))
    year_price_2008.Value.plot(kind="bar",label='Todos los productos en 2008',align='center', color="#909F43")

    plt.legend(title="Precio producto (LCU/tonelada)",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRECIO-PRODUCCIÓN EN ESPAÑA 2008', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Precio producto (LCU/tonelada)", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Precio-Producción_España2008_FAO.png')
    plt.show()
#price_production_Spain2008(mining_data_tb.price_production_spain2008(fao3()))


def price_production_Spain2012(year_price_2012):
    """
    Gráfica de comparacion de precio-producción en España año 2012
    """
    plt.figure(figsize=(20, 10))
    year_price_2012.Value.plot(kind="bar",label='Todos los productos en 2012',align='center',color="#F6D573")

    plt.legend(title="Precio producto (LCU/tonelada)",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('PRECIO-PRODUCCIÓN EN ESPAÑA 2012', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Precio producto (LCU/tonelada)", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=6,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")

    #plt.savefig('Precio-Producción_España2012_FAO.png')
    plt.show()
#price_production_Spain2012(mining_data_tb.price_production_spain2012(fao3()))



def price_production_Spain_bar(df3):
    plt.figure(figsize=(20, 10))
    df3[df3.Year == 2007].Value.plot(kind="bar",label='Precio 2007',color="#76D7C4")
    df3[df3.Year == 2008].Value.plot(kind="bar",label='Precio 2008',color="#F8C471")
    df3[df3.Year == 2012].Value.plot(kind="bar",label='Precio 2012',color="#E67C00")
    plt.legend(title="Precio producto (LCU/tonelada)",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)
    plt.suptitle('COMPARACIÓN DE PRECIO-PRODUCCIÓN EN ESPAÑA', size=25, color="#5A5034")
    plt.xlabel("Materia prima producida", size=20, color="#5A5034")
    plt.ylabel("Precio producto (LCU/tonelada)", size=20, color="#5A5034")
    plt.xticks(rotation=90,FontSize=8,color="#5A5034")
    plt.yticks(rotation=0,FontSize=12,color="#5A5034")
    #plt.savefig('Precio-Producción_España_anual_FAO.png')
    plt.show()
#price_production_Spain_bar(mining_data_tb.price_production_Spain(fao3()))

def production_agrupation(year2007,year2008,year2012):
    x = np.arange(len(year2007.Item))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(15, 10))
    ax.bar(x - width/3, year2007.Value, width, label='Precio-Producción 2007', color="#E2B553")
    ax.bar(x + width/3, year2008.Value, width, label='Precio-Producción 2008', color="#909F43")
    ax.bar(x + width*3/3, year2012.Value, width, label='Precio-Producción 2012', color="#F6D573")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Producción/Precio en $", size=20, color="#5A5034")
    ax.set_xlabel("Materia prima producida", size=20, color="#5A5034")
    ax.set_title('COMPARACIÓN DE PRECIO-PRODUCCIÓN EN ESPAÑA', size=20, color="#5A5034")
    ax.set_xticks(x)
    ax.set_xticklabels(year2007.Item,rotation=0)
    ax.legend(title="Precio producto (LCU/tonelada)",loc='top_right',edgecolor="#5A5034",facecolor="#EAEDED",framealpha=0.5, fontsize=14)

    fig.tight_layout()
    #plt.savefig('Producción-Precio_07-08-12_España_FAO.png')
    plt.show()

#production_agrupation(mining_data_tb.production_agrupation(fao4())[0],mining_data_tb.production_agrupation(fao4())[1],mining_data_tb.production_agrupation(fao4())[2])

def Outliers_agrupation(df3):
    plt.figure(figsize=(10, 8))
 
    sns.boxplot(x="Year", y="Value", data=df3, palette="pastel")

    plt.suptitle('OUTLIERS POR AGRUPACIÓN DE MATERIAS PRIMAS', size=20, color="#5A5034")
    plt.xlabel("Year", size=20, color="#5A5034")
    plt.ylabel("Value", size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=14,color="#5A5034")
    plt.yticks(rotation=0,FontSize=14,color="#5A5034")
    #plt.savefig('Outliers_agrupación_materias_primas.png')
    plt.show()

#Outliers_agrupation(mining_data_tb.price_production_Spain(fao3()))

def Outliers_materias_primas(df2):
   
    plt.figure(figsize=(10, 8))
    sns.boxplot(x="Year", y="Value", data=df2, palette="pastel")

    plt.suptitle('OUTLIERS DE MATERIAS PRIMAS', size=20, color="#5A5034")
    plt.xlabel("Year", size=20, color="#5A5034")
    plt.ylabel("Value", size=20, color="#5A5034")
    plt.xticks(rotation=0,FontSize=14,color="#5A5034")
    plt.yticks(rotation=0,FontSize=14,color="#5A5034")
    #plt.savefig('Outliers_materias_primas.png')
    plt.show()

#Outliers_materias_primas((mining_data_tb.production_Spain2(fao2)))