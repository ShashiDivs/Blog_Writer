from src.exception import BlogException
import os,sys
import wikipedia
# These are Tools for creating title and Content

def title_creator(blog_topic: str) -> str:
    """
    Generate a blog title based on the provided blog topic.

    Args:
        blog_topic (str): The topic of the blog.

    Returns:
        str: The generated blog title.
    """
    title = f"Deep Dive into {blog_topic}: Uncovering Hidden Insights"
    return title


def content_writer(title: str) -> str:
    """
    Generate detailed blog content using the provided title.

    Args:
        title (str): The blog title.

    Returns:
        str: The complete blog content.
    """
    content = (
        f"{title}\n\n"
        f"Please write a comprehensive blog post of at least 500 words on this subject. "
        f"In this comprehensive blog post, we explore the subject in depth. "
        f"Throughout the article, you'll discover various perspectives, insights, and practical examples. "
        f"Stay tuned as we uncover key takeaways and provide an engaging narrative around the topic."
    )
    return content


def recommendation_agent(title: str) -> str:
    """
    Recommend 5 sources based on the provided blog title by searching Wikipedia.

    Args:
        title (str): The blog title.

    Returns:
        str: A formatted string containing 5 recommended source titles.
    """
    try:
        # Search Wikipedia for the title, limiting to 5 results
        results = wikipedia.search(title, results=5)
        if results:
            recommendations = "Recommended Sources:\n" + "\n".join(f"{i+1}. {result}" for i, result in enumerate(results))
        else:
            recommendations = "No sources found."
    except Exception as e:
        raise BlogException(e,sys)
    return recommendations

