from jenkinsdashboard.ui.ui import Row, Cell
import shutil
import os


class Dashboard():
    def __init__(self, ci):
        terminal_size = shutil.get_terminal_size()
        self.terminal_width = terminal_size[0]
        self.ci = ci

    def render(self, ci_rows):
        os.system('cls||echo -e \\\\033c')
        for ci_row in ci_rows:
            ci_row.render()

    def generate(self):
        project_list = self.ci.project_list()
        ci_rows = []
        for project in project_list:
            cell = Cell(project['name'], right_aligned=False,
                        is_header=True, color='white')
            row_title = Row([cell], self.terminal_width)
            ci_rows.append(row_title)

            project_info = self.ci.project(project['name'])
            if 'PipelineMultiBranch' in project_info['_class']:
                for job in project_info['jobs']:
                    job_info = self.ci.job(project['name'], job['name'])
                    build_info = self.ci.build_multibranch(
                        project['name'],
                        job['name'],
                        job_info['lastBuild']['number']
                    )

                    if build_info['building']:
                        row_job = Row(
                            [Cell(job_info['name'], right_aligned=False),
                                Cell(str(build_info['number']),
                                     right_aligned=True),
                                Cell('BUILDING', right_aligned=True)
                             ], self.terminal_width)
                        ci_rows.append(row_job)
                    else:
                        row_job = Row(
                            [Cell(job_info['name'], right_aligned=False),
                                Cell(str(build_info['number']),
                                     right_aligned=True),
                                Cell(build_info['result'],
                                     right_aligned=True,
                                     color=self.color_by_result(
                                         build_info['result'])
                                     )
                             ], self.terminal_width)
                        ci_rows.append(row_job)
        return ci_rows

    def color_by_result(self, result):
        color = ''
        if result == 'FAILURE':
            color = 'red'
        elif result == 'SUCCESS':
            color = 'green'
        elif result == 'BUILDING':
            color = 'white'

        return color
