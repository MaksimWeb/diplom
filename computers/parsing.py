from .models import Application, Computer


def parsing():
    computer = {}

    file = open('C:/Users/Максим/Desktop/1.txt')
    line = file.readline()
    computer['title'] = line.split('\\\\')[1][:-1]
    while line := file.readline():
        if 'Applications:' in line:
            break
        splitted_line = line.split(':')
        if splitted_line[0] == 'Kernel version':
            computer['kernel_version'] = splitted_line[1].strip()
        elif splitted_line[0] == 'Product type':
            computer['product_type'] = splitted_line[1].strip()
        elif splitted_line[0] == 'Product version':
            computer['product_version'] = splitted_line[1].strip()
        elif splitted_line[0] == 'Processor type':
            computer['processor_type'] = splitted_line[1].strip()
        elif splitted_line[0] == 'Physical memory':
            computer['physical_memory'] = splitted_line[1].strip()
        elif splitted_line[0] == 'Video driver':
            computer['video_driver'] = splitted_line[1].strip()

    apps = []
    while line := file.readline():
        if '-' not in line:
            continue
        splitted_line = line.split('-')
        app = Application.objects.create(application_name=splitted_line[0],
                                         application_version=splitted_line[1] or None)
        apps.append(app)

    saved_computer = Computer.objects.create(**computer)
    saved_computer.applications.set(apps)
    saved_computer.save()
