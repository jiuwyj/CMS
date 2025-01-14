def search_symbol(input_string):
    def run(start_state, input_string,states, alphabet, transitions):
        current_state = start_state
        for symbol in input_string:
            if symbol not in alphabet:
                return False
            #print(transitions[current_state].get(symbol))
            if transitions.get(current_state):
                if transitions[current_state].get(symbol):
                    current_state = transitions[current_state][symbol]
                    continue
                # elif not transitions[current_state].get(symbol):
                #     return current_state
                #     break
            else:
                return current_state

        return current_state

    states = {'0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27',
                '28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50'}
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','.'}
    transitions = {
        '0': {'d': '1','o': '15','f':'18','a':'19','p':'23','c':'29','t':'43','d':'1','j':'46','r':'13','h':'14','s':'42','i':'2'},
        '2': {'p': '3','c': '4','s':'10','c':'4'},
        '4': {'p': '5'},
        '5': {'.': '6'},
        '6': {'n': '7','t': '8','w': '9'},
        '10': {'p': '11','_': '12'},
        '15': {'r': '16','s': '17'},
        '19': {'s': '20'},
        '20': {'n': '21','t': '10','w': '14'},
        '21': {'_': '22'},
        '23': {'o': '24','r': '25'},
        '25': {'o': '26'},
        '26':{'t': '27','v': '28'},
        '29':{'i': '30','o': '31','e': '32','l': '41'},
        '32':{'r': '33'},
        '33':{'t': '34'},
        '34':{'_': '35'},
        '35':{'n': '36','i': '37','s': '38'},
        '38':{'e': '39','u': '40'},
        '43':{'i': '44','r': '45'},
        '46':{'s': '47'},
        '47':{'_': '48'},
        '48':{'m': '49','n': '50'}
    }
    start_state = '0'
    a=run(start_state,input_string,states, alphabet, transitions)
    return a

