import sys
owfn_path = "../../"
sys.path.append(owfn_path)

from model_repair.logger import LOG
from model_repair.petri_net import PetriNet

model = PetriNet()

""" Proccess 'a' """
model.add_place("a_1")
model.add_place("a_2")

model.add_transition("t_1")
model.change_input_flow("a_1", "t_1", 1)
model.change_output_flow("a_2", "t_1", 1)

model.add_transition("t_2")
model.change_input_flow("a_2", "t_2", 1)
model.change_output_flow("a_1", "t_2", 1)

""" Proccess 'b' """
model.add_place("b_1")
model.add_place("b_2")

model.add_transition("t_3")
model.change_input_flow("b_1", "t_3", 1)
model.change_output_flow("b_2", "t_3", 1)

model.add_transition("t_4")
model.change_input_flow("b_2", "t_4", 1)
model.change_output_flow("b_1", "t_4", 1)

""" Initial marking:
        m_0(a_1) = m_0(b_1) = 1
        m_0(a_2) = m_0(b_2) = 0
"""
m_0 = {"a_1": 1, "b_1": 1}

""" Get Reachability Set """
model.reachability_set(m_0)
