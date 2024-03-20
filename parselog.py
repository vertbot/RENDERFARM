filename = "Team Render Server Job Log .txt"  # Replace with the actual path to your file

with open(filename, "r") as file:
    for line in file:
        if "Rendering frame" in line:
            names = line.split()  # Split the line into words
            for name in names:
                if name.startswith("DM-RENDER-"):
                    print(name)  # Do whatever you want with the name
