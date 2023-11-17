# Seoul Cultural Events App
![스크린샷 2023-11-17 오후 1 30 25](https://github.com/dkqpeo/gpt-project/assets/106148197/b9384d52-0bbb-4ded-bc85-af66aee4e92d)

## Overview

The Seoul Cultural Events App is a Flask-based web application that allows users to explore information about cultural events in Seoul. The application utilizes the Seoul Metropolitan Government's cultural events API to fetch and display event details.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python (version 3.6 or higher)
- Flask library (`pip install Flask`)
- Requests library (`pip install requests`)

### API Key

To access the Seoul cultural events API, you need an API key. Follow these steps to obtain one:

1. Visit [Seoul Open Data Plaza](http://data.seoul.go.kr/) and create an account.
2. Navigate to the [cultural events API page](http://data.seoul.go.kr/dataList/OA-15486/S/1/datasetView.do) and request an API key.
3. Insert your API key in the `API_KEY` variable in `app.py`.

### Running the Application

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

- Visit the homepage to see a list of cultural events.
- Click on the "Filter by District" link to view events specific to a district.

## API Information

The application uses the Seoul Metropolitan Government's cultural events API. API documentation can be found [here](http://data.seoul.go.kr/dataList/OA-15486/S/1/datasetView.do).

**Note:** Insert your API key in `app.py` to access the API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data provided by the Seoul Metropolitan Government.
