"""
================================================================================
                              DESCRIPTION
================================================================================

  This is the base class for all Petri net models. This includes the general
  Petri Net's features such as places and transitions sets, flow input and
  output functions and method to add, remove and modify these elements.

  There are no structural restrictions in the models defined.

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
  Last Update: 31-01-2016

  Date        Alias      Description
--------------------------------------------------------------------------------
  03-01-2016  ulisesma   Initial file creation
  09-01-2016  ulisesma   Description in documentation
  31-01-2016  ulisesma   Fixing imports and adding JSON loading and dumping
                         functions


"""

import json
import re

from error_handling import PetriNetException
from logger import LOG

IO_KEY_PATTERN = "\('(.*)', '(.*)'\)"


class PetriNet(object):
    """ Class to represent a general Petri Net system. """
    def __init__(self):
        self._places = []
        self._transitions = []
        self._input = {}
        self._output = {}


    def add_place(self, place):
        """
        Function to add places to P set if not already in it. If 'place' is not
        an string, this function will raise an exception.
        """
        if not isinstance(place, basestring):
            err_message = "Place provided is not an string"
            raise PetriNetException(err_message)
        if place not in self._places:
            self._places.append(place)
            LOG.info("Place '{0}' added to P set".format(place))
        else:
            LOG.info("Place '{0}' already in P set".format(place))


    def add_transition(self, transition):
        """
        Function to add transition to T set if not already in it. If
        'transition' is not an string, this function will raise an exception.
        """
        if not isinstance(transition, basestring):
            err_message = "Transition provided is not an string"
            raise PetriNetException(err_message)
        if transition not in self._transitions:
            self._transitions.append(transition)
            LOG.info("Transition '{0}' added to T set".format(transition))
        else:
            LOG.info("Transition '{0}' already in T set".format(transition))


    def change_input_flow(self, place, transition, value):
        """
        Change the value of the input function for 'place' and 'transition'
        equals to 'value':
            I(place, transition) = value
        Raise an exception if 'place' is not in P, 'transition' is not in T, or
        'value' is not an integer value equal or greatter than 0.
        """
        if place not in self._places:
            err_message = "Place is not in P"
            raise PetriNetException(err_message)
        if transition not in self._transitions:
            err_message = "Transition is not in T"
            raise PetriNetException(err_message)
        if not isinstance(value, int) or value = 0:
            err_message = "The value is not a integer greater or equal than 0"
            raise PetriNetException(err_message)
        key_pair = (place, transition)
        self._input[key_pair] = value
        msg = "Value updated in I. I({0}, {1}) = {2}".format(place, transition,
                                                             value)
        LOG.info(msg)


    def change_output_flow(self, place, transition, value):
        """
        Change the value of the output function for 'place' and 'transition'
        equals to 'value':
            O(place, transition) = value
        Raise an exception if 'place' is not in P, 'transition' is not in T, or
        'value' is not an integer value equal or greatter than 0.
        """
        if place not in self._places:
            err_message = "Place is not in P"
            raise PetriNetException(err_message)
        if transition not in self._transitions:
            err_message = "Transition is not in T"
            raise PetriNetException(err_message)
        if not isinstance(value, int) or value = 0:
            err_message = "The value is not a integer greater or equal than 0"
            raise PetriNetException(err_message)
        key_pair = (place, transition)
        self._output[key_pair] = value
        msg = "Value updated in O. O({0}, {1}) = {2}".format(place, transition,
                                                             value)
        LOG.info(msg)


    def _get_io_dict(self, function_type):
        """
        Read the proper I or O function and dump into a Python dictionary. It
        converts all the pair keys into strings to avoid problems dumping into a
        JSON file.
        """
        out_dict = {}
        if function_type == "I":
            used_dict = self._input
        elif function_type == "O":
            used_dict = self._output
        else:
            err_message = "Invalid function type: '{0}'".format(function_type)
            raise PetriNetException(err_message)
        for key in used_dict.keys():
            key_str = "{0}".format(key)
            out_dict[key_str] = used_dict[key]
        return out_dict


    def save_file(self, file_name):
        """
        Dump the Petri Net model into a JSON file with name 'file_name'.
        """
        msg = "Dumping Petri Net into file '{0}'".format(file_name)
        LOG.info(msg)
        out_dict = {}
        out_dict["P"] = self._places
        out_dict["T"] = self._transitions
        out_dict["I"] = self._get_io_dict("I")
        out_dict["O"] = self._get_io_dict("O")
        with open(file_name, "w+") as out_file:
          json.dump(out_dict, out_file)
        msg = "Dumping completed".format(file_name)
        LOG.info(msg)


    def _read_io_dict(self, function_type, used_dict):
        """
        Read the proper dict from a loaded file and writes the proper I or O
        function according to the key. It converts the key string into a
        basestring place-transition pair.
        """
        in_dict = {}
        for key_str in used_dict.keys():
            key = re.findall(IO_KEY_PATTERN, key_str)[0]
            p = str(key[0])
            t = str(key[1])
            in_dict[(p, t)] = used_dict[key_str]
        if function_type == "I":
            self._input = in_dict
        elif function_type == "O":
            self._output = in_dict
        else:
            err_message = "Invalid function type: '{0}'".format(function_type)
            raise PetriNetException(err_message)
        return in_dict

    def load_file(self, file_name):
        """
        Load a Petri Net model dumped into a JSON file with name 'file_name'.
        """
        msg = "Loading Petri Net from file '{0}'".format(file_name)
        LOG.info(msg)
        with open(file_name) as in_file:
            in_dict = json.load(in_file)
        self._places = in_dict["P"]
        self._transitions = in_dict["T"]
        self._input = self._read_io_dict("I", in_dict["I"])
        self._output = self._read_io_dict("O", in_dict["O"])
        msg = "Loading completed".format(file_name)
        LOG.info(msg)