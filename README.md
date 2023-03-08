# ISSUE
 - xls no more support so have to change xlsx and have to check pd.read_excel

# Kaggle API 설치
``` pip install kaggle --upgrade```
  
# Using kaggle data
1. [Simple Gender Classification](https://www.kaggle.com/datasets/muhammadtalharasool/simple-gender-classification)
2. [Goodreads All time Greatest Books 8k Data](https://www.kaggle.com/datasets/azim069/goodreads-all-time-greatest-books-8k-data)
3. [Iris Dataset (JSON Version)](https://www.kaggle.com/datasets/rtatman/iris-dataset-json-version)
4. [Laptop Selection Dataset](https://www.kaggle.com/datasets/rajugc/laptop-selection-dataset)
5. [Apple Stock (2013-2018)](https://www.kaggle.com/datasets/soheiltehranipour/apple-stock-20132018)

# Mysql with Docker
```
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<password> --name <container name> mysql
```
**Mac version is quite different**
1. amd64 version
```
docker run -d --platform linux/amd64 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<password> --name <container_name> mysql
```
2. arm64 version
```
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<password> --name <container_name> arm64v8/mysql
```