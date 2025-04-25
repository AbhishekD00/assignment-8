# import socket

# def main():
#      # Ask user for IP and port (default IP to 0.0.0.0 if blank).
#     host = input("Enter the IP address to bind the server (leave blank for '0.0.0.0'): ").strip()
#     if not host:
#         host = '0.0.0.0'
    
#     while True:
#         port_str = input("Enter the port number to bind the server: ").strip()
#         try:
#             port = int(port_str)
#             break
#         except ValueError:
#             print("Invalid port number. Please enter a valid integer.")
#      # Create a TCP/IP socket.
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         server_socket.bind((host, port))
#         server_socket.listen(1)
#         print(f"Server listening on {host}:{port}...")

#         while True:
#             print("Waiting for a client to connect...")
#             conn, addr = server_socket.accept()
#             print(f"Client connected from {addr}.")

#             with conn:
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         print("Client disconnected.")
#                         break
                    
#                     # Decode and print the received message
#                     client_msg = data.decode()
#                     print(f"Received from {addr}: {client_msg}")

#                     # Convert the received message to uppercase and send it back
#                     response = client_msg.upper()
#                     conn.sendall(response.encode())

# if __name__ == '__main__':
#     main()




import socket

def main():
    host = input("Enter the IP address to bind the server (leave blank for '0.0.0.0'): ").strip()
    if not host:
        host = '0.0.0.0'

    while True:
        port_str = input("Enter the port number to bind the server: ").strip()
        try:
            port = int(port_str)
            break
        except ValueError:
            print("Invalid port number. Please enter a valid integer.")

    responses = {
        "What is the average moisture inside my kitchen fridge in the past three hours?":
            "The average moisture in your kitchen fridge over the past 3 hours is 45%.",
        "What is the average water consumption per cycle in my smart dishwasher?":
            "The average water consumption per cycle in your smart dishwasher is 3.2 gallons.",
        "Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?":
            "Your dishwasher consumed more electricity compared to the two refrigerators."
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        while True:
            print("Waiting for a client to connect...")
            conn, addr = server_socket.accept()
            print(f"Client connected from {addr}.")

            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("Client disconnected.")
                        break

                    client_msg = data.decode()
                    print(f"Received from {addr}: {client_msg}")

                    # Process the message
                    response = responses.get(client_msg, "Sorry, I don't have data for that query.")
                    conn.sendall(response.encode())

if __name__ == '__main__':
    main()
