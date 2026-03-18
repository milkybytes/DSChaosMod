import unittest
import tkinter as tk
from TwitchVotingServer.gui.components.settings_tab import SettingsField
from tests.gui.components.tk_helper import get_root


class TestSettingsField(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = get_root()

    @classmethod
    def tearDownClass(cls):
        pass  # Shared root — must not be destroyed mid-session (Python 3.14+)

    def test_get_default_value(self):
        sf = SettingsField(self.root, "Label")
        self.assertEqual(sf.get(), "")

    def test_get_custom_value(self):
        sf = SettingsField(self.root, "Label", "Value")
        self.assertEqual(sf.get(), "Value")

if __name__ == "__main__":
    unittest.main()