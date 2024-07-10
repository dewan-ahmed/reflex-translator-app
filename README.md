# Reflex Translator App

This project demonstrates a basic translator app using the Reflex framework, deployed in a Docker container.

## Features

- Translate text into different languages using Google Translate API.
- View past translations with original text, translated text, destination language, and timestamp.
- Responsive web interface with interactive components.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher installed locally.
- Docker installed on your local machine or deployment environment.

## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dewan-ahmed/reflex-translator-app.git
   ```
2. Navigate to the project directory
   ```sh
   cd reflex-translator-app
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Configure `rxconfig.py` with your app details (e.g., `app_name`, `api_url`).
2. Build the Docker image
   ```sh
   docker build -t reflex-translator-app:latest .
   ```
3. Run the Docker container
   ```sh
   docker run -d -p 3000:3000 -p 8000:8000 --name reflex-translator-app reflex-translator-app:latest
   ```
4. Access the app in your web browser at `http://localhost:3000`

## Configuration

- Modify `rxconfig.py` to set your app configuration, including `app_name`, `api_url`, etc.
- Adjust `requirements.txt` to include any additional Python dependencies required.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Not yet added.
