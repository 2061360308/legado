import requests
import os


def get_discussion_id(token, number):
    headers = {"Authorization": f"Bearer {token}"}
    query = """
    {
      repository(owner: "2061360308", name: "legado") {
        discussion(number: %d) {
          id
        }
      }
    }
    """ % (number)
    response = requests.post('https://api.github.com/graphql', headers=headers, json={'query': query})
    print("获取id：", response.json())
    return response.json()['data']['repository']['discussion']['id']


def replay_discussion(token, discussion_number, content):
    # headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.biscayne-preview+json'}
    # data = {
    #     'body': content
    # }
    # response = requests.post(
    #     f'https://api.github.com/repos/2061360308/legado/discussions/{discussion_number}/comments',
    #     headers=headers,
    #     json=data
    # )
    # print(response.json())
    headers = {"Authorization": f"Bearer {token}"}
    query = """
        mutation($input: AddDiscussionCommentInput!) {
          addDiscussionComment(input: $input) {
            clientMutationId
          }
        }
        """
    variables = {
        "input": {
            "body": content,
            "discussionId": get_discussion_id(token, discussion_number)
        }
    }
    response = requests.post('https://api.github.com/graphql', headers=headers,
                             json={'query': query, 'variables': variables})
    print("自动回复：", response.json())
    # response = requests.get(
    #     'https://api.github.com/repos/2061360308/legado',
    #     headers=headers
    # )
    # print(response.json())


if __name__ == '__main__':
    replay_discussion(os.getenv("GITHUB_TOKEN"), 7, "这是api回复的内容")