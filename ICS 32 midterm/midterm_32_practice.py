try:

    try:

        a = 5

        b = 7

        c = "five"

        d = "seven"

        print(a*c) 

        print(c+d) 

    except:

        print(b*c) 

    else:

        print(c*d) 

    finally:

        print("first finally") 

except:

    print("second except") 

else:

    print("second else") 

finally:

    print("second finally") 


