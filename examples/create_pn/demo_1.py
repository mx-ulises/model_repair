import sys
owfn_path = "/home/pollo/repos/model_repair/lib"
sys.path.append(owfn_path)

from logger import LOG
from petri_net import PetriNet

model = PetriNet()

""" Adding places and transitions """
model.add_place("a")
model.add_place("b")
model.add_transition("t")

""" Adding flow"""
model.change_input_flow("a", "t", 1)
model.change_output_flow("b", "t", 1)

""" Saving file"""
model.save_file("example_pn.json")
