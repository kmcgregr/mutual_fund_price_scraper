FROM python:3
RUN python -m pip install --upgrade pip
RUN pip install requests
RUN pip install pandas
RUN pip install numpy
RUN pip install openpyxl
RUN pip install schedule
RUN pip install beautifulsoup4

WORKDIR /usr/src/app

COPY . /usr/src/app

CMD ["python", "/usr/src/app/mutual_fund_price_scrapper.py"]