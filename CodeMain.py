# Kawani J. Mumtaz
# Fall 2025
# Project 1
# Contributor: Kawani J. Mumtaz (Just Me)
# AI Usage: Debugging help from ChatGPT

import unittest
import os
import csv

def get_island(island, species, parameter):

    out_list = []

    try:
        for values in ImportPenguins.PenguinData[island][species][parameter]:
            out_list.append(values)
    except:
        return "Invalid"

    return out_list


def operator(command, values_list):

    if command == "median":
        values_list.sort()
        n = len(values_list)
        if n % 2 == 0:
            median = (values_list[n//2 - 1] + values_list[n//2]) / 2
        else:
            median = values_list[n//2]
        return median
    
    elif command == "mean":
        mean = sum(values_list) / len(values_list)
        return mean

    return None


class ImportPenguins():

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "penguins.csv")

    PenguinData = {}

    with open(full_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            species = row[1]
            island = row[2]
            bill_length_mm = row[3]
            bill_depth_mm = row[4]
            flipper_length_mm = row[5]
            body_mass_g = row[6]

            if island not in PenguinData:
                PenguinData[island] = {}
            
            if species not in PenguinData[island]:
                PenguinData[island][species] = {
                    "bill_depth_mm": [],
                    "bill_length_mm": [],
                    "flipper_length_mm": [],
                    "body_mass_g": []
                }

            if bill_depth_mm and bill_length_mm and flipper_length_mm and body_mass_g != "NA":

                PenguinData[island][species]["bill_depth_mm"].append(float(bill_depth_mm))
                PenguinData[island][species]["bill_length_mm"].append(float(bill_length_mm))
                PenguinData[island][species]["flipper_length_mm"].append(float(flipper_length_mm))
                PenguinData[island][species]["body_mass_g"].append(float(body_mass_g)) 


class LogWriter():
    def __init__(self, filename="log.txt"):
        self.filename = filename
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.full_path = os.path.join(self.base_path, self.filename)
        with open(self.full_path, 'w') as file:
            file.write("Log File Created\n")

    def add_log(self, entry):
        with open(self.full_path, 'a') as file:
            file.write(entry + "\n")

    def close(self):
        with open(self.full_path, 'a') as file:
            file.write("Log File Closed\n")


class CommandLine():
    def __init__(self):
        self.iteration = 0

    def run(self):
        """Run the interactive command-line loop. This will only execute
        when called explicitly (not on import).
        """
        log = None
        while True:
            self.iteration += 1

            instruct = input("Enter command: ")
            instruct = instruct.split()
            if len(instruct) == 0:
                print("Invalid command")
                continue
            if instruct[0] == "exit":
                break
            if len(instruct) != 4:
                print("Invalid command")
                continue
            instruct_command = instruct[0]
            instruct_island = instruct[1]
            instruct_species = instruct[2]
            instruct_parameter = instruct[3]

            if instruct_command not in ["mean", "median"]:
                print("Invalid command")
                continue

            input_list = get_island(instruct_island, instruct_species, instruct_parameter)

            if input_list == "Invalid":
                print("Invalid island, species, or parameter")
                continue

            printout = f"The {instruct_command} of {instruct_parameter} for {instruct_species} penguins on {instruct_island} island is {operator(instruct_command, input_list)}"
            print(printout)

            if log is None:
                log = LogWriter()
            log.add_log(f"Line {self.iteration}: {printout}")

        if log is not None:
            log.close()
        print("Exiting program. Data saved to log.txt")


class TestCodeMain(unittest.TestCase):

    # Tests general functionality of get_island
    def test_get_island_general(self):
        self.assertEqual(get_island("Dream", "Chinstrap", "bill_length_mm"), [46.5, 50, 51.3, 45.4, 52.7, 45.2, 46.1, 51.3, 46, 51.3, 46.6, 51.7, 47, 52, 45.9, 50.5, 50.3, 58, 46.4, 49.2, 42.4, 48.5, 43.2, 50.6, 46.7, 52, 50.5, 49.5, 46.4, 52.8, 40.9, 54.2, 42.5, 51, 49.7, 47.5, 47.6, 52, 46.9, 53.5, 49, 46.2, 50.9, 45.5, 50.9, 50.8, 50.1, 49, 51.5, 49.8, 48.1, 51.4, 45.7, 50.7, 42.5, 52.2, 45.2, 49.3, 50.2, 45.6, 51.9, 46.8, 45.7, 55.8, 43.5, 49.6, 50.8, 50.2])
        

    # Tests edge cases for get_island where an invalid dictionary is requested
    def test_get_island_edge(self):
        self.assertEqual(get_island("InvalidIsland", "Adelie", "bill_length_mm"), "Invalid")
        self.assertEqual(get_island("Biscoe", "InvalidSpecies", "bill_length_mm"), "Invalid")
        self.assertEqual(get_island("Biscoe", "Adelie", "InvalidParameter"), "Invalid")

    # Tests general functionality of operator
    def test_operator(self):
        self.assertEqual(operator("mean", [1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(operator("median", [1, 2, 3, 4, 5]), 3)
        self.assertEqual(operator("mean", [1, 2, 3, 4]), 2.5)
        self.assertEqual(operator("median", [1, 2, 3, 4]), 2.5)
        self.assertEqual(operator("invalid", [1, 2, 3]), None)

    # Tests general functionality of import_penguins
    def test_import_penguins_general(self):
        self.assertIn("Biscoe", ImportPenguins.PenguinData)
        self.assertIn("Adelie", ImportPenguins.PenguinData["Biscoe"])
        self.assertIn("bill_length_mm", ImportPenguins.PenguinData["Biscoe"]["Adelie"])
        self.assertEqual(len(ImportPenguins.PenguinData["Biscoe"]["Adelie"]["bill_length_mm"]), 44)


    # Tests edge cases for import_penguins where an island/species/parameter has fewer entries
    # Testing for Torgersen-Adelie which has 51 entries because of an 'NA' in the dataset, while there are 52 rows total for that island/species
    def test_import_penguins_edge(self):
        self.assertIn("Torgersen", ImportPenguins.PenguinData)
        self.assertIn("Adelie", ImportPenguins.PenguinData["Torgersen"])
        self.assertIn("bill_length_mm", ImportPenguins.PenguinData["Torgersen"]["Adelie"])
        self.assertEqual(len(ImportPenguins.PenguinData["Torgersen"]["Adelie"]["bill_length_mm"]), 51)


class main():
    #ImportPenguins()
    #CommandLine.run()
    unittest.main(verbosity=2)

if __name__ == '__main__':
        main()
