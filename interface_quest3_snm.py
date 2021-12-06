#!usr/bin/env python3

#Importing necessary modules
import sys
import paramiko
import time
import getpass
import re
import sys
import emoji

def fetch_addresses(connection,remote_ip):
    data_dict = {"IP": {"lo_IP" : "",
                         "eth0_IP":"" , 
                         "eth1_IP":"" },

                         "MAC": 
                         {"lo_MAC":"" ,
                         "eth0_MAC":"",
                         "eth1_MAC":"" },
                         
                         "TYPE": {"Loopback":"lo", "Ethernet0": "eth0","Ethernet1":"eth1"}
                         }

    # for Loopback

    """
    Step1: Sending the connection request with IP address
    command on loopback interface
    """
    connection.send("ip a s lo\n")
    time.sleep(1)

    """
    Step2: Recieving output of the send request.
    return type is byte, therefore converting it to string to
    parse the output in the next step
    """
    output_lo = connection.recv(65535)
    output_lo = str(output_lo)

    """
    Step3: Parsing the output through regular expressions
    
    """
    ip_address = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", output_lo)
    mac_address = re.findall(r"[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}", output_lo)

    """
    Storing the output in dictionary data structure
    """

    data_dict["MAC"]["lo_MAC"] = mac_address
    data_dict["IP"]["lo_IP"] = ip_address

    # for Ethernet0

    """
    Step1: Sending the connection request with IP address
    command on loopback interface
    """
    connection.send("ip a s eth0\n")
    time.sleep(1)

    """
    Step2: Recieving output of the send request.
    return type is byte, therefore converting it to string to
    parse the output in the next step
    """
    output_eth0 = connection.recv(65535)
    output_eth0 = str(output_eth0)

    """
    Step3: Parsing the output through regular expressions
    
    """
    ip_address = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", output_eth0)
    mac_address = re.findall(r"[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}", output_eth0)

    """
    Storing the output in dictionary data structure
    """

    data_dict["MAC"]["eth0_MAC"] = mac_address
    data_dict["IP"]["eth0_IP"] = ip_address


    # for Ethernet1

    """
    Step1: Sending the connection request with IP address
    command on loopback interface
    """
    connection.send("ip a s eth1\n")
    time.sleep(1)

    """
    Step2: Recieving output of the send request.
    return type is byte, therefore converting it to string to
    parse the output in the next step
    """
    output_eth1 = connection.recv(65535)
    output_eth1 = str(output_eth1)

    """
    Step3: Parsing the output through regular expressions
    
    """
    ip_address = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", output_eth1)
    mac_address = re.findall(r"[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}", output_eth1)

    """
    Step4:Storing the output in dictionary data structure
    """

    data_dict["MAC"]["eth1_MAC"] = mac_address
    data_dict["IP"]["eth1_IP"] = ip_address




    print(emoji.emojize(":slightly_smiling_face:"),"Welcome to our program")
    User_input = input("Enter your choice - Type?, IP?, MAC?, Exit?: ")

    if (User_input == "Type"):
          print(f"List of Interface Types on machine {remote_ip}") 
          print(data_dict["TYPE"])
    elif (User_input == "IP"):
          print(f"List of IP addresses on machine {remote_ip}") 
          print(data_dict["IP"])
    elif (User_input == "MAC"):
          print(f"List of MAC addresses on machine {remote_ip}") 
          print(data_dict["MAC"])
    elif (User_input == "Exit"):
          print(f"Exiting.... {remote_ip}") 
          sys.exit()
    else:
        print("The choices are case sensitive,Please try again") 
             

def interface_details():

    
     #Obtaining user input - Remote IP, username and password
     remote_ip= input("Enter the remote device's IP address: ")
     username = input("Enter the username: ")
     password = getpass.getpass(stream = sys.stderr)

     #Establishing a session for SSH connection with remote device
     session = paramiko.SSHClient()
     session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     try:
          session.connect(remote_ip, username=username, password=password)

     except paramiko.AuthenticationException:
          print("Unable to login. Please retry.\n")
          sys.exit()

     #Invoking a shell connection
     connection = session.invoke_shell()
     fetch_addresses(connection,remote_ip)
     print(emoji.emojize(":slightly_smiling_face:"),"Thank You for using our program")


     #Terminating the SSH connection session
     session.close()

# Function calling
interface_details()
     

    



    

