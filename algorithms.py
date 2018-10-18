import pandas

class MostPopular():
    def __init__(self):
        self.train_data = None
        self.user = None
        self.song = None
        self.pop_rec = None

    def pop_model(self, train_data, user, song):
        self.train_data = train_data
        self.user = user
        self.song = song
        train_df = self.train_data.groupby([self.song]).agg({self.user: 'count'})
        train_df = train_df.sort_values(by='count', ascending=False).reset_index()
        self.pop_rec = train_df.head(10)

    def rec_pop_model(self, user):
        pop_rec = self.pop_rec
        pop_rec['user'] = user
        return pop_rec

