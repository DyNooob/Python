import paddlehub as hub

senta = hub.Module(name="senta_lstm")
test_text = [line.strip('\n') for line in open('text.txt', 'r', encoding='utf-8').readlines() if line.strip('\n') != '']
input_dict = {"text": test_text}
results = senta.sentiment_classify(data=input_dict)
emotion_result = {
    'neg': 0,
    'pos': 0,
    'mid': 0
}
man_result = {
    '赞赞': 0,
    '王一博': 0
}
for result in results:
    if result['negative_probs'] > 0.7:
        emotion_result['neg'] += 1
    elif result['positive_probs'] > 0.7:
        emotion_result['pos'] += 1
    else:
        emotion_result['mid'] += 1
    
    if '王一博' in result['text'] and result['negative_probs'] > 0.7:
        man_result['王一博'] += 1
    if '赞赞' in result['text'] and result['negative_probs'] > 0.7:
        man_result['赞赞'] += 1
print(man_result)