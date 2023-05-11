# Oireachtas Events

## Project overview

Project  for Code Institute Full-stack development program: Full-Stack Toolkit.

View the [Live site](https://oir-events.herokuapp.com/)

### Project goals

The Houses of the Oireachtas regularly hosts events and exhibitions, and also offers the public an opportunity to visit Leinster House for a tour of the historic building. The Oireachtas Events site seeks to provide a single booking system for tickets to all Oireachtas events and tours.  

The site will offer users information on all Oireachtas events, exhibitions and open tours, an ability to create an account to book, reschedule and cancel tickets, and important visit information. The site will allow the site owner to manage ticketing for all events through one site.  

## User Experience Design

### Target Audience 

* Members of the public who would like more information on Oireachtas events 
* Members of the public who would like to attend Oireachtas events 
* Members of the public who would like to delete booking for Oireachtas events 

### User Requirements and Expectations 

* A visually appealing, accessible and easy to use site 
* An intuitive navigation with logical workflows for event booking management 
* An ability to view information on events and manage bookings

### Agile Planning

This project was developed using agile methodologies by delivering features in sprints. There were 3 sprints in total, the work was carried out over four weeks.

Initially user stories were developed, and a full set of acceptance criteria was created in order to define the functionality of the required feature, these user stories were assigned to epics (milstones), prioritised under the labels, ‘Must have’, ‘Should have’, and ‘Could have’. Then they were assigned to sprints and story pointed, according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

In GitHub projects, a Kanban board was used to track the progress of the project, the workflow started with To do then In Progress, Done and finally Closed, were the item was marked as closed. 

* View the [Kanban board](https://github.com/users/michelleconville/projects/5)

### User stories - broken down by Epic

EPIC 1 - Initial Setup

* As a developer, I need to set up the project so that it is ready for implementing the core features
* As a developer, I need to create static resources so that images and CSS work on the website
* As a developer, I need to create the navbar so that users can navigate the website
* As a developer I need to create the footer with social media links and contact information so this information can be found on any page on the website
* As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

EPIC 2 - Authentication Epic 

* As a developer, I need to implement allauth so that users can sign up and have access to the website’s features
* As a site owner, I would like the allauth pages customized to that they fit in with the sites styling 
* As a site owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used. 

EPIC 3 – Events 

* As a staff member, I want to create events so I can allow bookings
* As a staff member, I want to be able to delete events if they are no longer going ahead
* As a staff member, I want to be able to edit events 
* As a site user, I want to be able to find information on all Oireachtas tours so that I can decide if I want to book tickets 

Epic 4 – Bookings

* As a site user, I want to be able to book tickets for all available events so that I can attend
* As a site user, I want to be able to reschedule bookings for events so that I can attend
* As a site user, I want to be able to cancel bookings for events so that I can confirm I am no longer available
* As a site user, I want to receive a conformation for event bookings so that I have a record of the bookings I made 
* As a staff member, I want to view details of booking so I can manage the attendance of booked parties

Epic 5 Additional pages

* As a developer, I need to implement a 404-error page to alert users when they have accessed a page that doesn't exist
* As a developer, I need to implement a 500-error page to alert users when an internal server error occurs
* As a developer, I need to implement a 403-error page to redirect unauthorised users to, so that I can secure my views
* As a site owner, I would like a home page so that users can view information on my website
* As a site user, I want to read frequently asked questions so that I can find information on events
* As a site user, I want to access information on how to find Leinster House, so I arrive at the correct entrance

EPIC 6 - Deployment Epic

* As a developer, I need to deploy the project to heroku so that it is live for users

EPIC 7 – Documentation

* Complete readme documentation 

## The structure

### Features

#### Navigation Menu

*       USER STORY: As a developer, I need to create the navbar so that users can navigate the website

The initial navigation menu contain links to the Home, Events, Contact, Register, Login pages. The navigation menu is displayed on all pages and changes into a hamburger menu on smaller devices. This will allow users to view the site from any device.

The navigation changes depending on whether the user is an end user or a staff user. 

If an end user chooses to register and/or login, the following navigation options are available:

* Home 
* Events -> detailed event page
* Bookings (Drop Down):
    * Manage Bookings (user booking only)
    * New Booking
* Contact
* Logout

If a staff user chooses to register and/or login, the following navigation options are available:

* Home 
* Events -> detailed event page
* Add (to add an event)
* Bookings (Drop Down):
    * Manage Bookings (All booking)
    * New Booking
* Contact
* Logout

#### Footer 

*       USER STORY: As a developer I need to create the footer with social media links and contact information so this information can be found on any page on the website

A footer has been added to the bottom of the site, this contains social media link to Twitter, Facebook, YouTube, and LinkedIn so that users can follow the Oireachtas on our social media channels, to both here about upcoming events and the work of the Houses of the Oireachtas if that interests them. 

These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.

#### Homepage

*       USER STORY: As a site owner, I would like a home page so that users can view information on my website

The home page contains a carrousel of images taken in Leinster House. These images will have a call-to-action button on them, to either book an event or view all events. These buttons give the user a quick way to get to the events page or the booking page. The carrousel images can be replaced at any time using the backend admin panel.

The second part of the home page is visitor information, this information is displayed in an accordion module. This will give users information on, where to find Leinster House and what gate to use, via both a text description and a map, the items that them will need to bring with them and how to book tickets if it is there first visit to the website. 

#### Events pages

*       USER STORY: As a site user, I want to be able to find information on all Oireachtas tours so that I can decide if I want to book tickets

**Events pages (List view of all events)**

The events page contains a list of upcoming events that taking place in Leinster House, the events are displayed on cards, have an image, the name of the event and the short description, event card is clickable and will take the user to the detailed event page.

If there are no events currently scheduled to take place a message will display for the user to notify them of that. 

**Event page (Detailed event page)**

Each event has its own page, that contains three sections, the first has an image relating to the event, the event title, the date, the tour time, a short description and a book now button.  The second section is About this event, this gives more information about the upcoming event and the third is the What else to know section, this redirection the user to the visitor information.  

The first and second sections are unique to the event itself, this information will help the user decide if they would like to attend the event and give them the option to book a ticket. The third section is an quick way for the user to find the visitor information. 

**Create event page**

*       USER STORY - As a staff member, I want to create events so I can allow bookings

A create event page was implemented to allow staff users to create new events via the UI without having to use the backend admin panel. For staff and admin users only, a button “Add” will display in the navigation menu.

This will allow staff the ability to create an event and publish it to the website from a single page, this will create the Event page and will display an event card on the Events page. 

**Edit event page**

*       USER STORY - As a staff member, I want to be able to edit events

On the event page, an edit button displays for staff and admin users only, this allows staff to easily edit any of the details or make the page inactive if they no longer want to display to the website, this will not delete the event. 

**Delete event page**

*       USER STORY - As a staff member, I want to be able to delete events if they are no longer going ahead or are over

On the event page, a delete button displays for staff and admin users only, this allows staff to delete an event, once the button is selected, they will be taken to a confirmation page to confirm that they do want to delete the event. 

