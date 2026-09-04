# test_esp32prime.py
"""
Tests for ESP32Prime module.
"""

import unittest
from esp32prime import ESP32Prime

class TestESP32Prime(unittest.TestCase):
    """Test cases for ESP32Prime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ESP32Prime()
        self.assertIsInstance(instance, ESP32Prime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ESP32Prime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
