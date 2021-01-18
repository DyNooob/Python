from __future__ import print_function

import json
import six

import paddlehub as hub

if __name__ == "__main__":
    # Load porn_detection_lstm module
    porn_detection_lstm = hub.Module(name="porn_detection_lstm")

    test_text = [line.strip('\n') for line in open('text.txt', 'r', encoding='utf-8').readlines() if line.strip('\n') != '']

    input_dict = {"text": test_text}

    results = porn_detection_lstm.detection(data=input_dict)

    porn_result = {
        'porn': 0,
        'not_porn': 0
    }
    man_result = {
        '赞赞': 0,
        '王一博': 0
    }
    for index, text in enumerate(test_text):
        results[index]["text"] = text
    for index, result in enumerate(results):
        if six.PY2:
            print(json.dumps(results[index],
                encoding="utf8", ensure_ascii=False))
        else:
            if results[index]['porn_probs'] > 0.7:
                porn_result['porn'] += 1
            else:
                porn_result['not_porn'] += 1
                
            if '王一博' in results[index]['text'] and results[index]['porn_probs'] > 0.7:
                man_result['王一博'] += 1
            if '赞赞' in results[index]['text'] and results[index]['porn_probs'] > 0.7:
                man_result['赞赞'] += 1

    print(man_result)
