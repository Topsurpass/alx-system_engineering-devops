# Incident report for Airbnb clone project
## Issue Summary
On August 11th, 2023 from 9:00 pM to 10:00 PM WAT, MY AIRBNB CLONE website was down whenever i try to access the API web service. The service failed 100% of time which if deployed like that, 100% of users will experience a 500 internal server error, caused by not deleting other classes mapped with the particular class i intend deleting.

Timeline
9:00 PM Server down
9:10 PM Error logs checked
9:20 PM File causing error traced
9:45 PM API endpoint reviwed and other classes mapped with it was properly reviewed
10:00 PM 100% restored and API web service for the DELETE method restored
## Root Cause and Resolution
After the whole API endpoint was designed and url created, some edge cases were not covered which should have specified the error before deploying. After the server was down, the error message received from the server was thoroghly checked and the file causing this error was gotten. It was noticed that while using the method DELETE, the classes mapped to the database using SQLAlchemy contains some classes that were in relation with themselves using the backref class relationship of SQLAlchemy. So, in an attempt to delete some of these classes, the other classes mapped to them were left out which now cause the error. The error was fixed by writing code that deletes not just the class but broke or dissociates its relationships with other classes.


## Corrective and Preventative Measures
This problem can be corrected and prevented by writing test cases that takes care of all test cases before deploying.
