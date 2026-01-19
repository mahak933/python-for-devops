import psutil

def system_health():
    # Takes threshold values (CPU, disk, memory)
    cpu_threshold = float(input("Enter the CPU Threshold")) 
    disk_threshold = float(input("Enter the Disk Threshold")) 
    memory_threshold = float(input("Enter the Memory Threshold")) 

    # Fetch system metrics using psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    print(cpu_usage)
    disk_usage = psutil.disk_usage('/').percent
    print(disk_usage)
    memory_usage = psutil.virtual_memory().percent
    print(memory_usage)

    if cpu_threshold > cpu_usage:
        print("CPU Usage Alert")
    elif disk_threshold > disk_usage:
        print("Disk Usage Alert")
    elif memory_threshold > memory_usage:
        print("Memory Usage Alert")
    else:
        print("Everything is okay!")        


system_health()