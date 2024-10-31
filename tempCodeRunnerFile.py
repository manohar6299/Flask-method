# from flask import Flask, request, render_template, redirect, session, url_for

# from flask_sqlalchemy import SQLAlchemy
# import bcrypt
# from itsdangerous import URLSafeTimedSerializer
# from flask_mail import Mail, Message
# from functools import wraps

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'manohar6299254553@gmail.com'
# app.config['MAIL_PASSWORD'] = 'jyyzfpexrfrpcnmm'
# app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'
# db = SQLAlchemy(app)
# mail = Mail(app)
# app.secret_key = 'man_mn'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     message = db.Column(db.String(50))
#     def __init__(self, username, email, password,message):
#         self.username = username
        
#         self.email = email
#         self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#         self.message = message
        
#     def check_password(self, password):
#         return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# with app.app_context():
#     db.create_all()

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'email' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function



# @app.route('/')
# def get_start():
#     return render_template('get_start.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         user = User.query.filter_by(email=email).first()

#         if user and user.check_password(password):
#             session['email'] = user.email
#             return redirect(url_for('home'))

#         return render_template('login.html', error='Invalid credentials. Please try again.')

#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         existing_user = User.query.filter_by(email=email).first()
#         if existing_user:
#             return render_template('register.html', error='Email already registered.')

#         new_user = User(username=username, email=email, password=password)
#         db.session.add(new_user)
#         db.session.commit()

#         return redirect(url_for('login'))

#     return render_template('register.html')

# @app.route('/navbar')
# @login_required
# def navbar():
#     return render_template('navbar.html')

# @app.route('/home')
# @login_required
# def home():
#     return render_template('home.html')

# @app.route('/about')
# @login_required
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# @login_required
# def contact():
#     return render_template('contact.html')

# @app.route('/services')
# @login_required
# def services():
#     return render_template('services.html')

# @app.route('/courses')
# @login_required
# def courses():
#     return render_template('courses.html')

# @app.route('/reset-password', methods=['GET', 'POST'])
# def reset_password():
#     if request.method == 'POST':
#         email = request.form['email']
#         user = User.query.filter_by(email=email).first()

#         if user:
#             s = URLSafeTimedSerializer(app.secret_key)
#             token = s.dumps(email, salt='email-reset-salt')
#             reset_link = url_for('reset_with_token', token=token, _external=True)

#             # Send email
#             msg = Message('Password Reset Request',
#                           recipients=[email])
#             msg.body = f'Please click the link to reset your password: {reset_link}'
#             mail.send(msg)

#             return render_template('reset_password.html', message='Check your email for a password reset link.')
#         else:
#             return render_template('reset_password.html', error='Email not found. Please register or try a different email.')

#     return render_template('reset_password.html')

# @app.route('/reset/<token>', methods=['GET', 'POST'])
# def reset_with_token(token):
#     s = URLSafeTimedSerializer(app.secret_key)
#     try:
#         email = s.loads(token, salt='email-reset-salt', max_age=3600)
#     except:
#         return 'The reset link is invalid or has expired.'

#     if request.method == 'POST':
#         new_password = request.form['password']
#         confirm_password = request.form['confirm-password']

#         if new_password != confirm_password:
#             return render_template('reset_with_token.html', token=token, error='Passwords do not match.')

#         user = User.query.filter_by(email=email).first()
#         user.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#         db.session.commit()
#         return redirect('/login')

#     return render_template('reset_with_token.html', token=token)


# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('get_start'))

# if __name__ == '__main__':
#     app.run(debug=True)
