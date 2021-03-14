from .models import Application, Computer


class App:
    def __init__(self, application_name, application_version):
        self.application_name = application_name
        self.application_version = application_version


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
    else:
        newApps = []
        oldApp = Application.objects.filter(computer_id=comp.id)

        while line := file.readline():
            if '-' not in line:
                continue
            splitted_line = line.split('-')
            updatedApp = App(application_name=splitted_line[0], application_version=splitted_line[1] or None)
            newApps.append(updatedApp)

        newAppsCopy = newApps.copy()

        for newItem in newApps:
            for oldItem in oldApp:
                if newItem.application_name != oldItem.application_name:
                    continue
                elif newItem.application_version != oldItem.application_version:
                    oldItem.application_version = newItem.application_version
                    oldItem.save()

        for oldItem in oldApp:
            for newItem in newApps:
                if oldItem.application_name == newItem.application_name:
                    newAppsCopy.remove(newItem)

        for refresh in newAppsCopy:
            if len(newAppsCopy) > 0:
                Application.objects.create(application_version=refresh.application_version, computer_id=comp.id,
                                           application_name=refresh.application_name)
