Agricultural Management Portal - SIH Project:

This web application connects farmers with agricultural officers to manage crop reporting and track data. 
It includes built-in translation and text-to-speech features to ensure information is accessible in regional languages.

Project Breakdown

⚬	Role-based access provides separate dashboard views tailored specifically for farmers and officers.

⚬	The main application logic runs through app.py, while data.py manages the database and information processing.

⚬	Accessibility and localization are handled by tts.py (for audio) and translations.py (for multi-language support).

⚬	All frontend HTML views, including login, registration, crop tracking, and report details, are stored in the templates directory.

⚬	Supporting files like CSS and generated audio live in the static directory.
