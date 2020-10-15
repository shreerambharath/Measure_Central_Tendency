import pickle
import hashlib

def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

# def geth(obj):
#     obj = str(obj).encode()
#     m = hashlib.md5()
#     m.update( bytes(obj) )
#     return m.hexdigest()    
    
def test1():
    t = get_pickle('AvocadoNB/q1.pickle')
    assert '89170b9b74123fd955f7d352966d9f48'==t
    
def test2():
    t = get_pickle('AvocadoNB/q2.pickle')
    assert '81c60c6ea86b5ea2827d02da4e7c7703'==t

def test3():
    t = get_pickle('AvocadoNB/q3.pickle')
    assert '6b32b098c57381654f12b1cab1859014'==t


def test4():
    t = get_pickle('AvocadoNB/q4.pickle')
    assert '246c0903b5a64b2a854ec1e7865f174f'==t


def test5():
    t = get_pickle('AvocadoNB/q5.pickle')
    assert '305cf1fb13b9539dcd317a0354c9ed61'==t
