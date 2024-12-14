#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_most_likely_ancestor_consensus, test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


    def get_most_likely_ancestor_consensus(self):
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

        post1, post2, post3 = result

        self.assertEqual(post1, 2)
        self.assertEqual(post2, 4)
        self.assertEqual(post3, 10)

