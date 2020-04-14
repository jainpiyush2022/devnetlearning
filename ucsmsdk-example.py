from ucsmsdk.ucshandle import UcsHandle
# Create a connection handle
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")

# Login to the server
handle.login()

object_array = handle.query_classid(class_id="computeBlade")

for object in object_array:
    print(object.dn,object.num_of_cpus,object.available_memory)

blade = handle.query_dn('sys/chassis-3/blade-1')
print(blade)


# Logout from the server
handle.logout()