import os
import subprocess
import datetime
import sys

class QuantumMate:
    def __init__(self):
        self.system_restore_command = "rstrui.exe"
        self.system_restore_point_command = "wmic.exe /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint \"QuantumMate Restore Point\", 100, 7"

    def create_restore_point(self):
        """
        Create a system restore point.
        """
        try:
            print("Creating a system restore point.")
            result = subprocess.run(self.system_restore_point_command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("Restore point created successfully.")
            else:
                print("Failed to create a restore point.")
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred: {e}")

    def restore_system(self):
        """
        Open the system restore interface to allow the user to restore the system.
        """
        try:
            print("Opening System Restore...")
            os.system(self.system_restore_command)
        except Exception as e:
            print(f"An error occurred: {e}")

    def list_restore_points(self):
        """
        List available restore points.
        """
        try:
            print("Listing available restore points...")
            result = subprocess.run("vssadmin list shadows", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print("Failed to list restore points.")
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    print("Welcome to QuantumMate - Your System Restoration Companion")
    qm = QuantumMate()

    while True:
        print("\nPlease select an option:")
        print("1. Create a System Restore Point")
        print("2. Restore System to a Previous State")
        print("3. List Available Restore Points")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            qm.create_restore_point()
        elif choice == '2':
            qm.restore_system()
        elif choice == '3':
            qm.list_restore_points()
        elif choice == '4':
            print("Exiting QuantumMate. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if os.name == 'nt':
        main()
    else:
        print("QuantumMate is designed to run on Windows systems only.")