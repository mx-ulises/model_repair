import sys
owfn_path = "/home/pollo/repos/model_repair/lib"
sys.path.append(owfn_path)

from logger import LOG
import ctl

a = ctl.CTLAtomicProposition("a")
b = ctl.CTLAtomicProposition("b")

phi_1 = ctl.CTLAnd(a, b)
phi_2 = ctl.CTLNegatedExistGlobally(phi_1)
LOG.info(phi_2.print_lola())
