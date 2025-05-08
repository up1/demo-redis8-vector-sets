# Demo :: Redis with [Vector Set](https://redis.io/blog/announcing-vector-sets-a-new-redis-data-type-for-vector-similarity/)


## 1. Create Redis 8 server
```
$docker compose up -d redis
$docker compose ps
```

## 2. Working with Redis-CLI
```
$docker compose exec redis bash
$redis-cli
```
Instructions
```
# Add datas
$VADD mydata VALUES 4 0.5 1.2 0.75 3.8 "I love dogs"
$VADD mydata VALUES 4 0.5 1.2 0.75 3.8 "I like cats"
$VADD mydata VALUES 4 0.5 1.2 0.75 3.8 "I enjoy birds"

# Show embedding data
$VEMB mydata "I love dogs"
$VEMB mydata "I like cats"
$VEMB mydata "I enjoy birds"

# Show basic information of vector set
$VDIM mydata
$VCARD mydata
$VINFO mydata

# Similarity search for "I love dogs"
$VSIM mydata ELE "I love dogs" WITHSCORES COUNT 3
1) "I love dogs"
2) "1"
3) "I like cats"
4) "0.8427733480930328"
5) "I enjoy birds"
6) "0.7713080942630768"


# Similarity search for "I love" => embedding
$VSIM mydata VALUES <embedding> WITHSCORES COUNT 3
1) "I love dogs"
2) "0.7879546731710434"
3) "I like cats"
4) "0.7277481257915497"
5) "I enjoy birds"
6) "0.7191725969314575"

```

## 3. Working with Redis with Python
```
$pip install -r requirements.txt
$python 1_store_data.py
$python 2_search.py
```