import randomname

file_name = randomname.get_name() + '.txt'
with open(file_name, 'w') as f:
    f.write('Your content here.')