message = "C'est mon premier script"
print(message)

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0 
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print("Prenom supérieur à 7 : " + prenom)
    else:
        print("Prenom inférieur ou égal à 7 : " + prenom)
print("Nombre de prénoms supérieurs à 7 : " + str(more_than_seven))


"""
Count names with more than seven letters
"""
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms supérieurs à 7 : " + str(names(prenoms=prenoms)))

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()