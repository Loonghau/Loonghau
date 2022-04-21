import wmi

c = wmi.WMI()
# print(type(c.Win32_NetworkAdapterConfiguration(IPEnabled=1)))
mac = c.Win32_NetworkAdapterConfiguration(IPEnabled=1)[0].MACAddress
print(mac)
# for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
# print(interface.MACAddress)
# print(interface.Description, interface.MACAddress)
# for MAC_address in interface.MACAddress:
# print(MAC_address)
