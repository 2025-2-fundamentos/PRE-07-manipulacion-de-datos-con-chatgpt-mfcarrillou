
# %%
# Cargar los datos de la tabla "files/input/drivers.csv" en una variable llamada
# drivers, utilizando pandas
import pandas as pd

drivers = pd.read_csv("../files/input/drivers.csv")

#%%
# Cargar los datos de la tabla "files/input/timesheet.csv" en una variable llamada
# timesheets, utilizando pandas
timesheets = pd.read_csv("../files/input/timesheet.csv")

# %%
# Calcule el promedio de las columnas "hours-logged" y "miles-logged" en la
# tabla timesheets, agrupando los resultados por cada conductor [driverId]
avg_timesheet = timesheets.groupby("driverId")[["hours-logged", "miles-logged"]].mean().reset_index()

#%%
# Cree una tabla llamada "timesheet_with_means" basada en la tabla "timesheet",
# agregando una columna con el promedio de "hours-logged" para cada conductor (driverId). 
timesheet_with_means = timesheets.merge(avg_timesheet[["driverId", "hours-logged"]], on="driverId", suffixes=("", "_mean"))

#%%
# Cree una tabla llamada "timesheet_below" a partir de "timesheet_with_means",
# filtrando los registros donde "hours-logged" sea menor que "mean_hours-logged".
timesheet_below = timesheet_with_means[timesheet_with_means["hours-logged"] < timesheet_with_means["hours-logged_mean"]]