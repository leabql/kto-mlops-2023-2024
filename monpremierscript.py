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

import unittest
"""
Count names with more than seven letters
"""
def count_nb_names(prenoms: list):
    more_than_seven = 0
    nb_letters = 7
    for prenom in prenoms:
        if len(prenom) > nb_letters:
            more_than_seven += 1
            print("Prenom supérieur à", nb_letters,  ": " + prenom)
        else:
            print("Prenom inférieur ou égal à", nb_letters,  ": " + prenom)
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms supérieurs à 7 : " + str(count_nb_names(prenoms=prenoms)))

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_nb_names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()