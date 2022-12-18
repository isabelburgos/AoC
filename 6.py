file = open("input6.txt","r")

signal = file.read()

def search(signal, packet_length):
    for i in range(len(signal)):
        packet = signal[i:i+packet_length]
        if len(set(packet)) == packet_length:
            print(packet,"at",i+packet_length)
            break

search(signal,4)
search(signal,14)