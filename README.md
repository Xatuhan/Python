Banking Database System 

	This is a terminal-based banking system project written in Python. It allows users to register, log in, and perform basic banking operations. All user data is saved in a local SQLite database.

What the program does:
	When the program starts, you can choose to log in either as a user or as an admin.

For users:
	You can create an account by entering your name, ID number (TC), age (must be over 18), phone number, email, and password.

	After successful registration, your information is stored in a SQLite database (banka_proje.db), and a random 24-digit IBAN is created for you.

Then, you can:

	Deposit or withdraw money

	Transfer money to another IBAN (with a small transaction fee)

	Apply for a loan (eligibility is checked based on income and loan duration)

	Send messages or complaints to the admin

	View your past transactions (also saved into a text file)

For admins:
	You can log in with default credentials (ADMIN / ADMIN)

Admins can:

	Read messages from users

	View users' transaction history

	See the list of registered users

About the Code:
	The system uses two main classes:

	Kullanici (User): Stores personal and account details like name, balance, and IBAN.

	Yonetici (Admin): Handles admin login and basic management features.

	Transactions are also written to a .txt file for each user, based on their ID.

	The database table is created automatically when the program runs.

No extra setup is required. Just run the Python file, and the database and tables will be created if they don't already exist.
