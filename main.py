from password_generator import make_password

def main():
    print("Main program running...")
    while True:
        try:
            password_length = int(input("How long would you like your password to be? "))
            password = make_password(password_length)
            
            # Check if the password is an error message
            if "Error" in password:
                print(password)  # Print the error message
            else:
                print(f"Generated password: {password}")
                break  # Exit the loop after generating a valid password
        except ValueError:
            print("Please enter a valid integer for password length.")


def run_tests():
    print("Running tests...")

    # Test case 1: Check if password length matches input
    password_length = 8
    password = make_password(password_length)
    assert len(password) == password_length, f"Test failed: Expected length {password_length}, got {len(password)}"
    print(f"Test 1 passed: Generated password of length {password_length}")

     # Test case 2: Check if at least one symbol is in the password
    password = make_password(12)
    symbols = '!@#$%^&*()?'
    assert any(char in symbols for char in password), "Test failed: No symbol found in password"
    print("Test 2 passed: Contains at least one symbol")    

    # Test case 3: Check if at least one digit is in the password
    digits = '0123456789'
    assert any(char in digits for char in password), "Test failed: No digit found in password"
    print("Test 3 passed: Contains at least one digit")

    # Test case 4: Check if at least one lowercase character is in the password
    lowercase = 'abcdefghijklmopqrstuvwxyz'
    assert any(char in lowercase for char in password), "Test failed: No lowercase character found in password"
    print("Test 4 passed: Contains at least one lowercase character")

    # Test case 5: Check if at least one uppercase character is in the password
    uppercase = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    assert any(char in uppercase for char in password), "Test failed: No uppercase character found"
    print("Test 5 passed: Contains at least one uppercase character")




if __name__ == "__main__":
    import sys
    if "test" in sys.argv:
        run_tests()
    else:
        main()
