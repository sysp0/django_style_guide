import os
import shutil


_license = "{{cookiecutter.license}}"
jwt = "{{cookiecutter.use_jwt}}"
celery = "{{cookiecutter.use_celery}}"
project_slug = "{{cookiecutter.project_slug}}"

def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if _license == "None":
    delete_resource("LICENSE")

if jwt == "n":
    delete_resource(f"{project_slug}/authentication/")
    delete_resource(f"{project_slug}/users/")

if celery == "n":
    delete_resource(f"{project_slug}/tasks/")
    delete_resource(f"{project_slug}/config/settings/celery.py")

