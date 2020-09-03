import pandas as pd
import numpy as np 
from folder_tb import fao1, fao2, fao3, fao4





def production_years(df):
    """
    Obtenemos la cantidad total de materia prima que España ha producido desde 1961.
    """

    #df = pd.read_csv("FAO.csv",encoding="ISO-8859-1")
    df = df.loc[:,['Area', 'Item', 'Element', 'Unit', 'latitude', 'longitude', 'Y1961',
       'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969',
       'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977',
       'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985',
       'Y1986', 'Y1987', 'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993',
       'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001',
       'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013']]
    year = df.groupby("Area")['Y1961',
       'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969',
       'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977',
       'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985',
       'Y1986', 'Y1987', 'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993',
       'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001',
       'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013'].sum()
    Spain_total = year.loc["Spain",:]

    return Spain_total



def production_10_years(df):
    """
    Crisis en 2008, limpieza de datos de cinco años antes y cinco años despues de la crisis para ver cómo ha sido la evolución.
    """
    #df = pd.read_csv("FAO.csv",encoding="ISO-8859-1")
    df = df.loc[:,['Area', 'Item', 'Element', 'Unit', 'latitude', 'longitude', 'Y1961',
       'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969',
       'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977',
       'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985',
       'Y1986', 'Y1987', 'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993',
       'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001',
       'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013']]
    year = df.groupby("Area")['Y1961',
       'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969',
       'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977',
       'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985',
       'Y1986', 'Y1987', 'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993',
       'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001',
       'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013'].sum()
    Spain_years = year.loc["Spain",['Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013']]

    return Spain_years


def critical_years(df):
    """
    Materias primas producidas en España en 2008. Dicho año, lo comparo con el año 2007 donde se obtuvo el mayor auge y con 2012 donde alcanzó el mínimo antes de la recuperación.
    """

    #df = pd.read_csv("FAO.csv",encoding="ISO-8859-1")
    df = df.loc[:,['Area', 'Item', 'Element', 'Unit', 'latitude', 'longitude', 'Y1961',
       'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969',
       'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977',
       'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985',
       'Y1986', 'Y1987', 'Y1988', 'Y1989', 'Y1990', 'Y1991', 'Y1992', 'Y1993',
       'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001',
       'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009',
       'Y2010', 'Y2011', 'Y2012', 'Y2013']]

    Spain_food = df.loc[:,['Area', 'Item','Y2005','Y2007', "Y2008",'Y2012']]
    Spain_food = Spain_food[Spain_food.Area == 'Spain']
    Spain_produ = Spain_food.groupby(["Item"], as_index=False)['Y2005','Y2007', "Y2008",'Y2012'].sum()
    Spain_produ.set_index("Item", inplace=True)

    return Spain_produ


def production_by_years(df):
    """
    Obtenemos la cantidad total de materia prima que España ha producido desde 1961.
    """
    #df2 = pd.read_csv("Production_Crops_E_All_Data_(Normalized).csv",encoding="ISO-8859-1",date_parser="Year")
    Spain_food = df.loc[:,['Area', 'Item','Y2005','Y2007', "Y2008",'Y2012']]
    Spain_food = Spain_food[Spain_food.Area == 'Spain']
    year = Spain_food.groupby(["Item"], as_index=False)["Y2007", "Y2008",'Y2012'].sum()
    year.set_index("Item", inplace=True)

    return year

def production_years2(df2):
    """
    Obtenemos la cantidad total de materia prima que España ha producido desde 1961.
    """
    #df2 = pd.read_csv("Production_Crops_E_All_Data_(Normalized).csv",encoding="ISO-8859-1",date_parser="Year")
    df2 = df2.loc[:,["Area", "Item", "Element", "Year", "Unit", "Value"]]
    Spain_food2 = df2[df2.Area == 'Spain'] 
    Spain_food2 = Spain_food2[Spain_food2.Element == "Production"]
    year2 = df2.groupby("Year")["Value"].sum()

    return year2


def critical_years2007(df2):
    """
    Materias primas producidas en España en 2007. 
    """
    #df2 = pd.read_csv("Production_Crops_E_All_Data_(Normalized).csv",encoding="ISO-8859-1",date_parser="Year")
    df2 = df2.loc[:,["Area", "Item", "Element", "Year", "Unit", "Value"]]
    Spain_food2 = df2[df2.Area == 'Spain'] 
    Spain_food2 = Spain_food2[Spain_food2.Element == "Production"]  
    year2007= Spain_food2[Spain_food2.Year == 2007]
    year2007 =year2007.loc[:,["Item","Year","Value"]].set_index("Item")
    

    return year2007


def critical_years2008(df2):
    """
    Materias primas producidas en España en 2008. 
    """
    #df2 = pd.read_csv("Production_Crops_E_All_Data_(Normalized).csv",encoding="ISO-8859-1",date_parser="Year")
    df2 = df2.loc[:,["Area", "Item", "Element", "Year", "Unit", "Value"]]
    Spain_food2 = df2[df2.Area == 'Spain'] 
    Spain_food2 = Spain_food2[Spain_food2.Element == "Production"]  
    year2008 = Spain_food2[Spain_food2.Year == 2008]
    year2008 = year2008.loc[:,["Item","Year","Value"]].set_index("Item")

    return year2008


def critical_years2012(df2):
    """
    Materias primas producidas en España en 2008. 
    """
    #df2 = pd.read_csv("Production_Crops_E_All_Data_(Normalized).csv",encoding="ISO-8859-1",date_parser="Year")
    df2 = df2.loc[:,["Area", "Item", "Element", "Year", "Unit", "Value"]]
    Spain_food2 = df2[df2.Area == 'Spain'] 
    Spain_food2 = Spain_food2[Spain_food2.Element == "Production"]  
    year2012 = Spain_food2[Spain_food2.Year == 2012]
    year2012 = year2012.loc[:,["Item","Year","Value"]].set_index("Item")

    return year2012



def price_production_spain2007(df3):
    """
    Precio-Materias primas producidas en España en 2007. 
    """
    #df3 = pd.read_csv("FAOSTAT_data_8-10-2020.csv",encoding="ISO-8859-1",date_parser="Year") 
    df3 = df3.loc[:,["Area","Item","Year","Value"]]
    year_price_2007 = df3[df3.Year == 2007] 
    Spain_price = df3[df3.Area == 'Spain'] 
    year_price_2007= Spain_price[Spain_price.Year == 2007]
    year_price_2007 = year_price_2007.loc[:,["Item","Year","Value"]].set_index("Item")

    return year_price_2007



def price_production_spain2008(df3):
    """
    Precio-Materias primas producidas en España en 2008. 
    """
    #df3 = pd.read_csv("FAOSTAT_data_8-10-2020.csv",encoding="ISO-8859-1",date_parser="Year") 
    df3 = df3.loc[:,["Area","Item","Year","Value"]]
    year_price_2008 = df3[df3.Year == 2008] 
    Spain_price = df3[df3.Area == 'Spain'] 
    year_price_2008 = Spain_price[Spain_price.Year == 2008]
    year_price_2008 = year_price_2008.loc[:,["Item","Year","Value"]].set_index("Item")

    return year_price_2008




def price_production_spain2012(df3):
    """
    Precio-Materias primas producidas en España en 2012. 
    """
    #df3 = pd.read_csv("FAOSTAT_data_8-10-2020.csv",encoding="ISO-8859-1",date_parser="Year") 
    df3 = df3.loc[:,["Area","Item","Year","Value"]]
    year_price_2012 = df3[df3.Year == 2012]  
    Spain_price = df3[df3.Area == 'Spain'] 
    year_price_2012 = Spain_price[Spain_price.Year == 2012]
    year_price_2012 = year_price_2012.loc[:,["Item","Year","Value"]].set_index("Item")

    return year_price_2012

def production_Spain2(df2):
    """
    Función para poder calcular los outliers
    """
    df = df2.loc[:,["Area", "Item", "Year", "Value"]]
    df2= df[df2.Area == 'Spain'].set_index("Year")
    df2 = df2.loc[[2007,2008,2012],:]
    df2.reset_index("Year", inplace=True)
    df2.set_index("Item",inplace=True)

    return df2 

def price_production_Spain(df3):
    df3 = df3.loc[:,["Area","Item","Year","Value"]]
    df3 = df3.set_index("Item")
    return df3


def production_agrupation(df4):
    """
    Precio-Materias primas producidas en España por agrupacion de agricultura, comida, cereales y cultivos en 2007, 2008 y 2012. 
    """

    #df4 = pd.read_csv("FAOSTAT_Production_Indices_8-10-2020.csv",encoding="ISO-8859-1",date_parser="Year") 
    df4 = df4.loc[:,["Area", "Item", "Year", "Value"]]
    year2007= df4[df4.Year == 2007]
    year2008= df4[df4.Year == 2008]
    year2012= df4[df4.Year == 2012]
    year2007.set_index("Year", inplace=True)
    year2008.set_index("Year", inplace=True)
    year2012.set_index("Year", inplace=True)

    return year2007,year2008,year2012

