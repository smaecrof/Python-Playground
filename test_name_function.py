# Author: Spencer Mae-Croft
# Date: 08/31/2020

import unittest 
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Spencer Mae-Croft' work?"""

        formatted_name = get_formatted_name('Spencer', 'Mae-Croft')
        self.assertEqual(formatted_name, 'Spencer Mae-Croft')


    def test_first_middle_last_name(self):
        """ Do names like "Elise Ann Patrick" work?"""

        formatted_name = get_formatted_name("Elise","Patrick","Ann")
        self.assertEqual(formatted_name, "Elise Ann Patrick")

unittest.main()
