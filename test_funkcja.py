import funkcja as cdb


def test_sortowanie():
	owoce=['jabłko','gruszka','śliwka','banan','wiśnia','arbuz','brzoskwinia','malina','granat']
	assert (cdb.sortowanie(owoce) == sorted(owoce))

