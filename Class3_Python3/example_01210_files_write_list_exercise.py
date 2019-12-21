# use the list: particles = ["protonen", "neutronen", "elektronen"]
# open a file and write the elements of the list seperated by a comma into the file

particles = ["protonen", "neutronen", "elektronen"]
file_name = "particles.txt"

with open (file_name, "w") as f:
    content = ",".join(particles)
    f.write(content)

    # oder f.write(",".join(particles))