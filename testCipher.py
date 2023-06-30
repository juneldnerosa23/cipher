import unittest
from cipher import cipher


class CipherTests(unittest.TestCase):
    def test_cipher_shift_to_right(self):
        """
        Test cipher with positive integer value for N
        Shift to right
        """
        message = "AbCdE"
        N = 5
        ciphered_message = cipher(message, N)
        self.assertEqual(ciphered_message, "FgHiJ")

    def test_cipher_shift_to_left(self):
        """
        Test cipher with negative integer value for N
        Shift to left
        """
        message = "AbCdE"
        N = -5
        ciphered_message = cipher(message, N)
        self.assertEqual(ciphered_message, "VwXyZ")

    def test_cipher_direct_substitution(self):
        """
        Test cipher with dictionary value for N
        Do direct substitution
        """
        message = "AbCdE"
        N = {"A": "X", "C": "T", "E": "F"}
        ciphered_message = cipher(message, N)
        self.assertEqual(ciphered_message, "XbTdF")

    def test_empty_message(self):
        """
        Test cipher to return empty if message is empty
        """
        message = ""
        N = 25
        ciphered_message = cipher(message, N)
        self.assertEqual(ciphered_message, "")

    def test_invalid_type_for_param_N(self):
        """
        Test cipher to raise ValueError
        if N is not valid integer or dictionary
        """
        message = "tEst"
        N = "test"
        with self.assertRaises(ValueError):
            cipher(message, N)

    def test_param_N_out_of_range_positive_integer(self):
        """
        Test cipher to raise ValueError,
        if N is > 25
        """
        message = "tEst"
        N = 30
        with self.assertRaises(ValueError):
            cipher(message, N)

    def test_param_N_out_of_range_negative_integer(self):
        """
        Test cipher to raise ValueError,
        if N is < -25
        """
        message = "tEst"
        N = -30
        with self.assertRaises(ValueError):
            cipher(message, N)

    def test_message_contains_non_letter(self):
        """
        Test cipher with message contains non-letter characters,
        leave them as is
        """
        message = "@tEst#"
        N = 5
        ciphered_message = cipher(message, N)
        self.assertEqual(ciphered_message, "@yJxy#")


if __name__ == "__main__":
    unittest.main()
