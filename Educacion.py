import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df= pd.read_csv("datoscolombia.csv", encoding = "UTF8")


#barras terminado
plt.bar(df["DEPARTAMENTO"], df["TASA_MATRICULACIÓN_5_16"], color= "red")
plt.title("Matriculas en Colombia")
plt.xticks(rotation=60)
plt.xlabel("DEPARTAMENTO")
plt.ylabel("TASA DE MATRICULACION")
plt.show()



#lineas pendiente
POBLACIÓN_5_16= df["POBLACIÓN_5_16"]
AÑO= [2011, 2012, 2013, 2014, 2015, 2016]

plt.plot(df["AÑO"], df["POBLACIÓN_5_16"] , marker="o", color="red", linestyle="--")
plt.title("Gráfico de Líneas")
plt.xlabel("AÑO")
plt.ylabel("POBLACIÓN_5_16")
plt.show()




#torta terminado pero revisar dato
DEPARTAMENTO = ["Antioquia", "Santander", "Meta"]
COBERTURA_NETA = ["93.85", "92.4", "93.29"]

plt.figure(figsize=(8, 8))
plt.pie(COBERTURA_NETA, labels=DEPARTAMENTO, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'purple'], wedgeprops={'edgecolor': 'black'})
plt.title("Distribución de la Cobertura Neta por Departamento")
plt.show()





#timeseries revisar

plt.figure(figsize=(6, 4))
sns.lineplot(x=df["AÑO"], y=df["TASA_MATRICULACIÓN_5_16"], label="Tasa de Matrícula (5-16 años)", color="blue")
sns.lineplot(x=df["AÑO"], y=df["COBERTURA_NETA"], label="Cobertura Neta", color="green")
sns.lineplot(x=df["AÑO"], y=df["DESERCIÓN"], label="Deserción", color="red")
sns.lineplot(x=df["AÑO"], y=df["COBERTURA_BRUTA_SECUNDARIA"], label="Cobertura Bruta Secundaria", color="orange")
sns.lineplot(x=df["AÑO"], y=df["DESERCIÓN_SECUNDARIA"], label="Deserción Secundaria", color="purple")
sns.lineplot(x=df["AÑO"], y=df["APROBACIÓN_MEDIA"], label="Aprobación Media", color="brown")
plt.title("Evolución de Indicadores Educativos a lo largo de los Años")
plt.xlabel("AÑO")
plt.ylabel("Valor")
plt.legend(loc ="upper left",  bbox_to_anchor=(1, 1)) 
plt.show()





#radar revisar
valores = df["REPROBACIÓN"].tolist()  # Obtener los datos reales de tu DataFrame
Y = df["DEPARTAMENTOS"].tolist() 
if len(valores) != len(Y):
    raise ValueError
valores += valores[:1]  # Añadir el primer valor al final para cerrar el gráfico
ángulos = np.linspace(0, 2 * np.pi, len(Y), endpoint=False).tolist()
ángulos += ángulos[:1]
plt.figure(figsize=(6, 6))
plt.polar(ángulos, valores, marker='o', color='red', linewidth=2)
plt.fill(ángulos, valores, color='red', alpha=0.25)
plt.title("Gráfico de Radar")
plt.xticks(ángulos[:-1], Y)  # Etiquetas en la gráfica
plt.show()