import clips_random_joiner
import download_and_split_video


def start():
    urls_mixi = ['https://www.youtube.com/watch?v=3ZwlPYrMmy0',
            'https://www.youtube.com/watch?v=sKu4vZUaf5Q',
            'https://www.youtube.com/watch?v=eEtinQ7rCMs',
            'https://www.youtube.com/watch?v=FINtm0e7GJo',
            'https://www.youtube.com/watch?v=6CWSZWycPVg',
            'https://www.youtube.com/watch?v=y1hpI7KbpdA',
            'https://www.youtube.com/watch?v=6PP93b0cPww',
            'https://www.youtube.com/watch?v=0lKL4WrVg9Q',
            'https://www.youtube.com/watch?v=CoLA1zmPFpg',
            'https://www.youtube.com/watch?v=Jo3tpR-eHg8',
            'https://www.youtube.com/watch?v=U5ojEyZsIxk',
            'https://www.youtube.com/watch?v=TBnqPnBByLw',
            'https://www.youtube.com/watch?v=-o9rDR7r7Mk',
            'https://www.youtube.com/watch?v=QFTKnlkc5w4',
            'https://www.youtube.com/watch?v=mo4m3CkiPM8',
            'https://www.youtube.com/watch?v=HH50-9izH_0',
            'https://www.youtube.com/watch?v=5iNMA4wonIo',
            'https://www.youtube.com/watch?v=Ajx9AiGocqg',
            'https://www.youtube.com/watch?v=Nut6bG9vBdE',
            'https://www.youtube.com/watch?v=ObvIEYkTVe0',
            'https://www.youtube.com/watch?v=CTtdtOp_1so',
            'https://www.youtube.com/watch?v=cuBAUWKUnXo',
            'https://www.youtube.com/watch?v=8KEtaNTRPSU',
            'https://www.youtube.com/watch?v=UDLpY6GpgmM',
            'https://www.youtube.com/watch?v=tY6hOrh4584',
            'https://www.youtube.com/watch?v=CTtdtOp_1so',
            'https://www.youtube.com/watch?v=W06j4Ar-lYg',
            'https://www.youtube.com/watch?v=d_cU31lHRbU',
            'https://www.youtube.com/watch?v=5m_o2XydWHw',
            'https://www.youtube.com/watch?v=ZnsJfnusllg']

    urls_binge = ['https://www.youtube.com/watch?v=6T1yqrqO3p0',
                 'https://www.youtube.com/watch?v=eEDjJh2EPLU',
                 'https://www.youtube.com/watch?v=FOUiLsBFzlo',
                 'https://www.youtube.com/watch?v=u8EQKjkGbaQ',
                 'https://www.youtube.com/watch?v=nYxl05TbbHk',
                 'https://www.youtube.com/watch?v=OngQP506h3k',
                 'https://www.youtube.com/watch?v=2rgo5iqa1mc',
                 'https://www.youtube.com/watch?v=ApDRoxaxtAo',
                 'https://www.youtube.com/watch?v=TJG45Y-CsA0',
                 'https://www.youtube.com/watch?v=EsYchGLgIi0',
                 'https://www.youtube.com/watch?v=lTRdoWNzPxo',
                 'https://www.youtube.com/watch?v=yzOTgleOdws',
                 'https://www.youtube.com/watch?v=Hkpf_1QaqXY',
                 'https://www.youtube.com/watch?v=qJKZLhvGvcY',
                 'https://www.youtube.com/watch?v=8BEgO8V0riw',
                 'https://www.youtube.com/watch?v=wg5DHKMJHuo',
                 'https://www.youtube.com/watch?v=gVqraZZltO4',
                 'https://www.youtube.com/watch?v=q42OAo3A7j4',
                 'https://www.youtube.com/watch?v=WZ77oraVPQ8',
                 'https://www.youtube.com/watch?v=L6KbFZCo5fk',
                 'https://www.youtube.com/watch?v=O3qBEN3SQpQ',
                 'https://www.youtube.com/watch?v=nhEz7X-QMPU',
                 'https://www.youtube.com/watch?v=B48kx1ZiyU4',
                 'https://www.youtube.com/watch?v=9igdUM7fJ3M',
                 'https://www.youtube.com/watch?v=Xg81JII0XVM',
                 'https://www.youtube.com/watch?v=1tHct2Er5b0',
                 'https://www.youtube.com/watch?v=2zYw2qRfW2s',
                 'https://www.youtube.com/watch?v=QM_MnGFM4Ng',
                 'https://www.youtube.com/watch?v=nI89RHbR7nc',
                 'https://www.youtube.com/watch?v=PvcaIJbmBKA']

    download_and_split_video.download_and_split_by_clips(urls_binge)
    clips_random_joiner.join_clips(14)


start()
