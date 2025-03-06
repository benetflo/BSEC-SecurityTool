import socket

# Function to display help commands and instructions
def help_commands():
    print("========HELP========")
    print("PLEASE NOTE SPACES BETWEEN PROMPTS")
    print("Commands:")
    print("Full scan (ports 1 - 65536) ==  {TARGET_IP}")
    print("Targeted port scan (single port) ==  {TARGET_IP} {PORT}")
    print("Custom range scan == {TARGET_IP} {FLOOR_PORT} {CEILING_PORT}")
    print("====================")


# Function to perform the port scanning
def port_scanner(target_IP, s_port, port_floor, port_ceiling):
    # Create a socket object for TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set default timeout to 1 second for socket connection
    socket.setdefaulttimeout(1)

    # If both port floor and ceiling are specified (range scan)
    if port_floor and port_ceiling:
        for i in range(port_floor, port_ceiling + 1):  # Loop through port range
            try: 
                # Try to connect to the port on the target IP
                result = s.connect_ex((target_IP, i))
                if result == 0:
                    print(f"Port {i} is open on {target_IP}")
                else:
                    print(f"Port {i} is closed on {target_IP}")
            except socket.gaierror as e:  # Handle errors like invalid IP
                print(f"Invalid IP {e}")
    
    # If a single port is specified (single port scan)
    elif s_port:
        try:
            # Try to connect to the single port
            result = s.connect_ex((target_IP, s_port))
            if result == 0:
                print(f"Port {s_port} is open on {target_IP}")
            else:
                print(f"Port {s_port} is closed on {target_IP}")
        except socket.gaierror as e:  # Handle errors like invalid IP
            print(f"Invalid IP {e}")
    
    # Full port scan if no range or single port is given (ports 1 to 65536)
    else:
        try:
            no_open_ports = False
            print("Scanning...")
            for i in range(1, 65536):  # Scan ports from 1 to 65536
                result = s.connect_ex((target_IP, i))
                if result == 0:
                    print(f"Port {i} is open on {target_IP}")
                    no_open_ports = True
            if not no_open_ports:
                print(f"No open ports on {target_IP}")
                
        except socket.gaierror as e:  # Handle errors like invalid IP
            print(f"Invalid IP {e}")

    # Close the socket after the scan
    s.close()


# Function to handle user input
def input_values():
    while 1:
        # Take input from the user
        user_input = input("BSEC-Port-Scan$ ")
        
        # If the user inputs '/help', display the help commands
        if user_input == "/help":
            help_commands()
        elif user_input == "exit":
            return None, None
        else:
            # Split the input string into a list of words
            split_input = user_input.split()
            len_of_split_input = len(split_input)
            
            # Check if the input format is valid (should be between 1 to 3 components)
            if len_of_split_input < 1 or len_of_split_input > 3:
                print("Invalid format! type '/help' for list of commands")
            else:
                # Return the split input and the number of components
                return split_input, len_of_split_input


# Function to assign values based on user input
def assign_values(inp_str ,len_of_string):
    ip = ""
    p_floor = ""
    p_ceiling = ""
    s_port = ""
    
    # If there are 3 inputs, assume it's a range scan
    if len_of_string == 3:
        ip = inp_str[0]  # First value is the target IP
        p_floor = int(inp_str[1])  # Second value is the port floor
        p_ceiling = int(inp_str[2])  # Third value is the port ceiling
        return ip, p_floor, p_ceiling
    # If there are 2 inputs, assume it's a single port scan
    elif len_of_string == 2:
        ip = inp_str[0]  # First value is the target IP
        s_port = int(inp_str[1])  # Second value is the single port
        return ip, s_port
    # If there is only 1 input, assume it's just the target IP
    elif len_of_string == 1:
        ip = inp_str[0]  # First value is the target IP
        return ip
    else:
        print("Invalid format! type '/help' for list of commands")

def run():
	# Variables to store the values of the IP and ports
	target_IP, single_port, port_floor, port_ceiling = "", "", "", ""

	# Infinite loop to continuously ask for input and perform port scan
	while 1:
		# Get user input

		print("\ntype '/help' for commands")
		cmd_str, cmd_str_len = input_values()

		if cmd_str == None and cmd_str_len == None:
			break

		# Based on the number of inputs, assign appSropriate values
		match cmd_str_len:
			case 1:
				target_IP = assign_values(cmd_str, cmd_str_len)
			case 2:
				target_IP, single_port = assign_values(cmd_str, cmd_str_len)
			case 3:
				target_IP, port_floor, port_ceiling = assign_values(cmd_str, cmd_str_len)
			case _:
				pass

		# Perform the port scan based on the assigned values
		port_scanner(target_IP, single_port, port_floor, port_ceiling)

		# Reset the variables for the next round of input
		target_IP = ""
		single_port = ""
		port_floor = ""
		port_ceiling = ""
