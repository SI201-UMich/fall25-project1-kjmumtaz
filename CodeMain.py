# Kawani J. Mumtaz
# Fall 2025
# Project 1
# Contributor: Kawani J. Mumtaz (Just Me)
# AI Usage: Debugging help from ChatGPT

import unittest
import os
import csv

def get_island(island, species, parameter):

    values_list = []

    for values in ImportPenguins.PenguinData[island][species][parameter]:
        values_list.append(values)


def operator(command):

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


class CommandLine():

    iteration = 0

    while iteration >= 0:

        instruct = input("Enter command: ")
        instruct = instruct.split()
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

        get_island(instruct_island, instruct_species, instruct_parameter)

        print(f"The {instruct_command} of {instruct_parameter} for {instruct_species} on {instruct_island} is {operator(instruct_command)}")



    print("Exiting program.")




class Main():
    ImportPenguins()
    print(ImportPenguins.PenguinData)
