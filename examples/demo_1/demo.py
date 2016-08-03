import sys
owfn_path = "../../"
sys.path.append(owfn_path)

from model_repair.logger import LOG
from model_repair.petri_net import PetriNet

model = PetriNet()

""" Adding places and transitions """
model.add_place("a")
model.add_place("b")
model.add_transition("t")

""" Adding flow"""
model.change_input_flow("a", "t", 1)
model.change_output_flow("b", "t", 1)

""" Saving file as JSON file"""
model.save_file("example_pn.json")
