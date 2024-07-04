def get_system_resourses():
    resources = {
        "CPU" : "70%",
        "Memory" : "55%",
        "Disk" : "80%"
    }
    return resources

def display_resources():
    resources = get_system_resourses()
    print("Current system resource usage:")
    for  resource, usage in resources.items():
        print(f"{resource}: {usage}")