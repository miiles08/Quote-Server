import socket

# Store the most recent connection info
last_ip = None
last_port = None

def connect_to_server(ip, port):
    """Connect to a quote server and receive a quote."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)  # 5 second timeout
        client_socket.connect((ip, port))
        
        # Receive the quote
        quote = client_socket.recv(1024).decode()
        client_socket.close()
        
        print(f"Quote from {ip}:{port}: {quote}")
        return True
    except socket.timeout:
        print(f"Connection timeout: Could not connect to {ip}:{port}")
        return False
    except ConnectionRefusedError:
        print(f"Connection refused: Could not connect to {ip}:{port}")
        return False
    except Exception as e:
        print(f"Error connecting to {ip}:{port}: {e}")
        return False

def main():
    global last_ip, last_port
    
    print("Quote Server CLI")
    print("Commands:")
    print("  (c)onnect - Enter IP and port to connect")
    print("  (r)etry   - Retry the most recent connection")
    print("  (q)uit    - Exit")
    print()
    
    while True:
        try:
            command = input("> ").strip().lower()
            
            if command == "quit" or command == "exit" or command == "q":
                print("Goodbye!")
                break
            
            elif command == "connect" or command == "c":
                address = input("Enter IP:PORT: ").strip()
                
                try:
                    if ':' not in address:
                        print("Invalid format. Please use IP:PORT (e.g., 127.0.0.1:25555)")
                        continue
                    
                    ip, port_str = address.rsplit(':', 1)
                    port = int(port_str)
                    
                    if connect_to_server(ip, port):
                        last_ip = ip
                        last_port = port
                except ValueError:
                    print("Invalid port number")
            
            elif command == "retry" or command == "r":
                if last_ip and last_port:
                    print(f"Retrying connection to {last_ip}:{last_port}...")
                    connect_to_server(last_ip, last_port)
                else:
                    print("No previous connection to retry")
            
            else:
                print("Unknown command. Use 'connect', 'retry', or 'quit'")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()

