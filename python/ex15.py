from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.read())

print("""
Type the filename agan:""")
file_agan = input("> ")

txt_agan = open(file_agan)

print(txt_agan.read())

print("""
All of the steps above are summarized as code below:
'open(filename).read()'\n
And the output is same
""", open(filename).read())
