import requests

Base = "http://127.0.0.1:8081/person_search/api"


def get_traces():
    url = Base + "/traces"
    request = requests.get(url)
    with open("test.txt", 'w') as f:
        f.write(request.content)
    return request.content


def get_videos():
    url = Base + "/videos"
    request = requests.get(url)
    return request.json()


if __name__ == "__main__":
    get_traces()
    print(get_videos())
