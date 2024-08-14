echo "#!/bin/env bash
PROJECT_NAME=Eather
DATABASE_URI=mysql+pymysql://<db_user>:<user_password>@<user_host>/<db_name>
ACCESS_TOKEN_SECRET=<your_access_secret>
REFRESH_TOKEN_SECRET=<your_refresh_secret>
ACCESS_TOKEN_EXPIRE_MINUTES=30
" > .env