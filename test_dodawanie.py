import dodawanie as cdb

def test_dodawanie():
	a = 14
	b = 20
	assert (cdb.dodawanie(a,b) == a+b)
