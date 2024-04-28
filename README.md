# Submission Info

Author: Sara Jo Jeiter-Johnson

NetID: sjeiterj

Email: sjeiterj@u.rochester.edu

# Description

This website is meant to host a database of iconic quotes from queer media figures as well as everyday queer people. 

Anyone can submit a quote. Admins then can either approve or reject the submission. If approved, the submission will be put into the Iconic Queer Quotes Database for everyone to see. There is a random quote generator, which randomly selects and displays a quote from the database. There is also the "Iconic Queer Quote of the Day" (determined by bucket-hashing) which is displayed on the home page of the website.

# Notes
- __All Requirements have been Met__
- The 2 Additional Rquirements I did were __User Authentication__ and __Additional Database Interations__
- Code was based heavily on Professor's demos as we were supposed to follow his project structure closely
- The Pride Flag image is from Wikipedia [1], cited below

# Guide of how to see and use all features
1. Start at the home page
2. Click 'Submit a Quote!' on the header
3. Fill out the form however you like and submit. In order for the submission to be entered into the database, an admin must approve of it first, so go to the next step to create an admin account

4. Click 'Admin Sign Up' at the very top of the header
5. To prevent any random person from creating an admin account, we use an 'Admin Key' as a security measure. The Admin Key is determined by the .env file the server runs with. If you're using the .env file I provided, the Admin Key is `someadminkey`. Enter the Admin Key into the Admin Key section and then fill out the rest of the form as normal. It will say if your account was successfully created after you submit
6. Click 'Admin Login' at the very top of the header
7. Enter the username and password for the admin account you just created. It will say if your account was successfully logged in after you submit
8. The header will now have new options including 'Edit Database', 'Review Submissions', and 'Log out'

9. Now let's add your submission to the database. Click on 'Review Submissions'
10. Your submission should be visible with 'Approve' and 'Reject' buttons next to it. Click 'Approve'
11. Click 'See Quote Database'
12. Now you can see your submission in our database!

13. If you go to the home page, your quote may appear as the "Iconic Queer Quote of the Day"
14. If you click on 'Random Quote' your quote may also be randomly generated there

15. If you want to delete you quote, click on 'Edit Database' (only accessible is logged in as an admin)
16. Click the 'Delete' button next to the quote you want to delete

17. Log out, and now you've seen all the website features!

# Citations
1. By Guanaco and subsequent editors - SVG source (version of 17:56, 30 Sep 2011), Public Domain, https://commons.wikimedia.org/w/index.php?curid=479191