# test_pivothub.py
"""
Tests for PivotHub module.
"""

import unittest
from pivothub import PivotHub

class TestPivotHub(unittest.TestCase):
    """Test cases for PivotHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PivotHub()
        self.assertIsInstance(instance, PivotHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PivotHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
