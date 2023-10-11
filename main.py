import datetime
import requests
import tomllib


def main():
    # Read in configuration
    with open("config.toml", "rb") as config_file:
        config = tomllib.load(config_file)
        location = config["location"]
        model = config["model"]
        discord_webhook = config.get("discord_webhook", "")

    # Request data from Apple endpoint
    response = requests.get(
        "https://www.apple.com/shop/fulfillment-messages",
        params={
            "parts.0": model,
            "location": location,
        },
    )

    # Parse result data to determine available stores
    stores = response.json()["body"]["content"]["pickupMessage"]["stores"]
    available_stores = []
    model_name = ""
    for store in stores:
        store_name = "Apple {0}".format(store["storeName"])
        store_model = store["partsAvailability"][model]
        available = store_model["pickupDisplay"]
        if model_name == "":
            model_name = store_model["messageTypes"]["regular"][
                "storePickupProductTitle"
            ]
        if available == "available":
            available_stores.append(store_name)

    # Send notification
    if len(available_stores) > 0:
        message = "{0} is available!\n\nAvailable stores:\n{1}".format(
            model_name, ", ".join(available_stores)
        )
        print(message)
        if discord_webhook != "":
            response = requests.post(discord_webhook, data={"content": message})


if __name__ == "__main__":
    main()
