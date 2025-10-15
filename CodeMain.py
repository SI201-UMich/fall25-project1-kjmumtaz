# Kawani J. Mumtaz
# Fall 2025
# Project 1
# Contributor: Kawani J. Mumtaz (Just Me)
# AI Usage: Debugging help from ChatGPT

import unittest
import os
import csv

class ImportPenguins():

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "penguins.csv")

    PenguinData = {}

    with open(full_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            species = row[0]
            island = row[1]
            bill_length_mm = row[2]
            bill_depth_mm = row[3]
            flipper_length_mm = row[4]
            body_mass_g = row[5]

            if island not in PenguinData:
                PenguinData[island] = {}
            
            if species not in PenguinData[island]:
                PenguinData[island][species] = {bill_depth_mm: [], bill_length_mm: [], flipper_length_mm: [], body_mass_g: []}

            PenguinData[island][species][bill_depth_mm].append(float(bill_depth_mm))
            PenguinData[island][species][bill_length_mm].append(float(bill_length_mm))
            PenguinData[island][species][flipper_length_mm].append(float(flipper_length_mm))
            PenguinData[island][species][body_mass_g].append(float(body_mass_g)) 






class Main():
    ImportPenguins()
