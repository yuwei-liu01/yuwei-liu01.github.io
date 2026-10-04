# Extracted from 0831/IK模型最终调试0831.gh (first CodeInput).
import System
from System.IO.Ports import SerialPort

def send_to_serial_port(input_string, port_number, start_sending):
    sent_string = ""
    success = False

    if start_sending:
        port_name = 'COM' + str(port_number)
        baud_rate = 9600

        try:
            myPort = SerialPort(port_name, baud_rate)
            myPort.Parity = System.IO.Ports.Parity.None
            myPort.StopBits = System.IO.Ports.StopBits.One
            myPort.DataBits = 8
            myPort.Handshake = System.IO.Ports.Handshake.None

            myPort.Open()
            if not myPort.IsOpen:
                print "Failed to open port."
                return sent_string, success

            myPort.WriteLine(input_string)

            sent_string = input_string
            success = True

            myPort.Close()
        except Exception as e:
            print "Something went wrong:", e

    return sent_string, success

# Outputs
sent_string, success = send_to_serial_port(input_string, port_number, start_sending)
