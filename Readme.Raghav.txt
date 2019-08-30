Week10: Had to deviate from gantt chart as we are in the integration and testing stage of the project. Had to change my portion of the application
to be able to integrate it with the backend models. Implemented more javascript to send json data via ajax request to django views where
data can be unpacked and stored in the db using the appropriate models. Files are in home/static/js and home/templates/ called coach.js and 
coachhome.html on raghav_backend branch

Week9: Had to deviate from the gantt chart for integration purposes this week. Instead I added to the realtime tracker page including adding
functional buttons which result in calls to urls linked to django backend views. Added logic to coach.js which included making those calls
and adding more logic for the page. Files are coachhome.html coach.js and court.css located on raghav_backend

Week 8: Added UI framework for plays page which includes a basketball court and play list. Added the create team page as well which allows
users to create a team and enter information such as team name,team size etc. All this implementation is done using bootstrap and html.
Files are called creatteam.html,plays.html and are located in branch frontend_raghav under HomeStaticContent

Week7: Back to gantt chart. Implemented D3 court logic. There are some bugs with implementation but will fix it. Implemented court with 
cross sections using d3 framework. File is located on frontend_raghav under HomeStaticContent called dj

Week6: Had to deviate from gantt chart this week due to additional HTML framework requirement for the roster page. Implemented Roster html
page and UI logic using Javascript. Roster page shows players and form to add players to the roster.The files are located in HomeStaticContent/js
and HomeStaticContent as roster.html and roster.js respectively. Located on frontend_raghav

Week5: Implemented Unit Test Framework for Javascript logic for all UI pages. Javascript unit tests use the mocha library to run unit tests
Test Cases are basic for now but will be expanded when more functionalty is added to the UI logic. The unit tests are run in order
File is called unit_tests_framework.js and is located on frontend_raghav branch under js folder

Week4: Implemented the Analytics UI logic which generates ansychronus requests to the django server to pull up 
advance analytics data for each game played by the team. The table is dynamically generated based on values which 
are retrieved from the server. The UI logic supports updates in real time for advance analytics during the game.
File is located on frontend_raghav in HomeStaticContent/js. Please ignore the commit labeled second commit. Commit is called fourth commit  
On gantt chart it said update home ui. But that is mostly completed in first commit. Instead it should say update analytics UI

Week3: Implemented the Analytics wireframe using Bootstrap. Used the built in Bootstrap classes with table styling 
to implement a hardcoded table with values which will be dynamically served in the Ui logic step for the analytics
Added an area for the future court using d3- Located on frontend_raghav- under analytics.html

Week2: Implemented the Coach home stat tracker page using Bootstrap. Used the built in grid classes 
for bootstrap and made a player selection framework as well buttons for the player stats inputs.Made an area 
below the buttons where the visualized court will go using the dj framework.The added html file is under HomeStaticFiles/coachhome.html
which is the html code for this weeks commit.Located on frontend_raghav


Week 1: Implemented Home Page framework using Bootstrap. Used bootstraps 
built in classes to make dynamic home page with slide show of pictures describing function of each
component of the application. Made dummy links which will eventually link to login pages. Will also add
some additional design changes in following week. Files: HomeStaticContent/home.html -- html chasis for home page.
HomeStaticContent/petino.jpg -- picture of coach for page. HomeStaticContent/lamelp.jpg -- Picture player. HomeStaticContent/scout.jpg
--Picture of Scout for Home page. Branch this is located on is frontend_raghav
