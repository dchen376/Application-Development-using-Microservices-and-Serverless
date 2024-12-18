import connexion
import six

from swagger_server import util


def greetings_get():  # noqa: E501
    """Returns a list of Greetings

    Returns greetings in different languages # noqa: E501


    :rtype: None
    """
    hellos = {
        "English": "hello",
        "Hindi": "namastey",
        "Spanish": "hola",
        "French": "bonjour",
        "German": "guten tag",
        "Italian": "salve",
        "Chinese": "nǐn hǎo",
        "Portuguese": "olá",
        "Arabic": "asalaam alaikum",
        "Japanese": "konnichiwa",
        "Korean": "anyoung haseyo",
        "Russian": "Zdravstvuyte"
    }

    return hellos
