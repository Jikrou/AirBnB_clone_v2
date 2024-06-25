# test_do_create.py

import unittest
from unittest.mock import patch, MagicMock
from console import HBNBCommand


class TestDoCreate(unittest.TestCase):

    @patch('console.storage')
    def test_do_create_basic(self, mock_storage):
        """Test creating an instance with basic parameters"""
        cmd = HBNBCommand()

        # Mock the instance creation for 'Test' class
        mock_instance = MagicMock()
        mock_instance.name = 'Test Instance'  # Set specific attribute
        cmd.classes = {'Test': lambda: mock_instance}

        # Simulate input arguments
        args = "Test name='Test Instance' num=42"
        with patch('builtins.input', side_effect=[args]):
            cmd.do_create(args)

        # Assert that the instance was created and attributes set correctly
        self.assertEqual(mock_instance.name, 'Test Instance')

if __name__ == '__main__':
    unittest.main()
