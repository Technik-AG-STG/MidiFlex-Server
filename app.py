from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_login import logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import eventlet

# Exclude dns module from eventlet patching
eventlet.monkey_patch(all=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Use eventlet to run the Socket.IO server
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# For simplicity, in-memory user storage with profiles
users = {
    'admin': {'password': 'adminpass', 'profile': 'admin'},
    'user1': {'password': 'user1pass', 'profile': 'user1'},
    'user2': {'password': 'user2pass', 'profile': 'user2'},
}

# Define profiles with buttons and sliders
profiles = {
    'admin': {
        'buttons': [
            {'label': "Admin Button 1", 'note': 60, 'velocity': 127},
            {'label': "Admin Button 2", 'note': 62, 'velocity': 127},
        ],
        'sliders': [
            {'label': "Admin Slider 1", 'id': "admin_slider1"},
            {'label': "Admin Slider 2", 'id': "admin_slider2"},
        ],
    },
    'user1': {
        'buttons': [
            {'label': "User1 Button 1", 'note': 64, 'velocity': 127},
            {'label': "User1 Button 2", 'note': 65, 'velocity': 127},
        ],
        'sliders': [
            {'label': "User1 Slider 1", 'id': "user1_slider1"},
            {'label': "User1 Slider 2", 'id': "user1_slider2"},
        ],
    },
    'user2': {
        'buttons': [
            {'label': "User2 Button 1", 'note': 68, 'velocity': 127},
            {'label': "User2 Button 2", 'note': 69, 'velocity': 127},
        ],
        'sliders': [
            {'label': "User2 Slider 1", 'id': "user2_slider1"},
            {'label': "User2 Slider 2", 'id': "user2_slider2"},
        ],
    },
}

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        user.profile = users[user_id]['profile']
        return user
    return None

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')

class Button:
    def __init__(self, label, note, velocity):
        self.label = label
        self.note = note
        self.velocity = velocity

class Slider:
    def __init__(self, label, id):
        self.label = label
        self.id = id

buttons = []
sliders = []

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        user.id = form.username.data
        user.profile = users.get(form.username.data, {}).get('profile', '')
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html', form=form, message="Invalid credentials")

@app.route('/')
@login_required
def index():
    user_profile = profiles[current_user.profile]
    user_buttons = [Button(button['label'], button['note'], button['velocity']) for button in user_profile['buttons']]
    user_sliders = [Slider(slider['label'], slider['id']) for slider in user_profile['sliders']]
    return render_template('index.html', buttons=user_buttons, sliders=user_sliders)

def send_midi_signal(type, data):
    # Simplified function to send MIDI signal to the client
    socketio.emit('midi_signal', {'type': type, 'data': data})

@socketio.on('connect')
def handle_connect():
    emit('login_response', {'data': 'Connected'})

@socketio.on('login')
def handle_login(data):
    form = LoginForm(data=request.json)
    if form.validate():
        user = User()
        user.id = form.username.data
        user.profile = users[form.username.data]['profile']
        login_user(user)
        emit('login_response', {'data': 'Login successful'})
    else:
        emit('login_response', {'data': 'Login failed'})

@socketio.on('button_click')
@login_required
def handle_button_click(data):
    if current_user.id == 'admin':
        print(f"Button Clicked by Admin: {data}")
        # Send MIDI command for admin
        send_midi_signal('button_click', data)
    else:
        print(f"Button Clicked by User: {data}")
        # Send MIDI command for regular users
        send_midi_signal('button_click', data)

@socketio.on('fader_change')
@login_required
def handle_fader_change(data):
    print(f"Fader Changed: {data}")
    # Send MIDI command for fader change
    send_midi_signal('fader_change', data)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='localhost', port=25550)
