# FastAPI SqlModel Social Login


## DB 접속정보 설정

```markdown
DB_HOST=localhost
DB_USERNAME=postgres
DB_PASSWORD=1234Aoeu
DB_PORT=5432
DB_NAME=flowview
```

ex)

postgresql+asyncpg://postgres:1234Aoeu@localhost:5432/flowview

### DB Connector

DB컨넥터는 asyncpg를 사용합니다. psycopg2를 사용하면 아래와 같은 에러가 발생 합니다.

sqlalchemy.exc.InvalidRequestError: The asyncio extension requires an async driver to be used. The loaded 'psycopg2' is not async.


# 참고

[SQLModel](https://fastapi.tiangolo.com/tutorial/sql-databases/)