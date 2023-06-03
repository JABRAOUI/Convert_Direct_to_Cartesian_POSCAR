from pymatgen.core.structure import Structure
from pymatgen.io.vasp.inputs import Poscar
poscar = Poscar.from_file("CONTCAR")
structure = Structure(lattice=poscar.structure.lattice,
                      species=poscar.structure.species,
                      coords=poscar.structure.cart_coords)
poscar.comment = "Cartesian configuration"
poscar.structure = structure
poscar.write_file("POSCAR_cartesian")
file_path = "POSCAR_cartesian"
w1 = "direct"
w2 = "Cartesian"
with open(file_path, 'r') as f:
    file_contents = f.read()
new_contents = file_contents.replace(w1, w2)
with open(file_path, 'w') as f:
    f.write(new_contents)

