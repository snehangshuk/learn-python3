# Here + operator is modified to add to atoms to create a new salt
class Atom:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return self.label

    def __add__(self, other):
        return Molecule([self, other])

    def __sub__(self, other):
        return Molecule([self]), Molecule([other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __repr__(self):
        return str(self.atoms)


sodium = Atom("Na")
chlorine = Atom("Cl")
# salt = Molecule([sodium, chlorine])
# print("Original Salt: " + str(salt))
newsalt = sodium + chlorine
print("New Salt: " + str(newsalt))
atom1, atom2 = sodium - chlorine
print(f"Atoms after substraction: {atom1}, {atom2}")