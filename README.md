# Log Analysis Project

In this project, we used a PostgreSQL database. If you'd like to know a lot more about the kinds of queries that we used in this dialect of SQL, check out the [PostgreSQL documentation](https://www.postgresql.org/docs/). It's a lot of detail, but it spells out all the many things the database can do.

## Prepare the software and data
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

#### The virtual machine
  - This project makes use of the Linux-based virtual machine (VM).
  - If you need to bring the virtual machine back online (with ```vagrant up```), do so now. Then log into it with ```vagrant ssh```.

#### Download the data

Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called ```newsdata.sql```. Put this file into the ```vagrant``` directory, which is shared with your virtual machine.

#### Explore the data 

Once you have the data loaded into your database, connect to your database using ```psql -d news``` and explore the tables using the ```\dt``` and ```\d``` table commands and select statements.

>```\dt``` — display tables — lists the tables that are available in the database.

>``` \d table``` — (replace table with the name of a table) — shows the database schema for that particular table.

### DB includes three Tables:

> The ```authors``` table includes information about the authors of articles.

> The ```articles``` table includes the articles themselves.

>The ```log``` table includes one entry for each time a user has accessed the site.

### What are we reporting ?!
Here are the questions the reporting tool should answer.
* ######  What are the most popular three articles of all time?

* ######  Who are the most popular article authors of all time? 

*  ######   On which days did more than 1% of requests lead to errors?

### Installation
After doing what we note above, *welcome* you are now able to deal with our DB.

Before run our reporting code in your machine you must need to create 3 ```view```s.

```
ArticlesView
requests_no
requests_con
```
#### 1.```ArticlesView```
news=> ```create view ArticlesView AS SELECT COUNT(*) as nom, author FROM articles, log WHERE log.path = '/article/'||articles.slug GROUP BY author ORDER BY nom;```

then you can test this view ``` SELECT * FROM ArticlesView;``` you will get 4 rows as output ..

|nom | author|
|----|-------|
|84557 | 4|
|170098 | 3|
|423457|2|
|507594|1|

#### 2.```requests_no```
this *view* will return back by count of each  *HTTP* requests for each day.
``` CREATE VIEW requests_no AS SELECT to_char(time,'month dd,yyyy') as date, COUNT(*) as nom, status FROM log GROUP BY date, log.status ORDER BY nom; ```

#### 3. ```requests_con```
this view will return back by count of *ALL* requests which sented in each the day.
``` CREATE VIEW requests_con AS SELECT date, SUM(nom) as sum_all FROM requests_no GROUP BY date;```

NOW you are able to run python file :)

``` python report.py ```

## Usage

Now you are able to run this ``` python report.py ```

## Author
Ashraf Amer

## License
Copyright(c) 2017 Ashraf Amer