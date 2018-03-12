import requests


def test():
    url = "http://10.41.1.168/o/token/"
    post_data = {
        "client_id": "EfgBbx2qh6viPsZrNH7eBss3DbcVftYZAlx6tlUu",
        "grant_type": "client_credentials",
        "client_secret": "O798QPizlm1skRJcZlafVpiZzzUrUW6gGjZOXKe3Umh0Vo1hMkYe2bMihLZfFn8zVkhhqgKgBYAyBl1foFpIvyBahOu6WAzVXUmohjh8yOoJZo9RQ9c5qlgYdzGSZor4"
    }
    resp = requests.post(url, post_data)
    print("%r" % resp)
    if resp.status_code == 200:
        print(resp.json())
    else:
        print(resp.status_code)

test()