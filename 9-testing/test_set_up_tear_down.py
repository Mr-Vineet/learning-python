import unittest
import os

class TestListOfIntegers(unittest.TestCase):
    def setUp(self):
        self.nums = [1, 2, 3, 4]
    
    def test_length_of_list(self):
        self.assertEqual(len(self.nums), 4)
        

    def test_sum_of_integers(self):
        self.assertEqual(sum(self.nums), 10)
    
    def test_legth_of_list_after_clearing(self):
        self.nums.clear()
        self.assertEqual(len(self.nums), 0)

    def tearDown(self):
        print("Test done")

class TestFileChanges(unittest.TestCase):
    def setUp(self):
        self.filename = "demo_log.txt"
        
        with open(self.filename, "w") as f:
            f.write("log: I am in office")
    
    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.filename))
            
    def test_read_content_of_file(self):
        with open(self.filename, "r") as f:
            line = f.readline()
        self.assertTrue(line.startswith("log:"))
    
    def tearDown(self):
        if (os.path.exists(self.filename)):
            os.remove(self.filename)

class TestFileContent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filename = "demo.txt"
        with open(cls.filename, "w") as f:
            f.writelines(["my name is Vineet\n",
                          "I am working in TW as an associate Developer\n",
                          "I am currently living in GGN\n\n"])
        
        with open(cls.filename, "r") as f:
            print(f.read())
    
    @classmethod
    def tearDownClass(cls):
        if(os.path.exists(cls.filename)):
            os.remove(cls.filename)
    
    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.filename))
    
    def test_count_of_lines(self):
        with open(self.filename, "r") as f:
            no_of_lines = len(f.readlines())
            
        self.assertEqual(no_of_lines, 4)

if (__name__ == "__main__"):
   unittest.main()