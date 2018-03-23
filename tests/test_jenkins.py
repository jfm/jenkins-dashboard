from unittest.mock import patch
from nose.tools import assert_equal
import json

from jenkinsdashboard.ci.jenkins import Jenkins


jenkins = Jenkins(
    'http://jenkins.onboarding.liquid.int.tdk.dk',
    'admin',
    '0nboarding')


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json.loads(json_data)
        self.status_code = status_code

    def json(self):
        return self.json_data


def read_file(filename):
    with open(filename, 'r') as myfile:
        filedata = myfile.read()
    return filedata


def mocked_project_list(url, auth):
    json = read_file('tests/project_list.json')
    mock_response = MockResponse(json, 200)
    return mock_response


def mocked_project(url, auth):
    json = read_file('tests/project.json')
    mock_response = MockResponse(json, 200)
    return mock_response


def mocked_job(url, auth):
    json = read_file('tests/job.json')
    mock_response = MockResponse(json, 200)
    return mock_response


def mocked_build_multibranch(url, auth):
    json = read_file('tests/build_multibranch.json')
    mock_response = MockResponse(json, 200)
    return mock_response


@patch('jenkinsdashboard.ci.jenkins.requests.get',
       side_effect=mocked_project_list)
def test_project_list(mock_get):
    project_list = jenkins.project_list()
    assert_equal(len(project_list), 16)


@patch('jenkinsdashboard.ci.jenkins.requests.get', side_effect=mocked_project)
def test_project(mock_get):
    project = jenkins.project('test-project')
    assert 'lastBuild' in project
    assert project['lastBuild']['number'] == 4


@patch('jenkinsdashboard.ci.jenkins.requests.get', side_effect=mocked_job)
def test_job(mock_get):
    job = jenkins.job('test-project', 'master')
    assert job is not None
    assert job['buildable'] is True
    assert_equal(len(job['builds']), 1)


# @patch('jenkinsdashboard.ci.jenkins.requests.get', side_effect=mocked_build)
# def test_build(mock_get):
#     build = jenkins.build('test-project', 1)
#     assert build is not None
#     print(build)

@patch('jenkinsdashboard.ci.jenkins.requests.get',
       side_effect=mocked_build_multibranch)
def test_build_multibranch(mock_get):
    build = jenkins.build_multibranch('test-project', 'master', 1)
    assert build is not None
    assert 'WorkflowRun' in build['_class']
