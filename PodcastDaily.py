import todoist
from datetime import date, timedelta, datetime
import API_CONFIG

######
YESTERDAY = date.today() - timedelta(1)
YESTERDAY = YESTERDAY.strftime('%m%d%y')
######


class PodcastDaily:
    def __init__(self):
        self.api = todoist.TodoistAPI(API_CONFIG.TODOIST_ACCESS_TOKEN_KEY)
        self.api.sync()
        self.todo_projects = self.api.state['projects']

    def project_id(self, lookup_podcast_name="Weekly Podcasts 2"):
        for project in self.todo_projects:
            if project['name'] == lookup_podcast_name:
                return project['id']

    def project_data(self):
        id = self.project_id()
        data = self.api.projects.get_data(id)
        return data

    # Could check for any project in todoist
    def project_content(self):
        all_podcasts = {}
        podcasts_listened = []
        project_info = self.project_data()

        for item in reversed(project_info['items']):
            format_date = self.format_date(item['date_added'])
            if self.validate_date(format_date):
                podcast_format = self.project_details(item)
                podcasts_listened.append(podcast_format)

        all_podcasts[YESTERDAY] = podcasts_listened
        return all_podcasts

    def project_details(self, item):
        title, podcast = self.main_details(item['content'])
        podcast_format = self.format_podcast_statement(title, podcast)
        return podcast_format

    def validate_date(self, format_date):
        if YESTERDAY == format_date:
            return True

    def format_podcast_statement(self, title, podcast):
        return "You heard {0} from {1}".format(title, podcast)

    def format_date(self, yesterday):
        return datetime.strptime(yesterday, '%a %d %b %Y %X %z').strftime('%m%d%y')

    def main_details(self, content):
        main_info = content.split(':')
        podcast_brand, title_of_eps = main_info
        podcast_brand, title_of_eps = podcast_brand.strip(), title_of_eps.strip()
        return [title_of_eps, podcast_brand]

    @staticmethod
    def upload_yesterday():
        podcast_content = PodcastDaily()
        return podcast_content.project_content()
