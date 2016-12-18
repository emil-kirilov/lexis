import pickle
text = "sadsa"
with open('test.pk', 'wb') as fin:
	pickle.dump(text, fin)