from helper import main_passw,menu,add_passw,view_passw,delete_passw_by_app,delete_all_passw,eddit,get_name_passw,exit_program
if __name__=="__main__":
    main_passw()
    while True:
        menu()
        decision = input("Your choice: ")
        if decision.isdigit():
            pass
        else:
            print("Type number please")
            continue
        if int(decision) > 0 and int(decision) < 8:
            if int(decision) == 1:
                add_passw()
            if int(decision) == 2:
                view_passw()
            if int(decision) == 3:
                delete_passw_by_app()
            if int(decision) == 4:
                delete_all_passw()
            if int(decision) == 5:
                eddit()
            if int(decision) == 6:
                get_name_passw()
            if int(decision) == 7:
                exit_program()
        else:
            print("You write a wrong number")
            continue
