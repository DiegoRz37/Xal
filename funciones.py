import math

def preguntas(diccionario):
	contestadas = 0
	no_contestadas = 0

	for i in diccionario:
		if i["is_answered"] == True:
			contestadas = contestadas + 1
		else:
			no_contestadas = no_contestadas + 1
	return(contestadas, no_contestadas)

def vistasMinimas(diccionario):
	id_menorVista = 0
	minimo = math.inf
	for i in diccionario:
		if i["view_count"] < minimo:
			minimo = i["view_count"]
			id_menorVista = i["question_id"]
	return(id_menorVista)

def antique(diccionario):

	nueva = 0
	vieja = math.inf
	rvieja =0
	rnueva = 0
	for i in diccionario:
		if i["creation_date"] < vieja:
			vieja = i["creation_date"]
			rvieja = i["question_id"]
		elif i["creation_date"] > nueva:
			nueva = i["creation_date"]
			rnueva = i["question_id"]
	return (rvieja,rnueva)

def bestReputation(diccionario):
	name = "ninguno"
	maxReputation = 0
	for i in diccionario:
		if i["owner"]["reputation"] > maxReputation:
			maxReputation = i["owner"]["reputation"]
			name = i["owner"]["display_name"]
	return(name)





