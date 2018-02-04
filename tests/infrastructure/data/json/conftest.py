import json
from datetime import date, datetime
from pytest import fixture
from taskit.application.models.project import Project
from taskit.application.models.task import Task


def json_serialize(obj):
    """JSON serializer for objects not serializable by default"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type {} not serializable".format(type(obj)))


@fixture(scope='session')
def json_file(tmpdir_factory):
    file_name = tmpdir_factory.mktemp('data').join('taskit.json')
    test_dictionary = {
        "projects": {
            'P-1': vars(Project("Personal", uid="P-1")),
            'P-2': vars(Project("Work", uid="P-2")),
            'P-3': vars(Project("Errands", uid="P-3"))
        },
        "tasks": {
            'T-1': vars(Task("Buy the milk", uid="T-1")),
            'T-2': vars(Task("Make conference presentation", uid="T-2")),
            'T-3': vars(Task("Clean the kitchen", uid="T-3"))
        }
    }
    with open(str(file_name), 'w+') as f:
        json.dump(test_dictionary, f, default=json_serialize)
    return str(file_name)