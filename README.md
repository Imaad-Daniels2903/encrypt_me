# encrypt_me

A simple command-line tool that encrypts text using a custom algorithm built around the digits of pi.

Each character is converted to binary, combined with a numeric key, and mixed with digits of pi (run through a Fibonacci lookup) to produce the encrypted output.

> **Note:** This is a hobby/learning project. The algorithm is custom and has not been reviewed by cryptographers, so don't use it to protect anything sensitive.

## Quick start

### Option 1: Install with pipx (recommended)

[pipx](https://pipx.pypa.io) installs command-line tools in their own isolated environment, so they don't interfere with your other Python packages.

**1. Install pipx (skip this if you already have it)**

macOS:

```bash
brew install pipx
pipx ensurepath
```

Linux (Debian/Ubuntu):

```bash
sudo apt install pipx
pipx ensurepath
```

Linux (other) or any system with Python 3.9+:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Windows:

```powershell
py -m pip install --user pipx
py -m pipx ensurepath
```

After running `ensurepath`, **close and reopen your terminal** so the change takes effect. You can check it worked with `pipx --version`.

**2. Install encrypt_me**

```bash
pipx install git+https://github.com/YOUR-USERNAME/encrypt_me.git
```

**3. Run it**

```bash
encryptme "hello world"
```

To upgrade later, or to remove it:

```bash
pipx upgrade encrypt_me
pipx uninstall encrypt_me
```

### Option 2: Clone the repo and install with pip

Requires Python 3.9 or newer.

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/encrypt_me.git
cd encrypt_me
```

**2. (Recommended) Create a virtual environment**

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

**3. Install the package**

```bash
pip install .
```

If you plan to edit the code, use an editable install instead so your changes take effect immediately:

```bash
pip install -e .
```

**4. Run it**

```bash
encryptme "hello world"
```

If you installed into a virtual environment, remember to activate it first each time you open a new terminal.

## Usage

Pass the text as an argument:

```bash
encryptme "text to encrypt"
```

Or run it with no arguments and it will prompt you:

```bash
encryptme
enter text: text to encrypt
```

The encrypted result is printed to the terminal. It may contain unusual or non-printable characters, so redirect it to a file if you want to keep it exactly as is:

```bash
encryptme "text to encrypt" > output.txt
```

## How pi digits are loaded

The first 10,000 digits of pi ship with the package (`src/encrypt_me/pi.json`), which is enough to encrypt roughly 1,250 characters of text with no internet connection.

For longer input, the tool fetches additional digits from the [pi.delivery](https://pi.delivery) API and caches them in `~/.cache/encrypt_me/pi.json`, so each extra digit is only downloaded once. This requires an internet connection the first time.

## Project structure

```
encrypt_me/
├── src/
│   └── encrypt_me/
│       ├── __init__.py
│       ├── encryption.py   # the encryption algorithm
│       ├── main.py         # command-line entry point
│       ├── pi.py           # loads pi digits (bundled file + API fallback)
│       └── pi.json         # first 10,000 digits of pi
├── pyproject.toml
├── requirements.txt
└── README.md
```