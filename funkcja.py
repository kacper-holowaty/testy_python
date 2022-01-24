def sortowanie(owoce):
	owoce=['jabłko','gruszka','śliwka','banan','wiśnia','arbuz','brzoskwinia','malina','granat']
	i = 0
	while I < len(owoce):
		j = 0
		while j < len(owoce)-1:
			if owoce[j] > owoce[j+1]:
				tmp = lista[j]
				lista[j] = lista[j+1]
				lista[j+1] = tmp
			j += 1
		i += 1
	return lista
