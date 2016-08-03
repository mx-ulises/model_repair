import sys
owfn_path = "../../"
sys.path.append(owfn_path)

from model_repair.logger import LOG
from model_repair.petri_net import PetriNet

model = PetriNet()

""" Loading file"""
model.load_file("example_pn_old.json")

""" Adding an existing place """
model.add_place("a")

""" Adding new place and transition"""
model.add_place("c")
model.add_transition("t_2")

""" Adding new flow """
model.change_input_flow("a", "t_2", 1)
model.change_output_flow("c", "t_2", 1)

""" Saving file"""
model.save_file("example_pn_new.json")
