import click
import requests
import pprint


class FireWater:
    """Defines the the methods that implement the...

    ...functionality of FireWater App
    """


api_base_url = 'https://ah-django-staging.herokuapp.com/api'


@click.group()
def cli():
    """
    Contains executable sub-commands

    Try [firewater view --help] for details
    """
    pass


def get_resource_url(params=[]):
    """returns a full api url to fetch resource

    Keyword Arguments:
        params {list} -- [a list of url params in the required order] (
            default: {['articles', 'slug']})

    Returns:
        [string] -- [the full url path for resource]
    """
    resource_url = '/'.join([api_base_url]+params)
    return resource_url + '/'


@cli.command()
@click.option('--slug',
              help='Pass in a slug for a specific article view')
def view(slug=None):
    """Retrieves articles.
    For a specific article, pass in a slug

    Optional arguments:
        slug [string] -- [the slug of an article]
    """
    if slug is None:
        article_url = get_resource_url(['articles', 'feed'])
    else:
        article_url = get_resource_url(['articles', slug])

    article_resource = fetch_resource(article_url)
    if article_resource.status_code == 200:
        print({"Success": "{}".format(article_resource.status_code)})
        pretty_resource = pprint.pformat(article_resource.json(), indent=2)
        print(pretty_resource)
    elif article_resource.status_code == 404:
        print({"Not Found": "{}".format(article_resource.status_code)})
        print(article_resource.json())


def fetch_resource(resource_url):
    """fetches a resource given its url

    Arguments:
        resource_url {[string]} -- [the full url path to an api resource]
    """

    response = requests.get(resource_url)
    return response
