from deepsegment import DeepSegment
# The default language is 'en'
segmenter = DeepSegment('en', tf_serving=True)
segmenter.segment('I am Batman i live in gotham')