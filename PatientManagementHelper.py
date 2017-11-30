
# This program is a menu program that reads the patient file, adds patient, view patient at specific index, view all patients
# and search for patient and exits on menu number.
class PatientManagement:
    """
    Constructor intializes the file_name and a method read_patients_file, reads the patient file and writes it to a patient_dict
    dictionary
    """
    def __init__(self):
        self.patient_dict = {}
        self.file_name = input("Enter the file Name: ")
        self.read_patients_file(self.file_name)

    """
    This method reads the patient file based on the file_name and adds the file data to a dictioanry with key as index
    and displays the number of records read
    """
    def read_patients_file(self, file_name):
        patient_list = list()
        try:
            with open(file_name) as file:
                patient_list = ((file.read()).replace("\n", "#")).split("#")
                for count, itr in enumerate(patient_list):
                    if len(itr) > 0:
                        self.patient_dict[count] = itr
                print("Loaded " + str(len(self.patient_dict)) + " records from the file.")
                self.main_menu()
        except IOError:
            print("Error reading file. Please enter valid file name.")
    """"
    This method displays menu information and on choice entered by the user, calls the corresponding method with proper
    error handling.
    """
    def main_menu(self):
        choice = 0
        while True:
            print("###############################################")
            print("############      MENU       ##################")
            print("######## 1. Add Patient   #####################")
            print("######## 2. View Patient at specific index ####")
            print("######## 3. View all Patients #################")
            print("######## 4. Search for patient ################")
            print("######## 5. Exit ##############################")
            print("###############################################")
            try:
                choice = int(input("Select an option: "))
                if choice == 1:
                    self.add_patient()
                elif choice == 2:
                    print("Number of patients in patient directory are: " + str(len(self.patient_dict)) +
                          " , Select any number from 0 till " + str(len(self.patient_dict) - 1))
                    index_num = int(input("Enter the index number: "))
                    self.find_patient_at_index(index_num)
                elif choice == 3:
                    self.show_all()
                elif choice == 4:
                    p_name = input("Enter the patient to be searched with name: ")
                    self.find_patient_with_name(p_name)
                elif choice == 5:
                    self.call_exit()
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid number. Please enter again")

    """
    The user's entered new patient data is added to the dictionary and with proper error handling
    """
    def add_patient(self):
        try:
            name = str(input("Enter Name to be added: "))
            ssn = input("Enter SSN to be added: ")
            age = int(input("Enter AGE to be added: "))
            diagnosis = int(input("Enter DIAGNOSIS to be added: "))
            new_entry = name + "," + ssn + "," + str(age) + "," + str(diagnosis)
            self.patient_dict[len(self.patient_dict)] = new_entry
        except ValueError:
            print("Invalid value. Please enter again.")
        except:
            print("An unexpected error occurred.")

    """
    Based on the index entered by the user, the corresponding patient information is displayed.
    """
    def find_patient_at_index(self, ind_to_returned):
        try:
            p_list = str(self.patient_dict[ind_to_returned]).split(",")
            print("{:<51}".format('-----------------------------------------------------------------'))
            print("{:<30} {:<13} {:<4} {:<3}".format('NAME', 'SSN', 'AGE', 'DIAGNOSIS'))
            print("{:<51}".format('-----------------------------------------------------------------'))
            print("{:<30} {:<13} {:<4} {:<3}".format(str(p_list[0]), str(p_list[1]), str(p_list[2]) , str(p_list[3])))
        except ValueError:
            print("Invalid patient index.")
        except:
            print("An unexpected error occurred. Please try again.")

    """
    This method displays all the patient information in a proper format.
    """
    def show_all(self):
        try:
            print("{:<51}".format('-----------------------------------------------------------------'))
            print("{:<30} {:<13} {:<4} {:<3}".format('NAME', 'SSN', 'AGE', 'DIAGNOSIS'))
            print("{:<51}".format('-----------------------------------------------------------------'))
            for key, data in self.patient_dict.items():
                p_list = str(data).split(",")
                print("{:<30} {:<13} {:<4} {:<3}".format(str(p_list[0]), str(p_list[1]), str(p_list[2]), str(p_list[3])))
        except:
            print("An unexpected error occurred. Please try again.")

    """
    This method iterates through the dictionary and searches for the patient name as entered by the user and on finding the name,
    displayes the patient information on the console
    """
    def find_patient_with_name(self, patient_name):
        patient_found = False
        try:
            print("{:<51}".format('-----------------------------------------------------------------'))
            print("{:<30} {:<13} {:<4} {:<3}".format('NAME', 'SSN', 'AGE', 'DIAGNOSIS'))
            print("{:<51}".format('-----------------------------------------------------------------'))
            for k, v in self.patient_dict.items():
                p_list = str(v).split(",")
                if p_list[0].lower() == str(patient_name).lower():
                    print("{:<30} {:<13} {:<4} {:<3}".format(str(p_list[0]), str(p_list[1]), str(p_list[2]), str(p_list[3])))
                    patient_found = True
                    break
                else:
                    patient_found = False
            if patient_found == False:
                print("Patient not found. Please enter a valid name.")
        except ValueError:
            print("Invalid patient index.")
        except:
            print("An unexpected error occurred. Please try again.")

    """
    When this choice is called, the new patient data entered in the dictionary is written to the patient_data.txt file.
    """
    def call_exit(self):
        try:
            with open(self.file_name, "w") as outfile:
                for ky, value in self.patient_dict.items():
                    outfile.write(str(value) + "\n")
                print("\n")
                print("Successfully exited.")
                print("\n")
        except IOError:
            print("Error adding data. Please try again.")
        except:
            print("An unexpected error occurred.")

# Instantiate the object PatientManagement class.
pm = PatientManagement()
