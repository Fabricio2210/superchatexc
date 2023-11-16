def get_data_parsed(infos):
    array_data = []

    for info in infos:
        data = {
            "id": info["author"]["id"],
            "profilePicture": info["author"]["images"][0]["url"],
            "name": info["author"]["name"]
        }

        message_type = info["message_type"]
        if message_type == "membership_item":
            data["message"] = info["header_secondary_text"]
            data["isGifted"] = False
        elif message_type == "sponsorships_gift_purchase_announcement":
            data["message"] = info["message"]
            data["isGifted"] = True
        else:
            data["money"] = info["money"]["text"]
            data["currency"] = info["money"]["currency"]
            data["message"] = info["message"]
            data["isGifted"] = False

        array_data.append(data)

    return array_data