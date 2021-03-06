# -*- coding: utf-8 -*-

import argparse
from typing import NoReturn, Text

class Arguments:

  def __init__(self, *args, **kwargs) -> NoReturn:
    self._parser = self._create_parser_object(*args, **kwargs)
    self._adding_arguments()
    self.args = vars(self._parser.parse_args())

  @staticmethod
  def _create_parser_object(*args, **kwargs) -> argparse.ArgumentParser:
    try:
      return argparse.ArgumentParser(*args, **kwargs)
    except argparse.ArgumentError as error:
      print(f"Error when we create a parser object - {error}")

  def _adding_arguments(self) -> NoReturn:
    self._parser.add_argument("-u", "--url",
                                type=str,
                                metavar="<url>",
                                default=None,
                                help="GitLab URL")
    self._parser.add_argument("-t", "--token",
                                type=str,
                                metavar="<token>",
                                default=None,
                                help="GitLab Token")
