import string


def cipher(m, N):
    """Function to cipher a message

    Args:
        m (str, required): message string
        N (int or dict, required): integer between -25 to +25
            or a dictionary that contains direct mapping/substitution

    Return:
        ciphered message (str)
    """
    chipered_message = ""

    # Check if `m` param is a valid string and not empty
    if type(m) == str and len(m) > 1:
        # If `N` is integer, shift letter
        if type(N) == int:
            # Raise exeption if `N` not between -25 to +25
            if N < -25 or N > 25:
                raise ValueError("Param `N` is out of range.")

            for char in list(m):
                # Skip if character if not a letter, leave them as is
                if not char.isalpha():
                    chipered_message += char
                    continue

                # Lower or Upper case
                letters = (
                    list(string.ascii_lowercase)
                    if char.islower()
                    else list(string.ascii_uppercase)
                )

                # Shift letter to left or right
                # based on the current index + N
                current_idx = list(letters).index(char) + N
                if current_idx >= len(letters):
                    current_idx = current_idx - len(letters)
                chipered_message += letters[current_idx]

        # If `N` is dict, do direct substitution
        elif type(N) == dict:
            for char in list(m):
                # Skip if character if not a letter
                if not char.isalpha():
                    chipered_message += char
                    continue

                # Substitute letter if exists in dictionary,
                # otherwise leave them as is
                if char in N:
                    chipered_message += N[char]
                else:
                    chipered_message += char
        else:
            raise ValueError("Invalid type for param `N`.")

        return chipered_message

    # if `m` is empty then return `m`.
    else:
        return m


if __name__ == "__main__":
    # ['A', 'B', 'C', 'D', 'E',
    # 'F', 'G', 'H', 'I', 'J',
    # 'K', 'L', 'M', 'N', 'O',
    # 'P', 'Q', 'R', 'S', 'T',
    # 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Example 1 (N is positive integer, Shift to right)
    message = "AbCdE"
    num_or_dict = 5
    print(cipher(message, num_or_dict))

    # Example 2 (N is negative integer, Shift to left)
    message = "AbCdE"
    num_or_dict = -5
    print(cipher(message, num_or_dict))

    # Example 3 (N is dictionary, do direct substitution)
    message = "AbCdE"
    num_or_dict = {"A": "X", "C": "T", "E": "F"}
    print(cipher(message, num_or_dict))
