from jenkinsdashboard.ui.ui import UI
from jenkinsdashboard.ci.jenkins import Jenkins


if __name__ == '__main__':
    ui = UI()
    # jenkins = Jenkins('http://10.0.0.102:18081', 'jfm', 'c3po4all')
    jenkins = Jenkins(
        'http://jenkins.onboarding.liquid.int.tdk.dk', 'admin', '0nboarding')

    build_info_list = jenkins.fetch_all_last_builds()
    for build_info in build_info_list:
        if build_info['building']:
            print('BUILDING - ' + build_info['fullDisplayName'])
        else:
            print(build_info['result'] + '  - ' +
                  build_info['fullDisplayName'])
