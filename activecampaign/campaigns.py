class Campaigns(object):
    def __init__(self, client):
        self.client = client

    def list_all_campaigns(self, **params):
        """
        Retrieve all existing campaigns
        Returns:
        """
        return self.client._get("/campaigns", params=params)

    def retrieve_a_campaign(self, id):
        """
        retreive one campaign by id

        """
        return self.client._get("/campaigns/"+ str(id))

    def retrieve_a_campaign_message(self, id):
        """
        retreive one campaign message by id

        """
        return self.client._get("/campaigns/"+ str(id)+"/campaignMessage")


    