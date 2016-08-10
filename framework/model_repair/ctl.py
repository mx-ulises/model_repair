"""
================================================================================
                              DESCRIPTION
================================================================================

  This is module includes all the classes for each CTL operator to create
  CTL sintax trees.

================================================================================
                              MAINTAINERS
================================================================================

  This section contains all the maintainers primary information to get track of
  the contributors to this code in the file. The maintainer's list contains a
  maintainer alias (required), his name (optional) and contact mails (one
  required).


  Alias     Name              Mail
--------------------------------------------------------------------------------
  ulisesma  Ulises Martinez   ulises.martinezaraiza.mx@ieee.org
                              umartinez@gdl.cinvestav.mx


================================================================================
                              CHANGE LOG
================================================================================

      Version: 0.1
  Last Update: 27-03-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  06-02-2016  ulisesma   Initial file creation
  07-02-2016  ulisesma   Adding the unary operators classes
  11-02-2016  ulisesma   Adding the binary operators classes
  27-03-2016  ulisesma   Modifying some LoLA formulae
  27-03-2016  ulisesma   Some classes specified as singleton

"""

from error_handling import CTLException
from logger import LOG
from singleton import Singleton

class CTLFormula(object):
    """ Class to represent a general CTL """

    def __init__(self):
        """ Constructor of general CTL formula """
        pass


    def print_lola(self):
        """ Print function of a general CTL formula """
        pass


    def negate(self):
        """ Negate the current CTL formula """
        pass


"""
================================================================================
                              TERMINAL OPERATORS
================================================================================

This section includes the following CTL terminal operators:
    * True: The true operator
    * False: The false operator
    * Atomic Proposition: The atomic proposition operator for an specific place
    * Negated Atomic Propositon: The negated atomic proposition operator for an
                                 specific place.
"""


class CTLTrue(CTLFormula):
    """ Class to represent the True operator """
    __metaclass__ = Singleton

    def __init__(self):
        self._operator = "TRUE"
        LOG.info("New TRUE predicate created")


    def print_lola(self):
        return self._operator


    def negate(self):
        """ Negate the current CTL formula """
        return CTLFalse()


class CTLFalse(CTLFormula):
    __metaclass__ = Singleton
    """ Class to represent the False operator """

    def __init__(self):
        self._operator = "FALSE"
        LOG.info("New FALSE predicate created")


    def print_lola(self):
        return self._operator


    def negate(self):
        return CTLTrue()


TRUE = CTLTrue()
FALSE = CTLFalse()

class CTLAtomicProposition(CTLFormula):
    """ Class to represent the Atomic Proposition operator """

    def __init__(self, place):
        if not isinstance(place, basestring):
            err_message = "Place provided is not an string"
            raise CTLException(err_message)
        self._place = place
        LOG.info("New atomic proposition predicate created")


    def print_lola(self):
        return "{0} > 0".format(self._place)


    def negate(self):
        """ Negate the current CTL formula """
        return CTLNegatedAtomicProposition(self._place)


class CTLNegatedAtomicProposition(CTLFormula):
    """ Class to represent the Negated Atomic Proposition operator """

    def __init__(self, place):
        if not isinstance(place, basestring):
            err_message = "Place provided is not an string"
            raise CTLException(err_message)
        self._place = place
        LOG.info("New negated atomic proposition predicate created")


    def print_lola(self):
        return "{0} == 0".format(self._place)


    def negate(self):
        """ Negate the current CTL formula """
        return CTLAtomicProposition(self._place)


"""
================================================================================
                              UNARY OPERATORS
================================================================================

This section includes the following CTL unary operators:
    * Exist Next
    * Negated Exist Next
    * Exist Globally
    * Negated Exist Globally
"""


class CTLExistNext(CTLFormula):
    """ Class to represent the Exist Next operator """

    def __init__(self, phi):
        if not isinstance(phi, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi = phi
        LOG.info("New exist next predicate created")


    def print_lola(self):
        return "EX({0})".format(self._phi.print_lola())


    def negate(self):
        """ Negate the current CTL formula """
        return CTLNegatedExistNext(self._phi)


class CTLNegatedExistNext(CTLFormula):
    """ Class to represent the Negated Exist Next operator """

    def __init__(self, phi):
        if not isinstance(phi, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi = phi
        LOG.info("New negated exist next predicate created")


    def print_lola(self):
        return "NOT(EX({0}))".format(self._phi.print_lola())


    def negate(self):
        """ Negate the current CTL formula """
        return CTLExistNext(self._phi)


class CTLExistGlobally(CTLFormula):
    """ Class to represent the Exist Globally operator """

    def __init__(self, phi):
        if not isinstance(phi, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi = phi
        LOG.info("New exist globally predicate created")


    def print_lola(self):
        return "EG({0})".format(self._phi.print_lola())


    def negate(self):
        """ Negate the current CTL formula """
        return CTLNegatedExistGlobally(self._phi)


class CTLNegatedExistGlobally(CTLFormula):
    """ Class to represent the Negated Exist Globally operator """

    def __init__(self, phi):
        if not isinstance(phi, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi = phi
        LOG.info("New negated exist globally predicate created")


    def print_lola(self):
        return "NOT(EG({0}))".format(self._phi.print_lola())


    def negate(self):
        """ Negate the current CTL formula """
        return CTLExistGlobally(self._phi)


"""
================================================================================
                              BINARY OPERATORS
================================================================================

This section includes the following CTL binary operators:
    * Exist Until
    * Negated Exist Until
    * And
    * Negated And
"""


class CTLAnd(CTLFormula):
    """ Class to represent the And operator """

    def __init__(self, phi_1, phi_2):
        if not isinstance(phi_1, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        if not isinstance(phi_2, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi_1 = phi_1
        self._phi_2 = phi_2
        LOG.info("New and predicate created")


    def print_lola(self):
        lola_phi_1 = self._phi_1.print_lola()
        lola_phi_2 = self._phi_2.print_lola()
        return "({0} AND {1})".format(lola_phi_1, lola_phi_2)


    def negate(self):
        """ Negate the current CTL formula """
        return CTLNegatedAnd(self._phi_1, self._phi_2)


class CTLNegatedAnd(CTLFormula):
    """ Class to represent the Negated And operator """

    def __init__(self, phi_1, phi_2):
        if not isinstance(phi_1, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        if not isinstance(phi_2, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi_1 = phi_1
        self._phi_2 = phi_2
        LOG.info("New negated and predicate created")


    def print_lola(self):
        lola_phi_1 = self._phi_1.print_lola()
        lola_phi_2 = self._phi_2.print_lola()
        return "NOT({0} AND {1})".format(lola_phi_1, lola_phi_2)


    def negate(self):
        """ Negate the current CTL formula """
        return CTLAnd(self._phi_1, self._phi_2)



class CTLExistUntil(CTLFormula):
    """ Class to represent the Exsits Until operator """

    def __init__(self, phi_1, phi_2):
        if not isinstance(phi_1, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        if not isinstance(phi_2, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi_1 = phi_1
        self._phi_2 = phi_2
        LOG.info("New exist until predicate created")


    def print_lola(self):
        lola_phi_1 = self._phi_1.print_lola()
        lola_phi_2 = self._phi_2.print_lola()
        return "E({0} U {1})".format(lola_phi_1, lola_phi_2)


    def negate(self):
        """ Negate the current CTL formula """
        return CTLNegatedExistUntil(self._phi_1, self._phi_2)


class CTLNegatedExistUntil(CTLFormula):
    """ Class to represent the Negated Exsits Until operator """

    def __init__(self, phi_1, phi_2):
        if not isinstance(phi_1, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        if not isinstance(phi_2, CTLFormula):
            err_message = "Phi provided is not an CTL formula"
            raise CTLException(err_message)
        self._phi_1 = phi_1
        self._phi_2 = phi_2
        LOG.info("New negated exist until predicate created")


    def print_lola(self):
        lola_phi_1 = self._phi_1.print_lola()
        lola_phi_2 = self._phi_2.print_lola()
        return "NOT(E({0} U {1}))".format(lola_phi_1, lola_phi_2)


    def negate(self):
        """ Negate the current CTL formula """
        return CTLExistUntil(self._phi_1, self._phi_2)
