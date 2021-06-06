# eduHub
## An Educational Hub for Students

#### Specification
1. Authentication
2. Contact Us
3. Profile/Dashboard
4. Enroll
5. View Course Material
6. Comment
7. Video

- `Main Directory`
    - `eduHub` - Main Django App
        - `urls.py` - All the urls of my application
        - `views.py` - All the backend fuctions and calculation of my application
        - `models.py` - All the models used in my application (Contact, User, Post, Course, Comment)
        - `admin.py` - Models to be shown on the admin page
        - `static`
            - `comment.css` - All the comment box styling
        - `templates`
            - `admin`
                - `base_site` - Added a little css to the admin page
            - `layout.html` - The basic layout of all the webpages
            - `index.html` - This is the first page, displays all the  courses in the website
            - `contact.html` - Contact form
            - `login.html` - Login page
            - `register.html` - Registration page
            -  `CourseIndexPage.html` - Shows all the chapters in the course
            - `ViewChapter.html` - The Chapter Content (Written, Video) and Comment box.
            - `profile.html` - Profile Page
            - `search.html` - Shows the search results

### Justification

Why is my project differrent from the previous projects ?

- Added css in the admin page
- Video Upload and Playing Video
- Use of custom message tags