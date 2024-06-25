# test_do_create.py

import unittest
from unittest.mock import patch, MagicMock
from console import HBNBCommand

class TestDoCreate(unittest.TestCase):

    @patch('console.storage')
    def test_do_create_basic(self, mock_storage):
        """Test creating an instance with basic parameters"""
        cmd = HBNBCommand()
        cmd.classes = {'Test': MagicMock()}
        mock_instance = cmd.classes['Test']()

        args = "Test name='Test Instance' number=42"
        with patch('builtins.input', side_effect=[args]):
            cmd.do_create(args)

        # Assert that the instance was created and attributes set correctly
        self.assertEqual(mock_instance.name, 'Test Instance')
        self.assertEqual(mock_instance.number, 42)


if __name__ == '__main__':
    unittest.main()

