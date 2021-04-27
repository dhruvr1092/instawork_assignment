## Installation

Using pip

```bash
pip install -r requirements.txt
```
## Init

```
python manage.py makemigrations
```

```
python manage.py makemigrations team_management 
```

```
python manage.py migrate
```

```
python manage.py runserver
```

For now have used sqlite, if needed can include MySql with a docker file 

## Curls


To add a new team-member
```
curl -i -XPOST http://localhost:8000/team-members -d '{"email": "member1@instawork.com", "phone": "9234567890", "first_name": "Robert", "last_name": "Lewandowski", "role": "admin" }' -H 'Content-Type: application/json'    
```

To view list of all team-members
```
curl -i -XGET http://localhost:8000/team-members 
```
To view details of a particular team-member
```
curl -i -XGET http://localhost:8000/team-members/{id}
```

To edit details of a particular team-member
```
curl -i -XPUT http://localhost:8000/team-members/{id} -d '{"email": "member1@instawork.com", "phone": "9234567891", "first_name": "Robert", "last_name": "Lewandowski", "role": "admin" }' -H 'Content-Type: application/json' 
```
partial edit
```
curl -i -XPUT http://localhost:8000/team-members/{id} -d '{"email": "member1@instawork.com", "phone": "9234567892"}' -H 'Content-Type: application/json' 
```

To delete details of a particular team-member
```
curl -i -XDELETE http://localhost:8000/team-members/{id}
```

## Swagger docs

```python
http://localhost:8000/_docs/
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
