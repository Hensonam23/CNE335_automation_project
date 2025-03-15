# CNE335 Final Project
# Aaron Henson
# CNE 335 Winter 2025

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Aaron Henson")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results
    server = Server("54.190.35.62")
    if server.ping():
        print("Ping successful")
    else:
        print("Ping failed")
