import requests

def scrape_facebook_posts(url):
    # Placeholder function for scraping Facebook posts
    # Implement actual scraping logic here
    posts = []
    # Simulated data for demonstration
    for i in range(1, 21):
        posts.append({
            'content': f'Post content {i} from {url}',
            'shares': i * 10,
            'comments': i * 5,
            'likes': i * 2
        })
    return posts