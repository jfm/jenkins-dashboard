import requests


class Jenkins:

    def __init__(self, host, username, password):
        self.host = host
        self.auth = (username, password)

    def api_get(self, url):
        response = requests.get(url + '/api/json', auth=self.auth)
        if response.status_code == 200:
            return response.json()

    def project_list(self):
        return self.api_get(self.host)['jobs']

    # https://jenkins.onboarding.liquid.int.tdk.dk/job/event-handler/api/json
    def project(self, project_name):
        url = self.host + '/job/' + project_name
        return self.api_get(url)

    # https://jenkins.onboarding.liquid.int.tdk.dk/job/event-handler/job/master/api/json
    def job(self, project_name, job_name):
        url = self.host + '/job/' + project_name + '/job/' + job_name
        return self.api_get(url)

    # https://jenkins.onboarding.liquid.int.tdk.dk/job/metrics/4/api/json
    def build(self, job_name, build_number):
        url = self.host + '/job/' + job_name + '/' + str(build_number)
        return self.api_get(url)

    # https://jenkins.onboarding.liquid.int.tdk.dk/job/event-handler/job/master/17/api/json
    def build_multibranch(self, project_name, branch_name, build_number):
        url = self.host + '/job/' + project_name + '/job/' + branch_name + \
            '/' + str(build_number)
        return self.api_get(url)

    def fetch_all_last_builds(self):
        build_info_list = []
        project_list = self.project_list()
        for project in project_list:
            project_info = self.project(project['name'])
            if 'PipelineMultiBranch' in project_info['_class']:
                for job in project_info['jobs']:
                    job_info = self.job(project['name'], job['name'])
                    last_build_number = job_info['lastBuild']['number']
                    build_info = self.build_multibranch(
                        project['name'], job['name'], last_build_number)
                    build_info_list.append(build_info)

        return build_info_list