from pykeepass import PyKeePass as pkp


# load database
kp = pkp(filename='input file name', password='input keepass password')

# find any group by its name
group = kp.find_groups(name='input group title', first=True)

# find entry by its title
entry = kp.find_entries(title='input entry title', first=True)

# retrieve the associated password
print(entry.password)

print(entry.username)





