Week 9 commit:
Work on branches player_login_logic
Deviated from gantt chart this week to continue additional features and finish work. Coach login was completed during the week. Worked on finishing player login logic. This work was begun on a separate branch (player_login_logic) Began work on playbook feature discussed on design document. Playbook feature is not functional at the moment.

Files edited
- SmartStats/roster/views.py
- SmartStats/roster/views/players.py
- SmartStats/roster/models.py
- SmartStats/roster/urls.py
- SmartStats/roster/templates/roster/playbook.html
- SmartStats/roster/templates/roster/playbookload.html
- SmartStats/roster/templates/roster/gallery.html

Week 8 commit:
Work on branches page_logic_lucas, master
- Merged page_logic_lucas to master
- Continued debuging of login page. Still having issues with csrf tokens. 
- Made templates for the realtimetracker and create team pages for use in page_logic_lucas branch. Not an accurate representation of the actual page, but for use in showing the homepage when the request is made to show it. 

Files edited:
- SmartStats/roster/views.py
- SmartStats/roster/urls.py
- SmartStats/roster/templates/roster/realtimetracker.html
- SmartStats/roster/templates/roster/createteam.html
- SmartStats/roster/templates/roster/register.html

Week 7 commit:

Work on branches: page_logic_lucas

-Deviated from gantt chart to complete much needed work on the login and registration functionality of the web application. 
- Implemented Registration logic and some login logic. 
- Encountered several bugs/issues during this implementation. A significant amount of the work time during this week was spent attempting to solve these problems. Managed to solve several issues
	- Unable to run the web application (urls.py and views.py in SmartStats/roster had typos)
	- Python version did not allow for f string use. Instead used formatted strings implemented in python versions prior to python 3.6 (currently running python 3.5.2)
- Some issues I was not able to solve by the end of this commit due date
	- CSRF token missing or incorrect. Next steps: will inspect the registration/login html pages since it appears that the settings.py, views.py, and urls.py files are correct.

Files edited:
- SmartStats/roster/views.py
- SmartStats/roster/urls.py
- SmartStats/roster/templates/roster/base.html
- SmartStats/SmartStats/settings.py

Week 6 commit:

Work on branches raj

- Continued work on real time tracker logic. To this end changes were made to the views file for the real time tracker logic including player substitution, block, steal, free throw statistics, and timeout requests. Not all changes were tested/committed.
- Real time tracker logi also includes backed development and shot statistics task for this week in the gantt chart. 

Files edited:
-SmartStats/roster/models.py
-SmartStats/basketball_stats/views.py
-SmartStats/basketball_stats/models.py

Week 4 commit:
Work on branches: frontend_raghav

-Began to work on UI logic for the real time tracker. Currently only requests players from the django server and creates a table displaying player name and number. The table will be altered to represent players in court. Substitute player can also be requested from the server. Further work is needed to complete the logic for time stamps and statistics entered in game.
- Reading: Django and bootstrap integration.

Files edited:
-HomeStaticContent/js/realtimetracker.js

Week 3 commit:
Work on branches: raj

-Edited views and urls in directories basketball_stats and roster for future integration with frontend. 
-Began work on views and url for pages to be added (analytics, schedule, homepage); however, not all changes are commited to the branch.
-Began work on backend analytics with pandas and numpy. Not commited due to analytics work not being scheduled at this point on the gantt chart.
- Reading: More pandas/numpy review, django/query integration. 

Files edited (and commited):
-basketball_stats\views.py
-basketball_stats\urls.py
-roster\views.py
-roster\urls.py

Week 2 commit:
Work on branches: raj

-Edited views in directory basketball_stats to reflect Vj's changes under the Smartstats directory.
-Changed html structure under basketball_stats for future use if the branch isn't completely integrated with the smartstats branch.
-Reading: django user authentication and django-bootstrap integration for future use in the upcoming weeks.

Week 1 Commit:
Work on branches: backend_Lucas, raj 

-Edited views in basketball_stats for playbook and anayltics
-Edited models.py in basketball_stats to add statistics models
-Met with VJ and decided I would complete the models for the basketball statistics.
-Created Skeleton models for the database schema. 
-Reading: reviewed Django style, and reviewed pandas for future use.

Files edited:
- basketball_stats\models.py
- basketball_stats\views.py

Notes: Stats model not implemented yet because this is a stretch goal, and will be implemented once MVP is complete
