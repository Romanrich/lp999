from pprint import pprint

CONTACTS = {}


def input_error(func):
   
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Ви ввели не вірне ім'я"
        except TypeError:
            return "Ви ввели не вірний форат команди"
        except IndexError:
            return "Введіть ім'я та телефон"
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args

    return wrapper




def main():
    
    

    @input_error
    def quit_func():
        quit()
        print('Good bye!')




    @input_error
    def hello_contact():
        print('How can I help you?')



    @input_error
    def add_contact ():
        name = input('Enter name!')
        phone = input('Enter phone!')
        CONTACTS[name] = phone
        print ('Contact added')




    @input_error
    def show_all():
        pprint (CONTACTS)


    

    @input_error
    def change_contact():
        name = input('Enter name!')
        CONTACTS[name] = input('Enter phone!')







    @input_error
    def phone_contact():
        name = input('Enter name!')
        print (name, CONTACTS[name])

    commands = {
        'exit' : quit_func,

        'good bye' : quit_func,

        'close' : quit_func,

        'add' : add_contact,

        'phone' : phone_contact,

        'hello' : hello_contact,

        'show all' : show_all,


        'change' : change_contact,
    }
     

    while True :
        comn  = input('Enter command!:')
    
        if comn not in commands:
            print('Non command')
            continue
        commands[comn]()

if __name__ == '__main__':
    main()