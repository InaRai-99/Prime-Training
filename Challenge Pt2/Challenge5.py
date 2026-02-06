# Validate packet start/end markers

packet = b'\x94Goodbye\x99'
valid_start = False
valid_end = False

if packet[0] == 0x02:
    valid_start = True
if packet[-1] == 0x03:
    valid_end = True

print(f"Packet: {packet}")
if valid_start and valid_end:
    content = packet[1:-1].decode('utf-8')
    print(f"Valid packet! Content: '{content}'")
else:
    print("Invalid packet markers")
