import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def create_christmas_cards(names_file, template_file, output_dir):
    template = read_file(template_file)
    names = read_file_lines(names_file)
    os.makedirs(output_dir, exist_ok=True)
    for name in names:
        card = template.replace('NAME', name)
        write_to_file(f'{output_dir}/{name}.txt', card)

def main(): 
    create_christmas_cards('employees.txt', 'template.txt', 'christmasCards')

if __name__ == "__main__":
    main()
    