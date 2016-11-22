from tweepy.streaming import StreamListener


class TwitterListener(StreamListener):
    def on_data(self, data):
        try:
            with open('data.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print(str(e))
            return True

    def on_error(self, status):
        print(status)
        return True