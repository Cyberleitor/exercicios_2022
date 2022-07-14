filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for index in filenames:
    if '.hpp' in index:
        newfilenames.append(index.replace('.hpp', '.h'))
    else:
        newfilenames.append(index)

print(newfilenames)
