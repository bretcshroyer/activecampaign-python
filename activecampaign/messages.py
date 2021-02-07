class Messages(object):
    def __init__(self, client):
        self.client = client

    def list_all_messages(self, **params):
        """
        Retrieve all existing deals


        Returns:

        """
        return self.client._get("/messages", params=params)

    def retrieve_a_message(self, id):
        """
        retreive one message by id

        """
        return self.client._get("/messages/"+ str(id))
