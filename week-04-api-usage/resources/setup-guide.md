# Setup Guide for Week 4

To complete this week's assignment, you'll need to install the official Python library for your chosen LLM provider and get an API key.

## Step 1: Get an API Key

You need an API key to authenticate your requests.

### For OpenAI:

1.  Go to the OpenAI Platform.
2.  Sign up or log in.
3.  Navigate to the API Keys section in your account settings.
4.  Create a new secret key and copy it immediately. You won't be able to see it again.

### For Google AI (Gemini):

1.  Go to Google AI Studio.
2.  Sign in with your Google account.
3.  Click on **Get API key** and create a new key.

**IMPORTANT:** Treat your API key like a password. 🔑 Do not share it or commit it to a public GitHub repository.

-----

## Step 2: Store Your API Key Securely

The best practice is to store your API key as an environment variable.

### On macOS/Linux:

Open your terminal and run the relevant command:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

```bash
export GOOGLE_API_KEY='your_api_key_here'
```

To make the variable permanent, add the export line to your shell profile file (e.g., `~/.zshrc` or `~/.bash_profile`).

### On Windows:

1.  Search for "Edit the system environment variables" in the Start Menu and open it.
2.  Click the **Environment Variables...** button.
3.  In the "User variables" section, click **New...** and add your key.
      - Variable name: `OPENAI_API_KEY` or `GOOGLE_API_KEY`
      - Variable value: `your_api_key_here`

-----

## Step 3: Install Python Libraries

Open your terminal or command prompt and install the necessary library using `pip`.

### For OpenAI:

```bash
pip install openai
```

### For Google Gemini:

```bash
pip install google-generativeai
```
