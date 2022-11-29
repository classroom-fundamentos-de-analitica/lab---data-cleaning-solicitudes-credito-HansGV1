"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    # Lectura de datos MyFrame y orden
    MyFrame = pd.read_csv("solicitudes_credito.csv", sep=";")
    MyFrame.dropna(axis = 0, inplace = True)
    MyFrame.drop_duplicates(inplace = True)
    # Fechas
    MyFrame.fecha_de_beneficio = pd.to_datetime(MyFrame.fecha_de_beneficio, infer_datetime_format = True, errors = "ignore", dayfirst = True)
    MyFrame.fecha_de_beneficio = MyFrame.fecha_de_beneficio.dt.strftime("%Y/%m/%d")
    MyFrame = MyFrame.drop(['Unnamed: 0'], axis=1)
    # Arreglo headers & replace
    MyFrame[["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]] = MyFrame[["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    MyFrame = MyFrame.replace(to_replace="(_)|(-)", value=" ", regex=True)    
    MyFrame = MyFrame.replace(to_replace="[,$]|(\.00$)", value="", regex=True)
    # Cast de tipo de datos necesarios 
    MyFrame.monto_del_credito = MyFrame.monto_del_credito.astype("int")
    MyFrame.comuna_ciudadano = MyFrame.comuna_ciudadano.astype("float")
    MyFrame.drop_duplicates(inplace = True)

    return MyFrame
