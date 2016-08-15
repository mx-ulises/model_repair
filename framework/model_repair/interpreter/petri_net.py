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
  Last Update: 14-08-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  09-08-2016  ulisesma   Initial file creation
  13-08-2016  ulisesma   Place Lists and other sub-parsers
  14-08-2016  ulisesma   Marking List and other sub-parsers
  14-08-2016  ulisesma   Transitions and other sub-parsers

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
        err_message = ERROR_MESSAGE_TEMPLATE.format(";", separator)
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
    #TODO: Create a Petri Net object and return
    pass


def _place_lists(file_object):
    LOG.info("[START] Getting Place lists")
    capacity = _capacity(file_object)
    place_list = _place_list(file_object)
    separator = _get_object(file_object)
    if separator != ";":
        err_message = ERROR_MESSAGE_TEMPLATE.format(";", separator)
        raise PetriNetInterpreterException(err_message)
    capacity = _capacity(file_object)
    while capacity:
        place_list = _place_list(file_object)
        separator = _get_object(file_object)
        if separator != ";":
            err_message = ERROR_MESSAGE_TEMPLATE.format(";", separator)
            raise PetriNetInterpreterException(err_message)
        capacity = _capacity(file_object)
    LOG.info("[END] Getting Place lists")
    #TODO: Create a Place lists object and return
    pass


def _capacity(file_object):
    LOG.info("[START] Getting capacity")
    reserved = _get_object(file_object)
    if reserved != "SAFE":
        err_message = ERROR_MESSAGE_TEMPLATE.format("SAFE", reserved)
        raise PetriNetInterpreterException(err_message)
    number = _get_object(file_object)
    if isinstance(number, Number):
        err_message = ERROR_MESSAGE_TEMPLATE.format("number", number)
        raise PetriNetInterpreterException(err_message)
    separator = _get_object(file_object)
    if reserved != ":":
        err_message = ERROR_MESSAGE_TEMPLATE.format(":", separator)
        raise PetriNetInterpreterException(err_message)
    LOG.info("[END] Getting capacity")
    #TODO: Create a capacity object and return
    pass

def _place_list(file_object):
    LOG.info("[START] Getting Place list")
    nodeident = _nodeident(file_object)
    separator = _get_object(file_object)
    while separator == ",":
        nodeident = _nodeident(file_object)
        separator = _get_object(file_object)
    LOG.info("[END] Getting Place list")
    #TODO: Create a Place list object and return
    pass

def _nodeident(file_object):
    LOG.info("[START] Getting Node identifier")
    nodeident = _get_object(file_object)
    if isinstance(nodeident, Number) or isinstance(nodeident, Identifier):
        LOG.info("[END] Getting Node identifier")
        return nodeident
    err_message = ERROR_MESSAGE_TEMPLATE.format("Identifier", nodeident)
    raise PetriNetInterpreterException(err_message)

def _marking_list(file_object):
    LOG.info("[START] Getting Marking List")
    marking = _marking(file_object)
    separator = _get_object(file_object)
    while separator == ",":
        marking = _marking(file_object)
        separator = _get_object(file_object)
    LOG.info("[END] Getting Marking List")
    #TODO: Create a Place list object and return
    pass


def _marking(file_object):
    LOG.info("[START] Getting Marking")
    nodeident = _nodeident(file_object)
    separator = _get_object(file_object)
    if separator == ":":
        number = _get_object(file_object)
        if not isinstance(nodeident, Number):
            err_message = ERROR_MESSAGE_TEMPLATE.format("Number", number)
            raise PetriNetInterpreterException(err_message)
    LOG.info("[END] Getting Marking")
    #TODO: Create a Marking object and return
    pass


def _transition(file_object):
    LOG.info("[START] Getting Transition")
    reserved = _get_object(file_object)
    if reserved != "TRANSITION":
        err_message = ERROR_MESSAGE_TEMPLATE.format("TRANSITION", reserved)
        raise PetriNetInterpreterException(err_message)
    nodeident = _nodeident(file_object)
    fairness = _fairness(file_object)
    reserved = _get_object(file_object)
    if reserved != "CONSUME":
        err_message = ERROR_MESSAGE_TEMPLATE.format("CONSUME", reserved)
        raise PetriNetInterpreterException(err_message)
    arc_list = _arc_list(file_object)
    separator = _get_object(file_object)
    if separator != ";":
        err_message = ERROR_MESSAGE_TEMPLATE.format(";", separator)
        raise PetriNetInterpreterException(err_message)
    reserved = _get_object(file_object)
    if reserved != "PRODUCE":
        err_message = ERROR_MESSAGE_TEMPLATE.format("PRODUCE", reserved)
        raise PetriNetInterpreterException(err_message)
    arc_list = _arc_list(file_object)
    separator = _get_object(file_object)
    if separator != ";":
        err_message = ERROR_MESSAGE_TEMPLATE.format(";", separator)
        raise PetriNetInterpreterException(err_message)
    LOG.info("[END] Getting Transition")
    #TODO: Create a Transition object and return
    pass


def _fairness(file_object):
    LOG.info("[START] Getting Fairness")
    reserved = _get_object(file_object)
    if reserved != "STRONG" and reserved != "WEAK":
        err_message = ERROR_MESSAGE_TEMPLATE.format("STRONG' or 'WEAK", reserved)
        raise PetriNetInterpreterException(err_message)
    reserved = _get_object(file_object)
    if reserved != "FAIR":
        err_message = ERROR_MESSAGE_TEMPLATE.format("FAIR", reserved)
        raise PetriNetInterpreterException(err_message)
    LOG.info("[END] Getting Fairness")
    #TODO: Create a Fairness object and return
    pass


def _arc_list(file_object):
    LOG.info("[START] Getting Arc List")
    arc = _arc(file_object)
    separator = _get_object(file_object)
    while separator == ",":
        arc = _arc(file_object)
        separator = _get_object(file_object)
    LOG.info("[END] Getting Arc List")
    #TODO: Create a Arc List object and return
    pass


def _arc(file_object):
    LOG.info("[START] Getting Arc")
    nodeident = _nodeident(file_object)
    separator = _get_object(file_object)
    if separator == ":":
        number = _get_object(file_object)
        if not isinstance(nodeident, Number):
            err_message = ERROR_MESSAGE_TEMPLATE.format("Number", number)
            raise PetriNetInterpreterException(err_message)
    LOG.info("[END] Getting Arc")
    #TODO: Create a Arc object and return
    pass
