import pandas as pd



# Función para abrir el dataset. Convertimos el csv en dataframe y establecemos que "Year" es tipo fecha:


def fao1():
   """ 
   Primer dataframe de FAO. Recogido en kaggle  --> FAO.csv
   """
   df = pd.read_csv("/Users/Elsa/Desktop/Covid_Agosto/Proyecto_Elsa/Proyecto_individual_Elsa/src/main/FAO.csv",encoding="ISO-8859-1")
    
   return df




def fao2():
   """ 
   Segundo dataframe. Recogido en página oficial de FAO --> Production_Crops_E_All_Data_(Normalized).csv
   """
   df2 = pd.read_csv("/Users/Elsa/Desktop/Covid_Agosto/Proyecto_Elsa/Proyecto_individual_Elsa/src/main/Production_Crops_E_All_Data_(Normalized).csv",encoding="ISO-8859-1",date_parser="Year")

   return df2


def fao3():
   """ 
   Tercer dataframe. Recogido en página oficial de FAO --> FAOSTAT_data_8-10-2020.csv
   """
   df3 = pd.read_csv("/Users/Elsa/Desktop/Covid_Agosto/Proyecto_Elsa/Proyecto_individual_Elsa/src/main/FAOSTAT_data_8-10-2020.csv",encoding="ISO-8859-1",date_parser="Year") 
  
   return df3


def fao4():
   """ 
   Cuarto dataframe. Recogido en página oficial de FAO --> FAOSTAT_Production_Indices_8-10-2020.csv
   """
  
   df4 = pd.read_csv("/Users/Elsa/Desktop/Covid_Agosto/Proyecto_Elsa/Proyecto_individual_Elsa/src/main/FAOSTAT_Production_Indices_8-10-2020.csv",encoding="ISO-8859-1",date_parser="Year")  
   
   return df4