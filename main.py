import requests
import funciones as f

if __name__ == "__main__":
	url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
	response = requests.get(url)
	rjson = response.json()
	items = rjson["items"]

contestadas, no_contestadas = f.preguntas(items)
idVistasMin = f.vistasMinimas(items)
vieja, nueva = f.antique(items)
mejorRep = f.bestReputation(items)

print ("\nRespuestas contestadas ", contestadas)
print ("\nRespuestas no contestadas ", no_contestadas)
print ("\nID de la pregunta con menos vistas ", idVistasMin)
print ("\nID de la respuesta mas nueva ", nueva)
print ("\nID de la respuesta mas vieja ", vieja)
print ("\nUsuario con mejor reputacion ", mejorRep)


