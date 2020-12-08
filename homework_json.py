import json
import hashlib
import time


def generate_json_packet(message):
    print("Generating packet")

    message_hash = hashlib.md5(message.encode()).hexdigest()
    packet = {"message": message, "hash": message_hash}

    # Here is your code to print packet in json format and to return it
    json_packet = json.dumps(packet, indent=2)
    print(json_packet)

    return json_packet


def verify_json_packet(json_packet):
    # Here is your code to convert json_packet to Python structure
    packet = json.loads(json_packet)
    print(packet)
    print("Here is the packet in Python", packet)

    if hashlib.md5(packet["message"].encode()).hexdigest() == packet["hash"]:
        print("Packet is verified")
        return True
    else:
        print("Packet is broken")
        return False


def main_cycle():
    x = 0
    while True:
        print("Program started")

        message = "Message: " + str(x)
        print("Current message: ", message)
        print("Generating json packet from message")

        json_packet = generate_json_packet(message)
        time.sleep(0.1)

        if verify_json_packet(json_packet) is True:
            print("Packet is verified, going to next")
            x += 1
        else:
            print("Packet is broken, stopping")
            break


main_cycle()
