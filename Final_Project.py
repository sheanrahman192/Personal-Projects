import string
import random
class PasswordManager:
    
    def __init__(self, name, master_pw):
        self.__name = name
        self.__master_pw = master_pw
        self.__login = {}

    #No idea what this is
    #def checker(self):
        #return self.__passwords.copy()

    def validate(self, master_pass):
        # Checks whether mp is the same as the master password
        # Returns a boolean
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE

        #Only needs to return bools for later comparisons
        if master_pass == self.__master_pw:
            return True
        else:
            return False


    def get_name(self):
        # Return the name of the owner of the password manager
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE

        return self.__name

    def get_comp_list(self):
        # Return a list of all the company names (all the keys from dictionary login, not the values)
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE

        #Since .keys() returns a list, it's the easiest way to get all the company names into a list
        company_names = self.__login.keys()
        return company_names

    def get_comp_info(self, comp_name, master_pass):
        # If master_password entered correctly
        # If company name is present in the dictionary login
        # Returns a tuple of username and password for the company name passed in as the argument
        # If master password is wrong, print the error message according to instructions and returns False
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE

        #If the master_pass and master_pw are the same, this is True, so it'll run the code below,
        #which just returns the username and password, stored as a list in the dictionary value
        if self.validate(master_pass):
            user_and_password = (self.__login[comp_name][0], self.__login[comp_name][1])
            return user_and_password
        else:
            print("Incorrect master password!")
            return False

# ****** __generate_password begins. ******
    #__generate_password is correct.Do not change anything in it.

    def __generate_password(self, criteria = {'length':14, 'min_lower':0, 'min_upper':0, 'min_digits':0, 'min_special':0}):
        lower_letters = string.ascii_lowercase # a string of all alphabets in lowercase
        upper_letters = string.ascii_uppercase # a string of all alphabets in uppercase
        digits = string.digits # a string of all numbers
        special_chars = string.punctuation # a string of all punctuations
        length = criteria.get('length', 14) # refer to the dictionary 'criteria' and set default required length of the password to 14
        min_special = criteria.get('min_special', 0) # refer to the dictionary 'criteria' and set min num of speacial characters to 0
        min_digits = criteria.get('min_digits', 0) # refer to the dictionary 'criteria' and set min num of digits to 0
        min_upper = criteria.get('min_upper', 0) # refer to the dictionary 'criteria' and set min num of uppercase to 0
        min_lower = criteria.get('min_lower', 0) # refer to the dictionary 'criteria' and set min num of lowercase to 0

        # Ensure length requirements are met
        if length >= min_lower + min_upper + min_special + min_digits:
            # Generate password with required characters
            password = (random.choices(lower_letters, k=min_lower)) + (random.choices(upper_letters, k=min_upper)) + (
                random.choices(special_chars, k=min_special)) + (random.choices(digits, k=min_digits))
            # Fill the remaining length with random characters
            remaining_length = length - (min_lower + min_upper + min_special + min_digits)
            password += ''.join(
                random.choices(upper_letters + lower_letters + digits + special_chars, k=remaining_length))
            # Shuffle the password to ensure randomness
            password_list = list(password)
            random.shuffle(password_list)
            password = ''.join(password_list)
            return password

# ****** __generate_password ends. ******
    
    def add_data(self, comp_name, username, master_pass, criteria = {'length':14, 'min_lower':0, 'min_upper':0, 'min_digits':0, 'min_special':0}):
        # If master_password entered is correct
        # If company name not in dictionary login
        # generate a new password according to criteria by appropriately calling generate_password() method
        # add the company as key  and [username, password] as the value to the dictionary login
        # If __generate_password does not return a password, prints the error message according to instructions
        # If master password is wrong, print the error message according to instructions and return False
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE

        #Again, just making sure the master_pass given matches the actual master_pw
        if self.validate(master_pass):
            #If the company name is not in the login keys, which are all the company names
            if comp_name not in self.__login.keys():
                #Creates a new password based off the criteria
                new_pass = self.__generate_password(criteria)
                #This is to insure valid criteria were entered, if it wasn't the new_pass would be a Null value, as the 
                #password generator would not return anything
                if new_pass == None:
                    print("Invalid Specifications!")
                #If the password is valid, creates a key value pair, with the value being a list, containing the username and password
                else:
                    self.__login[comp_name] = [username, new_pass]
        else:
            print("Incorrect master password")
            return False

    
    def change_password(self, comp_name, master_pass, new_pass = None, criteria = {'length':14, 'min_lower':0, 'min_upper':0, 'min_digits':0, 'min_special':0}):
        # If master_password entered correctly
        # If company name is present in the dictionary login
        # Updates the password to the company name
        # This will be new_pass if provided, otherwise, will generate a
        # New password using criteria by appropriately calling generate_password() method
        # If generte_password does not return a password, print the error message according to instructions
        # If site does not exist, print the error message according to instructions
        # If master password is wrong, print the error message according to instructions and returns False
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE

        
        if self.validate(master_pass):
            #Slight difference from previous method, this one checks that it IS in the key list
            if comp_name in self.__login.keys():
                #If new_pass is not given by user
                if new_pass == None:
                    #Generates the new password
                    new_pass1 = self.__generate_password(criteria)
                    #Checks to make sure valid criteria are given
                    if new_pass1 == None:
                        print("Invalid criteria!")
                        return False
                    else:
                        self.__login[comp_name][1] = new_pass1
                else: 
                    self.__login[comp_name][1] = new_pass
            else:
                print("Company does not exist!")
                return False
        else:
            print("Incorrect master password!")
            return False

        

    def remove_comp(self, comp_name, master_pass):
        # If master_password entered correctly
        # If company name is present in the dictionary login
        # Delete the company name and the associated data (delete item from dictionary login based on key)
        # If master password is wrong, print the error message according to instructions and returns False
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE

        if self.validate(master_pass):
            #Checks to see in comp_name is in key list , if it isn't, this method does nothing
            if comp_name in self.__login.keys():
                #Deletes the key value pair from the login dictonary 
                del self.__login[comp_name]
        else:
            print("Incorrect master password!")
            return False

    
    def __str__(self):
        # Return a string representation of ONLY the sites
        # Should look like this
        # Company names stored for NAME_OF_OWNER are as follows:
        # Google
        # Meta
        # Tesla
        # One company name per line with the header line
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE
        #Iterates through the key list, and prints cout each value of the list, ie the company names
        comp_list = ""
        comp_list += "Company names stored for " + self.__name + "are as follows:\n"
        for comp in self.__login.keys():
            comp_list += comp + "\n" 

        return comp_list




