import socket
import time

# connection settings
EV3_MAC_ADDRESS = "00:16:53:5F:11:CE"  # CHANGE THIS to your EV3's MAC address
EV3_PORT = 1  # RFCOMM port (usually 1)

# ==================== Bluetooth ====================
class BT:
    def __init__(self):
        self.bt_socket = None
        self.connected = False

    def connect_bluetooth(self):
            """Connect to EV3 via Bluetooth RFCOMM socket (native Python socket, no PyBluez needed)"""
            try:
                print(f"Connecting to EV3 at {EV3_MAC_ADDRESS}...")
                self.bt_socket = socket.socket(
                    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
                )
                self.bt_socket.settimeout(10)  # 10 second connection timeout
                self.bt_socket.connect((EV3_MAC_ADDRESS, EV3_PORT))
                self.bt_socket.settimeout(None)  # No timeout for normal operation
                self.connected = True
                print("Connected to EV3 successfully!")
                return True
            except OSError as e:
                print(f"Bluetooth connection failed: {e}")
                self.connected = False
                return False

    def disconnect_bluetooth(self):
        """Cleanly disconnect from EV3"""
        self.tracking = False
        if self.bt_socket:
            try:
                self.send_stop_command()
                time.sleep(0.1)
                self.bt_socket.close()
            except:
                pass
        self.connected = False
        print("Disconnected from EV3")

    def send_message(self, message):
        """Send a message string to EV3"""
        if not self.connected or not self.bt_socket:
            return False
        try:
            # print(f"[TX] sending: {message!r}")
            self.bt_socket.sendall((message + "\r\n").encode())
            print(f"[TX] sent OK")
            return True
        except OSError as e:
            print(f"Send failed: {e}")
            self.connected = False
            return False

# ==================== Main ====================

def main():
    bt = BT()
    bt.connect_bluetooth()
    cmds = ["A, 44.5, 90.0",
            "F, 50",
            "B, 100",
            "H"
            ]
    for cmd in cmds:
        bt.send_message(cmd)
    print('All commands have been sent!')
    bt.disconnect_bluetooth()

if __name__ == "__main__":
    main()