from pyrosetta import *

init()
pose = pose_from_pdb("/Users/yangzichen/Documents/PyRosetta/Workshop#0/1rw9.pdb")
ScoreFunction = get_score_function()
score = ScoreFunction(pose)
print(ScoreFunction)
print("This PDB Score in ref15 is:",score)
pymover = PyMOLMover()
pymover.apply(pose)

