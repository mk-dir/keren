def is_weird(number):
    # Implementing the Constraint 1<= n <= 100
    if number > 100:
        return 'Number Greater than 100'
    else:
    #Test whether Number is Even using
    # modulus operator
        if number%2==0:
            if number >=2 and number <=5:
                return 'not weird'
            #Inclusive range between 2 & 5
            elif number >=6 and number <=20:
                return 'weird'
            elif number >20:
                return 'not weird'
        else:
            return 'Weird'


number=int(input('Enter a number between 0 & 100: '))
print(is_weird(number))

