import sys
owfn_path = "../../"
sys.path.append(owfn_path)

from model_repair.logger import LOG
from model_repair.petri_net import PetriNet
import model_repair.ctl

model = PetriNet()

""" Adding places, transitions and flow for 'P'"""
model.add_place("p_iddle")
model.add_place("p_active")
model.add_transition("t_1")
model.add_transition("t_2")
model.change_input_flow("p_iddle", "t_1", 1)
model.change_output_flow("p_active", "t_1", 1)
model.change_input_flow("p_active", "t_2", 1)
model.change_output_flow("p_iddle", "t_2", 1)

""" Adding places, transitions and flow for 'P'"""
model.add_place("q_iddle")
model.add_place("q_active")
model.add_transition("t_3")
model.add_transition("t_4")
model.change_input_flow("q_iddle", "t_3", 1)
model.change_output_flow("q_active", "t_3", 1)
model.change_input_flow("q_active", "t_4", 1)
model.change_output_flow("q_iddle", "t_4", 1)

""" Initial Marking """
m_0 = {"p_iddle": 1, "q_iddle": 1}

""" Generates CTL formula """
a = ctl.CTLAtomicProposition("p_active")
b = ctl.CTLAtomicProposition("q_active")

phi_1 = ctl.CTLAnd(a, b)
TRUE = ctl.TRUE
phi_2 = ctl.CTLNegatedExistUntil(TRUE, phi_1)

LOG.info("===================================================================")
model.model_checking(m_0, phi_2)
LOG.info("===================================================================")
model.model_checking(m_0, phi_2.negate())
