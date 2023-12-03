# MidiFlex Server

MidiFlex Server is a Flask-based web application that allows users to control MIDI devices through a web interface. It provides a flexible environment for users with different profiles, each having their own set of buttons and sliders.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Profiles](#profiles)
- [License](#license)

## Introduction

MidiFlex Server is designed to facilitate MIDI control in a collaborative environment. Users can log in, and based on their profile, they get access to a customized set of buttons and sliders. This server works in conjunction with the MidiFlex Client, which processes and sends MIDI commands to the specified devices.

## Features

- **(In Progress) User Authentication**: Secure user authentication system that encrypts passwords (SHA-256) and stores them externally.
- **Profile-Based Control**: Each user has a unique profile defining their set of buttons and sliders.
- **Real-time Updates**: Utilizes Flask-SocketIO to provide real-time updates to the web interface when MIDI commands are triggered.
- **Docker**: Simple Hosting with Docker.
- **Logout Functionality**: Allows users to log out securely with a simple logout button.

## Requirements

- python 3.8.10
- pip
- git
- docker (if it should run with docker)
- one or more PCs that have the MidiFlex Client running

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/MidiFlex-Server.git
    ```

2. Install dependencies:

    ```bash
    cd MidiFlex-Server
    pip install -r requirements.txt
    ```

3. Run the server:

    ```bash
    python app.py
    ```

## Usage

1. Start the Server, the Start the MidiFlex Clients.
2. Access the web interface at `http://your-server-ip:25465`.
3. Log in with your credentials.
4. Explore and interact with the personalized MIDI layout based on your user profile.

## Profiles

Profiles are currently stored in the server code (`app.py`). Each profile consists of buttons and sliders, each having a unique label, note, and velocity.

Example Profile:

```python
'admin': {
    'buttons': [
        {'label': "Admin Button 1", 'note': 60, 'velocity': 127},
        # ... add more buttons
    ],
    'sliders': [
        {'label': "Admin Slider 1", 'id': "admin_slider1"},
        # ... add more sliders
    ],
},
```


## License

MidiFlex Server is licensed under the MIT License.
