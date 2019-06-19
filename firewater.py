import click
import requests
import json


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
@click.option("-s", "--save", is_flag=True, help="export to json file")
def list(save=None):
    """Retrieves an article

    """
    article_url = get_resource_url(['articles', 'feed'])

    article_resource = fetch_resource(article_url)

    formart_output(article_resource.status_code, article_resource.json())

    if save:
        export_to_json(article_resource.json()['results'])


@cli.command()
@click.argument('slug')
@click.option("-s", "--save", is_flag=True, help="export to json file")
def view(slug, save=None):
    article_url = get_resource_url(['articles', slug])
    article_resource = fetch_resource(article_url)

    formart_output(
        article_resource.status_code,
        article_resource.json())

    if save:
        export_to_json(
            article_resource.json()['title'],
            article_resource.json())


def fetch_resource(resource_url):
    """fetches a resource given its url

    Arguments:
        resource_url {[string]} -- [the full url path to an api resource]
    """

    response = requests.get(resource_url)
    return response


def formart_output(status_code, output):

    if status_code == 200:
        print({"Success": "{}".format(status_code)})
        pretty_resource = json.dumps(output, indent=4)
        print(pretty_resource)
        return pretty_resource
    elif status_code == 404:
        print({"Not Found": "{}".format(status_code)})
        print(output)
        return output
    else:
        print({"Error occurred": "{}".format(status_code)})
        print(output)
        return output


def export_to_json(data, file_name='articles'):
    with open(
            '{}.json'.format(file_name), 'w') as json_file:
        exported_data = json.dump(data, json_file, indent=2)

    return exported_data
