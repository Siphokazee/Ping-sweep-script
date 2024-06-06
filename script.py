import subprocess

def ping_sweep(ip_address, subnet_mask):
  
  ip_binary = format(int(ip_address.split(".")[0]), '08b') + "." + \
              format(int(ip_address.split(".")[1]), '08b') + "." + \
              format(int(ip_address.split(".")[2]), '08b') + "." + \
              format(int(ip_address.split(".")[3]), '08b')
  mask_binary = format(int(subnet_mask.split(".")[0]), '08b') + "." + \
                format(int(subnet_mask.split(".")[1]), '08b') + "." + \
                format(int(subnet_mask.split(".")[2]), '08b') + "." + \
                format(int(subnet_mask.split(".")[3]), '08b')

  
  usable_bits = 0
  for char in mask_binary:
    if char == "1":
      usable_bits += 1

  
  for i in range(2** (32 - usable_bits)):
    
    current_ip_binary = ip_binary[: (32 - usable_bits)] + format(i, '0' + str(usable_bits) + 'b')

    
    current_ip_address = ".".join([str(int(b, 2)) for b in current_ip_binary.split(".")])


    ping_result = subprocess.run(["ping", "-c", "1", current_ip_address], capture_output=True, text=True)

    
    if ping_result.returncode == 0:
      print(f"Host found: {current_ip_address}")


ip_address = "192.168.1.0"
subnet_mask = "255.255.255.0"
ping_sweep(ip_address, subnet_mask)
