<!-- ## Since Valentine's Day has passed, the corresponding resources of the cloud server have been released.
## Therefore, the following experience address has expired. -->


<!-- * The online experience URL is: https://studious-dollop-jp97jx6xqjg25qjg-5000.app.github.dev/ -->
### Valentine's Day Card Generator: Documentation & Tutorial

#### Introduction

This project allows users to create custom Valentine's Day greeting cards with various effects and styles. The card's background, text, and font color are customizable.The website also features an audio player that plays a romantic background music track.

---

### Features

* **Background and Font Color Customization**: You can change the card's background color and the text color using a simple interface.
* **Typing Effect**: The greeting text appears in a typing animation, adding a dynamic feel to the card.

* **Music Player**: The page includes an embedded music player that plays a romantic background song. The player is positioned at the top right corner and can be controlled by the user.

---

### Technology Stack

* **Frontend**: HTML, CSS (for styling), JavaScript (for dynamic content).
* **Backend**: Flask (Python web framework) - used for serving the HTML and handling customization data.
* **Audio**: MP3 file used for background music.

---

### How to Set Up the Project

#### Prerequisites:

* Python 3.x installed.
* Flask installed (`pip install Flask flask_sqlalchemy uuid`).
* Basic knowledge of HTML and CSS.

#### 1. Clone the Repository (if available)

```bash
git clone this repo
cd valentines-day-card
```

#### 2. Install Dependencies

Make sure you have Flask installed, or install it by running:

```bash
pip install Flask
```

#### 3. Project Directory Structure

Ensure your project has the following structure:

```
valentines-day-card/
│
├── static/
│   ├── css/
│   │   └── styles.css         # CSS file for styling
│   ├── music/
│   │   └── 3385112214.mp3     # Background music file
│
├── templates/
│   └── index.html             # HTML file for rendering the card
│
└── app.py                     # Flask app to serve the website
```

#### 4. Flask App Setup

In `app.py`, set up your Flask application:


#### 5. Customization Options

* **background**: Color code for the background of the card.
* **font\_color**: Font color for the text.
* **text**: The text that will be displayed on the card (e.g., "Happy Valentine's Day!").



