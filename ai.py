import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def blog_post_to_bullet_points(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Convert the following blog post into bullet points:"},
            {"role": "user", "content": content}
        ]
    )
    bullet_points = response.choices[0].message['content']
    return bullet_points

def generate_content_ideas(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate content ideas based on the following summary:"},
            {"role": "user", "content": content}
        ]
    )
    ideas = response.choices[0].message['content']
    return ideas

def generate_facebook_post(content, length):
    prompt = f"Generate a {length} Facebook post based on the following summary:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )
    post = response.choices[0].message['content']
    return post
