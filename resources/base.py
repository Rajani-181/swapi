not_implemented_error_msg = "This method is not implemented"

# TODO - you can also convert this class into abstract class and
# define methods as abstract methods

class SampleDataException(Exception):
    def __init__(self, message, errors=""):
        print("message coming from our custom exception class")
        super.__init__(message)
        self.errors = errors


class ResourceBase(object):
    """
       Base class representing required methods to be implemented by all resource
       classes
    """

    # TODO - add all resources in the list
    resources = ["planets", "spaceships", "people", "vehicles"]

    def __init__(self):
        self.home_url = "https://swapi.dev/" #https://swapi.dev/api/films/

    def get_count(self):
        raise NotImplementedError(not_implemented_error_msg)

    def get_resource_urls(self):
        raise NotImplementedError(not_implemented_error_msg)

    def get_sample_data(self):
        raise SampleDataException(not_implemented_error_msg)
