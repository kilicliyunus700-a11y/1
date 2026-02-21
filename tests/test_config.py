"""Tests for config loading functionality of Root - Team AutoExploit."""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Config', 'config.json')


class TestConfigStructure(unittest.TestCase):
    """Tests to verify config.json has the expected structure."""

    def setUp(self):
        with open(CONFIG_PATH, encoding='utf-8') as f:
            self.config = json.load(f)

    def test_technology_section_exists(self):
        """config.json must have a TECHNOLOGY section."""
        self.assertIn('TECHNOLOGY', self.config)

    def test_technology_required_keys(self):
        """TECHNOLOGY section must contain required feature toggles."""
        tech = self.config['TECHNOLOGY']
        required_keys = [
            'CVE_Exploiter', 'Plugin_Exploiter', 'LFI_Scanner',
            'WP_PHPUnit', 'PhpMyAdmin', 'Proxies', 'WordPress',
        ]
        for key in required_keys:
            self.assertIn(key, tech, f"Missing key: {key}")

    def test_core_section_exists(self):
        """config.json must have a Core section."""
        self.assertIn('Core', self.config)

    def test_core_keys(self):
        """Core section must have userAgent and maxThreads."""
        core = self.config['Core']
        self.assertIn('userAgent', core)
        self.assertIn('maxThreads', core)

    def test_proxy_config_section_exists(self):
        """config.json must have a Proxy_Config section."""
        self.assertIn('Proxy_Config', self.config)

    def test_urls_section_exists(self):
        """config.json must have a URLs section."""
        self.assertIn('URLs', self.config)

    def test_boolean_technology_values(self):
        """All values in TECHNOLOGY section must be booleans."""
        for key, value in self.config['TECHNOLOGY'].items():
            self.assertIsInstance(value, bool, f"TECHNOLOGY.{key} should be bool, got {type(value)}")

    def test_max_threads_is_integer(self):
        """Core.maxThreads must be an integer."""
        self.assertIsInstance(self.config['Core']['maxThreads'], int)


if __name__ == '__main__':
    unittest.main()
