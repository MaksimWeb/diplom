from .models import Application, Computer


def parsing():
    file = open('C:/Users/Максим/Desktop/1.txt')
    line = file.readline()
    comp, created = Computer.objects.get_or_create(title=line.split('\\\\')[1][:-2])
    while line := file.readline():
        if 'Applications:' in line:
            break
        splitted_line = line.split(':')
        if splitted_line[0] == 'Kernel version':
            comp.kernel_version = splitted_line[1].strip()
        elif splitted_line[0] == 'Product type':
            comp.product_type = splitted_line[1].strip()
        elif splitted_line[0] == 'Product version':
            comp.product_version = splitted_line[1].strip()
        elif splitted_line[0] == 'Processor type':
            comp.processor_type = splitted_line[1].strip()
        elif splitted_line[0] == 'Physical memory':
            comp.physical_memory = splitted_line[1].strip()
        elif splitted_line[0] == 'Video driver':
            comp.video_driver = splitted_line[1].strip()

    comp.save()
    if created:
        apps = []
        while line := file.readline():
            if '-' not in line:
                continue
            splitted_line = line.split('-')
            app = Application.objects.create(application_name=splitted_line[0],
                                             application_version=splitted_line[1] or None)
            apps.append(app)

        comp.applications.set(apps)
        comp.save()
