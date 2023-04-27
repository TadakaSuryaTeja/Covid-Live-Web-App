<h1> Covid-Live-Web-App </h1> 
This is a web application that provides live updates on Covid-19 cases around the world. It is built using Python and Django.

# Installation

Clone the repository:

```python
git clone https://github.com/yourusername/Covid-Live-Web-App.git
```

Create a virtual environment:
```python
python3 -m venv env
```

Activate the virtual environment:

```python
source env/bin/activate
```

Install the required packages:

```python
pip install -r requirements.txt
```

Run the Django server:
```python
python manage.py runserver
```

# Usage
Once the server is running, you can access the web application by navigating to http://localhost:8000/ in your web browser.

The application displays a world map with circles representing the number of confirmed Covid-19 cases in each country. You can click on a circle to view more information about that country, including the number of confirmed cases, recovered cases, and deaths.

The application also provides a search bar where you can enter the name of a country to view its Covid-19 statistics.

# Data source
The Covid-19 data used in this application is sourced from the COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University.
