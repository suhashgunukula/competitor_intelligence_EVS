import subprocess

user_input = input("Enter the competitor list you want to run and see:")

if user_input == "Avira": # working
    subprocess.run(["python","Avira_File.py"], shell=True)
elif user_input == "McAfee":
    subprocess.run(["python", "McAfee_file.py"], shell=True)
elif user_input == "Bitdefender":
    subprocess.run(["python", "Bitdefender_file.py"], shell=True)
else:
    print("Invalid input!")