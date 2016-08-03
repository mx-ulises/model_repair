import sys
owfn_path = "../../"
sys.path.append(owfn_path)

from model_repair.logger import LOG
import model_repair.ctl as ctl

a = ctl.CTLAtomicProposition("a")
b = ctl.CTLAtomicProposition("b")

phi_1 = ctl.CTLAnd(a, b)
phi_2 = ctl.CTLNegatedExistGlobally(phi_1)
LOG.info(phi_2.print_lola())
