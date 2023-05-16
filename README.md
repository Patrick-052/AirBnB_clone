# 0x00. AirBnB clone - The console

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Phase One](#phase-one)
  * [The Command Interpreter](#the-command-interpreter)
    - [Usage](#usage)
4. [Project Structure](#project-structure)
6. [Contributors](#contributors)
7. [License](#license)

## Introduction
The goal of this project is to deploy on a server a simple copy of the [AirBnB website](https://www.airbnb.com/).

Features will be implemented in phases, and the final application will comprise:
  * A command interpreter to manipulate data without a visual interface
  * A website (front-end)
  * A database or file that stores objects
  * An API for communication between the front end and the database

---
## Phase One
This phase involved building the command interpreter. Its description follows.

---
### The Command Interpreter
The command interpreter provides a command-line interface for managing project
components. Its functionality includes:
  * Creating object instances
  * Updating object instances
  * Listing object instances
  * Destroying object instances

---
#### Usage
The interpreter works as follows:
  * In interactive mode:

	```bash
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$
	```

  * In non-interactive mode:

	```bash
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
	```

---
## Project Structure
Organisation is as follows:

	```
	.
	├── [AUTHORS](AUTHORS)
	├── [LICENSE](LICENSE)
	├── [README.md](README.md)
	├── [console.py](console.py)
	├── [hack](hack)
	│   └── [generate-authors.sh](hack/generate-authors.sh)
	├── [models](models)
	│   ├── [__init__.py](models/__init__.py)
	│   ├── [amenity.py](models/amenity.py)
	│   ├── [base_model.py](models/base_model.py)
	│   ├── [city.py](models/city.py)
	│   ├── [engine](models/engine)
	│   │   ├── [__init__.py](models/engine/__init__.py)
	│   │   └── [file_storage.py](models/engine/file_storage.py)
	│   ├── [place.py](models/place.py)
	│   ├── [review.py](models/review.py)
	│   ├── [state.py](models/state.py)
	│   └── [user.py](models/user.py)
	└── tests
		├── __init__.py
		└── test_models
			├── __init__.py
			├── test_amenity.py
			├── test_base_model.py
			├── test_city.py
			├── test_engine
			│   ├── __init__.py
			│   └── test_file_storage.py
			├── test_place.py
			├── test_review.py
			├── test_state.py
			└── test_user.py
	```

---
## Contributors
This project was written by [Patrick-052](https://github.com/Patrick-052) and [Kemboiray](https://github.com/Kemboiray).

---
## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more information.
