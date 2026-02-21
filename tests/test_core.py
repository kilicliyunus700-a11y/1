"""Unit tests for Core modules of Root - Team AutoExploit."""
import os
import sys
import unittest

# Add root directory to path so Core modules can be imported in limited fashion
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCoreBranding(unittest.TestCase):
    """Tests to verify rebranding strings are correct in core modules."""

    def test_infom_helper_about_title(self):
        """Infom_Helper About_US panel should reference new project name."""
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Core', 'Infom_Helper.py')
        with open(path, encoding='utf-8') as f:
            source = f.read()
        self.assertIn('Root - Team AutoExploit', source)
        self.assertNotIn('BurnWP Framework', source)
        self.assertNotIn('DRCrypter', source)
        self.assertNotIn('drcrypter.ru', source)

    def test_ui_settings_window_title(self):
        """UI_Settings window title should reference new project name."""
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Core', 'UI_Settings.py')
        with open(path, encoding='utf-8') as f:
            source = f.read()
        self.assertIn('Root - Team AutoExploit - Config', source)

    def test_readme_title(self):
        """README.md should have the new project title."""
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
        with open(path, encoding='utf-8') as f:
            content = f.read()
        self.assertIn('# 🔥 Root - Team AutoExploit v1.0.0 💥', content)
        self.assertNotIn('BurnWP Framework', content)
        self.assertNotIn('drcrypterdotru', content)
        self.assertNotIn('t.me/burnwpcommunity', content)

    def test_requirements_pyqt_fluent_pinned(self):
        """requirements.txt should have PyQt-Fluent-Widgets pinned to a version."""
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'requirements.txt')
        with open(path, encoding='utf-8') as f:
            content = f.read()
        self.assertRegex(content, r'PyQt-Fluent-Widgets==\d+\.\d+\.\d+')

    def test_no_bare_except_in_config_a(self):
        """Config_A.py should not use bare except clauses."""
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Core', 'Config_A.py')
        with open(path, encoding='utf-8') as f:
            source = f.read()
        # bare except: (not followed by a space and exception class)
        import re
        bare_excepts = re.findall(r'^\s*except\s*:', source, re.MULTILINE)
        self.assertEqual(bare_excepts, [], "Found bare except: clauses in Config_A.py")


if __name__ == '__main__':
    unittest.main()
