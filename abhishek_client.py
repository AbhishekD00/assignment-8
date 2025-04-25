# import socket

# def main():
#     # Prompt user for the server IP address
#     while True:
#         server_ip = input("Enter the server IP address: ").strip()
#         if server_ip:
#             break
#         print("IP address cannot be empty.")

#     # Prompt user for the server port
#     while True:
#         server_port_str = input("Enter the server port number: ").strip()
#         try:
#             server_port = int(server_port_str)
#             break
#         except ValueError:
#             print("Invalid port number. Please enter a valid integer.")

#     # Attempt to create a socket and connect
#     try:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#             client_socket.connect((server_ip, server_port))
#             print(f"Connected to server at {server_ip}:{server_port}.")

#             # Continuously send messages and receive responses
#             while True:
#                 message = input("Enter a message to send (type 'exit' to quit): ")
#                 if message.lower() == 'exit':
#                     print("Exiting client.")
#                     break

#                 # Send the message to the server
#                 client_socket.sendall(message.encode())

#                 # Receive the server's response
#                 response = client_socket.recv(1024)
#                 if not response:
#                     print("Connection closed by server.")
#                     break

#                 print("Server response:", response.decode())
#     except socket.gaierror:
#         print("Invalid IP address. Could not resolve.")
#     except ConnectionRefusedError:
#         print("Connection refused. Is the server running and listening on the given port?")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == '__main__':
#     main()

import socket

def main():
    valid_queries = [
        "What is the average moisture inside my kitchen fridge in the past three hours?",
        "What is the average water consumption per cycle in my smart dishwasher?",
        "Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?"
    ]

    while True:
        server_ip = input("Enter the server IP address: ").strip()
        if server_ip:
            break
        print("IP address cannot be empty.")

    while True:
        server_port_str = input("Enter the server port number: ").strip()
        try:
            server_port = int(server_port_str)
            break
        except ValueError:
            print("Invalid port number. Please enter a valid integer.")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, server_port))
            print(f"Connected to server at {server_ip}:{server_port}.")

            while True:
                print("\nValid Queries:")
                for query in valid_queries:
                    print(f"- {query}")
                message = input("\nEnter your query (or type 'exit' to quit): ")

                if message.lower() == 'exit':
                    print("Exiting client.")
                    break

                if message not in valid_queries:
                    print("\n❌ Sorry, this query cannot be processed.")
                    print("Please try one of the following:")
                    for query in valid_queries:
                        print(f"- {query}")
                    continue

                client_socket.sendall(message.encode())
                response = client_socket.recv(1024)
                if not response:
                    print("Connection closed by server.")
                    break

                print("\n✅ Server response:", response.decode())
    except socket.gaierror:
        print("Invalid IP address. Could not resolve.")
    except ConnectionRefusedError:
        print("Connection refused. Is the server running and listening on the given port?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
