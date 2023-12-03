# MidiFlex

MidiFlex is a versatile web-based MIDI controller application designed to provide a seamless and personalized experience for controlling MIDI devices. It offers user-friendly interfaces, real-time updates, and secure authentication.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Server](#running-the-server)
  - [Configuring MIDI Output](#configuring-midi-output)
  - [Accessing the Web Interface](#accessing-the-web-interface)
- [User Authentication](#user-authentication)
- [User Profiles](#user-profiles)
- [Usage](#usage)
  - [Interacting with Buttons](#interacting-with-buttons)
  - [Adjusting Sliders](#adjusting-sliders)
- [Logging Out](#logging-out)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Profiles**: Each user has a unique button and fader layout based on predefined profiles.
- **Real-time Updates**: Changes in MIDI controls are instantly reflected on the user interface.
- **Authentication**: Secure login system to access personalized MIDI layouts.
- **Flexible Configuration**: Easily configure MIDI output ports for a customized setup.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/) (3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/MidiFlex.git
Navigate to the project directory:
bash
Copy code
cd MidiFlex/MidiFlex-Server
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Running the Server

Start the Flask app:
bash
Copy code
python app.py
The server will run on http://0.0.0.0:25465. Access the web interface in your browser.
Configuring MIDI Output
Open the app.py file in the MidiFlex Client directory.
Replace 'your_midi_output_port' with the name of your MIDI output port.
python
Copy code
with mido.open_output('your_midi_output_port') as port:
Save the changes.
Accessing the Web Interface
Open your browser and navigate to:
http://localhost:25465 or
http://127.0.0.1:25465.
Log in using the provided user credentials:
Admin Profile: Username: admin, Password: adminpass
User1 Profile: Username: user1, Password: user1pass
User2 Profile: Username: user2, Password: user2pass
Explore the personalized MIDI layouts for each user profile.
User Authentication

The login screen provides access to personalized MIDI layouts based on user profiles.
If already logged in, users will be redirected to their respective profiles.
User Profiles

Each profile includes a set of buttons and sliders with unique MIDI configurations.
Explore the different profiles (Admin, User1, User2) to discover their layouts.
Usage

Interacting with Buttons
Click on buttons to send MIDI commands.
Real-time updates will be reflected on the UI and your MIDI software.
Adjusting Sliders
Move sliders to send MIDI commands with varying velocities.
Observe real-time updates on the UI and your MIDI software.
Logging Out

Click on the "Log Out" button to log out of the application.
Contributing

Contributions are welcome! Please check the CONTRIBUTING.md file for guidelines.

License

This project is licensed under the MIT License - see the LICENSE file for details.

kotlin
Copy code

Feel free to use and customize this README.md for your MidiFlex 
