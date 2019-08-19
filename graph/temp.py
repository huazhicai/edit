data = {
    'nodes': [
        {'preQueryNodes': None, 'args': [('Url', 12), ('kwargs', 13)], 'returns': (('Doc', 0), ('Result', 1)),
         'eventLinks': {'Out': [(2, 'ConsoleOutput'), (3, 'ContainerGetItem')]}, 'preLinks': {'In': True},
         'returns_linked': True},

        {'preQueryNodes': None, 'args': [], 'returns': (), 'eventLinks': {'Out': [(0, 'PyQueryUrl')]},
         'preLinks': {}},

        {'preQueryNodes': None, 'args': [('Doc', 0)], 'returns': (), 'eventLinks': {}, 'preLinks': {'In': True}},

        {'preQueryNodes': None, 'args': [('doc_in', 1), ('field', 14)], 'returns': (('doc_out', 2),),
         'eventLinks': {'Out': [(4, 'IteratorList')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('doc_in', 2)], 'returns': (('doc', 3),),
         'eventLinks': {'Out': [(5, 'StringConcat')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('prefix', 15), ('suffix', 3)], 'returns': (('result', 4),),
         'eventLinks': {'Out': [(6, 'PyQueryUrl')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('Url', 4), ('kwargs', 16)], 'returns': (('Doc', 5), ('Result', 6)),
         'eventLinks': {'Out': [(7, 'ContainerGetItem')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('doc_in', 6), ('field', 17)], 'returns': (('doc_out', 7),),
         'eventLinks': {'Out': [(8, 'IteratorList')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('doc_in', 7)], 'returns': (('doc', 8),),
         'eventLinks': {'Out': [(9, 'PyQueryUrl'), (10, 'ConsoleOutput')]}, 'preLinks': {'In': True},
         'returns_linked': True},

        {'preQueryNodes': None, 'args': [('Url', 8), ('kwargs', 18)], 'returns': (('Doc', 9), ('Result', 10)),
         'eventLinks': {'Out': [(11, 'FieldMakeup')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('Doc', 8)], 'returns': (), 'eventLinks': {}, 'preLinks': {'In': True}},

        {'preQueryNodes': None, 'args': [('doc_in', 9), ('kwargs', 19)], 'returns': (('doc_out', 11),),
         'eventLinks': {'Out': [(12, 'ConsoleOutput')]}, 'preLinks': {'In': True}, 'returns_linked': True},

        {'preQueryNodes': None, 'args': [('Doc', 11)], 'returns': (), 'eventLinks': {},
         'preLinks': {'In': True}}],

    'runTimeData': [
        None, None, None, None, None, None, None, None, None, None, None, None, 'www',
        {'departments': ['.clearfix > li > a', True, 'href']}, 'departments', 'www',
        {'doctors': ['.ks_yishi > ul > li > a', True, 'href']}, 'doctors',
        {'name': ['#showexpdiv > ul > li.zj_xm > strong', False, None]},
        {'hospital': '北京301医院', 'grade': '三甲'}
    ]
}

data1 = {
    'nodes':
        [{'inputs': [('Url', 12), ('kwargs', 13)], 'outputs': (('Doc', 0), ('Result', 1)),
          'event_links': {'Out': [(2, 'ConsoleOutput'), (3, 'ContainerGetItem')]}, 'preLinks': {'In': True},
          'returns_linked': True},
         {'inputs': [], 'outputs': (), 'event_links': {'Out': [(0, 'PyQueryUrl')]}, 'preLinks': {}},
         {'inputs': [('Doc', 0)], 'outputs': (), 'event_links': {}, 'preLinks': {'In': True}},
         {'inputs': [('doc_in', 1), ('field', 14)], 'outputs': (('doc_out', 2),),
          'event_links': {'Out': [(4, 'IteratorList')]}, 'preLinks': {'In': True}, 'returns_linked': True},
         {'inputs': [('doc_in', 2)], 'outputs': (('doc', 3),), 'event_links': {'Out': [(5, 'StringConcat')]},
          'preLinks': {'In': True}, 'returns_linked': True},
         {'inputs': [('prefix', 15), ('suffix', 3)], 'outputs': (('result', 4),),
          'event_links': {'Out': [(6, 'PyQueryUrl')]}, 'preLinks': {'In': True}, 'returns_linked': True},
         {'inputs': [('Url', 4), ('kwargs', 16)], 'outputs': (('Doc', 5), ('Result', 6)),
          'event_links': {'Out': [(7, 'ContainerGetItem')]}, 'preLinks': {'In': True},
          'returns_linked': True}, {'inputs': [('doc_in', 6), ('field', 17)], 'outputs': (('doc_out', 7),),
                                    'event_links': {'Out': [(8, 'IteratorList')]}, 'preLinks': {'In': True},
                                    'returns_linked': True},
         {'inputs': [('doc_in', 7)], 'outputs': (('doc', 8),),
          'event_links': {'Out': [(9, 'PyQueryUrl'), (10, 'ConsoleOutput')]}, 'preLinks': {'In': True},
          'returns_linked': True},
         {'inputs': [('Url', 8), ('kwargs', 18)], 'outputs': (('Doc', 9), ('Result', 10)),
          'event_links': {'Out': [(11, 'FieldMakeup')]}, 'preLinks': {'In': True}, 'returns_linked': True},
         {'inputs': [('Doc', 8)], 'outputs': (), 'event_links': {}, 'preLinks': {'In': True}},
         {'inputs': [('doc_in', 9), ('kwargs', 19)], 'outputs': (('doc_out', 11),),
          'event_links': {'Out': [(12, 'ConsoleOutput')]}, 'preLinks': {'In': True}, 'returns_linked': True},
         {'inputs': [('Doc', 11)], 'outputs': (), 'event_links': {}, 'preLinks': {'In': True}}],
    'runTimeData':
        [
            None, None, None, None, None, None, None, None, None, None, None, None, 'www',
            {'departments': ['.clearfix > li > a', True, 'href']}, 'departments', 'www',
            {'doctors': ['.ks_yishi > ul > li > a', True, 'href']}, 'doctors',
            {'name': ['#showexpdiv > ul > li.zj_xm > strong', False, None]},
            {'hospital': '北京301医院', 'grade': '三甲'}
        ]
}

data2 = {
    'nodes': [{'event_actions': {'Default': 'Start'}, 'event_links': {'Out': {1: 'In'}}, 'inputs': {}, 'outputs': {}},
              {'event_actions': {'In': 'PyQueryUrl'}, 'event_links': {'Out': {2: 'In', 3: 'In'}},
               'inputs': {'Url': 13, 'kwargs': 14}, 'outputs': {'Doc': 0, 'Result': 1}},
              {'event_actions': {'In': 'ConsoleOutput'}, 'event_links': {}, 'inputs': {'Doc': 0}, 'outputs': {}},
              {'event_actions': {'In': 'ContainerGetItem'}, 'event_links': {'Out': {4: 'In'}},
               'inputs': {'doc_in': 1, 'field': 15}, 'outputs': {'doc_out': 2}},
              {'event_actions': {'In': 'IteratorList'}, 'event_links': {'Out': {5: 'In'}}, 'inputs': {'doc_in': 2},
               'outputs': {'doc': 3}},
              {'event_actions': {'In': 'StringConcat'}, 'event_links': {'Out': {6: 'In', 7: 'In'}},
               'inputs': {'prefix': 16, 'suffix': 3}, 'outputs': {'result': 4}},
              {'event_actions': {'In': 'ConsoleOutput'}, 'event_links': {}, 'inputs': {'Doc': 4}, 'outputs': {}},
              {'event_actions': {'In': 'PyQueryUrl'}, 'event_links': {'Out': {8: 'In'}},
               'inputs': {'Url': 4, 'kwargs': 17}, 'outputs': {'Doc': 5, 'Result': 6}},
              {'event_actions': {'In': 'ContainerGetItem'}, 'event_links': {'Out': {9: 'In'}},
               'inputs': {'doc_in': 6, 'field': 18}, 'outputs': {'doc_out': 7}},
              {'event_actions': {'In': 'IteratorList'}, 'event_links': {'Out': {10: 'In'}}, 'inputs': {'doc_in': 7},
               'outputs': {'doc': 8}},
              {'event_actions': {'In': 'StringConcat'}, 'event_links': {'Out': {11: 'In', 14: 'In'}},
               'inputs': {'prefix': 19, 'suffix': 8}, 'outputs': {'result': 9}},
              {'event_actions': {'In': 'PyQueryUrl'}, 'event_links': {'Out': {12: 'In'}},
               'inputs': {'Url': 9, 'kwargs': 20}, 'outputs': {'Doc': 10, 'Result': 11}},
              {'event_actions': {'In': 'FieldMakeup'}, 'event_links': {'Out': {13: 'In'}},
               'inputs': {'doc_in': 11, 'kwargs': 21}, 'outputs': {'doc_out': 12}},
              {'event_actions': {'In': 'ConsoleOutput'}, 'event_links': {}, 'inputs': {'Doc': 12}, 'outputs': {}},
              {'event_actions': {'In': 'ConsoleOutput'}, 'event_links': {}, 'inputs': {'Doc': 9}, 'outputs': {}}],
    'runTimeData': [None, None, None, None, None, None, None, None, None, None, None, None, None,
                    'www.301hospital.mil.cn', {'departments': ['.clearfix > li > a', True, 'href']}, 'departments',
                    'www.301hospital', {'doctors': ['.ks_yishi > ul > li > a', True, 'href']}, 'doctors',
                    'www.301hospital.com', {'name': ['#showexpdiv > ul > li.zj_xm > strong', False, None],
                                            'title': ['#showexpdiv > ul > li.zj_xm', False, None],
                                            'department': ['#showexpdiv > ul > li.zj_xm', False, None],
                                            'special': ['div.zj_ys_b>p', False, None],
                                            'resume': ['#showexpdiv > ul > li.zj_jj > p:nth-child(1)', False, None],
                                            'outpatient_info': ['div.zj_ys_b > table > tr', False, None]},
                    {'hospital': '北京301医院', 'grade': '三甲'}]}
