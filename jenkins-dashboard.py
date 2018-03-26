from jenkinsdashboard.ci.jenkins import Jenkins
from jenkinsdashboard.ui.dashboard import Dashboard
import time


if __name__ == '__main__':
    # jenkins = Jenkins('http://10.0.0.102:18081', 'jfm', 'c3po4all')
    jenkins = Jenkins(
        'http://jenkins.onboarding.liquid.int.tdk.dk', 'admin', '0nboarding')

    dashboard = Dashboard(jenkins)
    while True:
        ci_rows = dashboard.generate()
        dashboard.render(ci_rows)
        time.sleep(30)
