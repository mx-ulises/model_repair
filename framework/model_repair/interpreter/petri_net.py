"""
================================================================================
                              DESCRIPTION
================================================================================

  This Module include the interpreter for Petri Net models specified as LoLA
  files providing a comprehensive class structure that can be translated into a
  Petri Net object or a JSON file for exchange.

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
  Last Update: 09-08-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  09-08-2016  ulisesma   Initial file creation

"""

from sets import Set

from model_repair.error_handling import PetriNetInterpreterException
from model_repair.logger import LOG

RESERVED_WORDS = ["PLACE", "MARKING"]
RESERVED_WORDS = Set(RESERVED_WORDS)

ERROR_MESSAGE_TEMPLATE = "Invalid object found. Expected '{0}', found '{1}'."

def _get_object(file_object):
    #TODO: Implement routines to get the required objects
    pass


def _net(file_object):
    LOG.info("[START] Processing new LoLA Petri net file")
    reserved = _get_object(file_object)
    if reserved != "PLACE":
        err_message = ERROR_MESSAGE_TEMPLATE.format("PLACE", reserved)
        raise PetriNetInterpreterException(err_message)

    place_list = _place_lists(file_object)

    reserved = _get_object(file_object)
    if reserved != "MARKING":
        err_message = ERROR_MESSAGE_TEMPLATE.format("MARKING", reserved)
        raise PetriNetInterpreterException(err_message)

    marking_list = _marking_list(file_object)

    separator = _get_object(file_object)
    if separator != ";":
        err_message = ERROR_MESSAGE_TEMPLATE.format(";", reserved)
        raise PetriNetInterpreterException(err_message)

    transitions = []
    x = _transition(file_object)
    if not x:
        err_message = ERROR_MESSAGE_TEMPLATE.format("Transition Object", x)
        raise PetriNetInterpreterException(err_message)

    transitions.append(x)
    x = _transition(file_object)
    while x:
        transitions.append(x)
        x = _transition(file_object)

    LOG.info("[END] Processing new LoLA Petri net file")
    pass


def _place_lists(file_object):
    #TODO: Implement routines to get the place_lists objects
    pass


def _marking_list(file_object):
    #TODO: Implement routines to get the marking_list objects
    pass


def _transition(file_object):
    #TODO: Implement routines to get the transition objects
    pass
