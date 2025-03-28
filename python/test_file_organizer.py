import unittest
import os
from io import StringIO
import sys

class TestFileOrganizer(unittest.TestCase):
    def test_file_organizer(self):
        # Test that main.py exists
        self.assertTrue(os.path.exists("main.py"), "main.py does not exist")
        # Test that main.py contains the expected code
        with open("main.py", "r") as file:
            main_contents = file.read()
            self.assertIn("def main():", main_contents, "main() function not found")
            self.assertIn("print(\"Welcome to the File Organizer\")", main_contents, "Welcome message not found")
            self.assertIn("source_dir", main_contents, "source_dir variable not found")
            self.assertIn("if __name__ == \"__main__\":", main_contents, "__main__ block not found")
            self.assertIn("main()", main_contents, "main() function not called")
        # Test that main.py runs
        output = sys.stdout
        sys.stdout = StringIO()
        import main
        sys.stdout = output
        self.assertEqual(sys.stdout.getvalue(), "Welcome to the File Organizer\n", "Output is not correct")
        
if __name__ == "__main__":
    unittest.main()

