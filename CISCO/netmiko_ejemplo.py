from netmiko import ConnectHandler
switch = {"device_type": "cisco_nxos",
          "host": "sandbox-nxos-1.cisco.com",
          "port": 22, 
          "username": "admin",
          "password": "Admin_1234!"}

router = {"device_type": "cisco_nxos",
          "host": "sandbox-iosxe-latest-1.cisco.com",
          "port": 22, 
          "username": "developer",
          "password": "C1sco12345"}

conexionEquipo= ConnectHandler(**switch)
conexionEquipo.send_config_from_file(config_file="a.txt")
interface_cli = conexionEquipo.send_command("show ip interface brief")
print(interface_cli)
conexionEquipo.disconnect() 