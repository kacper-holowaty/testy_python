import funkcja


def test_sortowanie():
	owoce=['jabłko','gruszka','śliwka','banan','wiśnia','arbuz','brzoskwinia','malina','granat']
	assert (sortowanie(owoce) == sorted(owoce))

