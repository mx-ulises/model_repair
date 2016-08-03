import sys
owfn_path = "../../"
sys.path.append(owfn_path)

from model_repair.logger import LOG
from model_repair.petri_net import PetriNet

model = PetriNet()

""" Adding places and transitions """
model.add_place("a")
model.add_place("b")
model.add_transition("t_1")
model.add_transition("t_2")

""" Adding flow"""
model.change_input_flow("a", "t_1", 1)
model.change_output_flow("b", "t_1", 1)

model.change_input_flow("b", "t_2", 1)
model.change_output_flow("a", "t_2", 1)

""" Generates a LoLA file """
print model.export_lola({"a": 1})
