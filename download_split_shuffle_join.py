import clips_random_joiner
import download_and_split_video


def start():
    # urls = ['https://www.youtube.com/watch?v=3ZwlPYrMmy0',
    #         'https://www.youtube.com/watch?v=sKu4vZUaf5Q',
    #         'https://www.youtube.com/watch?v=eEtinQ7rCMs',
    #         'https://www.youtube.com/watch?v=FINtm0e7GJo',
    #         'https://www.youtube.com/watch?v=6CWSZWycPVg',
    #         'https://www.youtube.com/watch?v=y1hpI7KbpdA',
    #         'https://www.youtube.com/watch?v=6PP93b0cPww',
    #         'https://www.youtube.com/watch?v=0lKL4WrVg9Q',
    #         'https://www.youtube.com/watch?v=CoLA1zmPFpg',
    #         'https://www.youtube.com/watch?v=Jo3tpR-eHg8',
    #         'https://www.youtube.com/watch?v=U5ojEyZsIxk',
    #         'https://www.youtube.com/watch?v=TBnqPnBByLw',
    #         'https://www.youtube.com/watch?v=-o9rDR7r7Mk',
    #         'https://www.youtube.com/watch?v=QFTKnlkc5w4',
    #         'https://www.youtube.com/watch?v=mo4m3CkiPM8',
    #         'https://www.youtube.com/watch?v=HH50-9izH_0',
    #         'https://www.youtube.com/watch?v=5iNMA4wonIo',
    #         'https://www.youtube.com/watch?v=Ajx9AiGocqg',
    #         'https://www.youtube.com/watch?v=Nut6bG9vBdE',
    #         'https://www.youtube.com/watch?v=ObvIEYkTVe0',
    #         'https://www.youtube.com/watch?v=CTtdtOp_1so']
    urls = ['https://www.youtube.com/watch?v=3ZwlPYrMmy0',
            'https://www.youtube.com/watch?v=sKu4vZUaf5Q']

    download_and_split_video.download_and_split_by_clips(urls)
    clips_random_joiner.join_clips(6)


start()
